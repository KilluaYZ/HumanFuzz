from flask import Blueprint, request, send_file, Request
from bson import ObjectId

import config
from codecheck.utils.Tools import *
from flask import Blueprint, request
from codecheck.utils.build_response import *
from codecheck.database.Mongo import Mongo
from codecheck.utils.myExceptions import *
from codecheck.utils.file import *
from codecheck.utils.Logger import logger
import datetime
from codecheck.container.DockerManager import DockerManager, DockerContainer
import codecheck.utils.requests as mrequests
from codecheck.analyser.TargetCoverage import cal_target_coverage
import subprocess
import shutil
import os
bp = Blueprint('project', __name__, url_prefix='/project')
mongo = Mongo()

TargetCoverageMap = {}

@bp.route('/add', methods=['POST'])
def add_project():
    try:
        name = request.json.get('name')
        container_id = request.json.get('container_id')
        checkFrontendArgsIsNotNone(
            [
                {"key":"name","val":name},
                {"key": "container_id", "val": container_id},
            ]
        )
        user = check_user_before_request(request)
        row = mongo.insert_one('Project',
           {"name":name,
            "container_id":container_id,
            "user_id": user['_id'],
            "create_time": datetime.datetime.now(),
            "last_start_time": datetime.datetime.now(),
            "binary_path": "",
            "binary_cov_path": "",
            "output_path": "",
            "input_path": "",
            "binary_args": "",
            "target_path": "",
            "status": "stop"
            })
        _id = row.inserted_id
        project = mongo.find_one('Project',{"_id": _id})
        return build_success_response(project)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/config', methods=['POST'])
def config_project():
    try:
        project_id = request.json.get('project_id')
        binary_path = request.json.get('binary_path')
        binary_cov_path = request.json.get('binary_cov_path')
        output_path = request.json.get('output_path')
        input_path = request.json.get('input_path')
        binary_args = request.json.get('binary_args')
        target_path = request.json.get('target_path')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
                {"key": "binary_path", "val": binary_path},
                {"key": "binary_cov_path", "val": binary_cov_path},
                {"key": "output_path", "val": output_path},
                {"key": "input_path", "val": input_path},
                {"key": "binary_args", "val": binary_args},
                {"key": "target_path", "val": target_path},
            ]
        )
        user = check_user_before_request(request)
        row = mongo.update_one('Project',{"_id": ObjectId(project_id), "user_id": user['_id']},
    {"$set": {
            "binary_path": binary_path,
            "binary_cov_path": binary_cov_path,
            "output_path": output_path,
            "input_path": input_path,
            "binary_args": binary_args,
            "target_path": target_path,
        }})
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/del', methods=['POST'])
def del_project():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key":"project_id","val":project_id},
            ]
        )
        user = check_user_before_request(request)
        mongo.delete_one('Project',{"_id": ObjectId(project_id), "user_id": user['_id']})
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/list', methods=['POST'])
def list_project():
    try:
        user = check_user_before_request(request)
        rows = mongo.find("Project", {"user_id": user['_id']}).sort("create_time", -1)
        return build_success_response(list(rows))

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/get', methods=['POST'])
def get_project():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        row = mongo.find_one("Project", {"user_id": user['_id'], "_id": ObjectId(project_id)})
        if row is None:
            raise NetworkException(400, f'project {project_id} 不存在')
        return build_success_response(row)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

def get_case_id(case_obj: dict)->int:
    fname = case_obj['fname']
    return int(fname.replace('\\','/').split('/')[-1].split(',')[0].split(':')[-1])

def get_target_coverage(project_obj: dict, case_obj: dict, container_obj: DockerContainer) -> int:
    project_id = str(project_obj['_id'])
    if project_id not in TargetCoverageMap:
        TargetCoverageMap[project_id] = {}
    case_id = get_case_id(case_obj)
    if case_id not in TargetCoverageMap[project_id]:
        TargetCoverageMap[project_id][case_id] = cal_target_coverage(project_obj, case_obj, container_obj)
    return TargetCoverageMap[project_id][case_id]

@bp.route('/fuzz/add', methods=['POST'])
def fuzzer_add_fuzzer():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        row = mongo.find_one("Project", {"user_id": user['_id'], "_id": ObjectId(project_id)})
        if row is None:
            raise NetworkException(400, f'project {project_id} 不存在')
        container_id = row["container_id"]
        container = mongo.find_one("Container", {"container_id": container_id})
        if container is None:
            raise NetworkException(400, f'container 在数据库中 {container_id} 不存在')
        dm = DockerManager()
        container_obj = dm.get_container(container_id)
        if container_obj is None:
            raise NetworkException(400, f'container 在Docker服务中 {container_id} 不存在')
        if container_obj.get_status() != 'running':
            raise NetworkException(400, f'container {container_id} 未运行')

        fuzzer_id = project_id
        shared_file_path = f"{container['share_dir']}"
        res = mrequests.fuzzer_add(fuzzer_id, shared_file_path)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/resume', methods=['POST'])
def fuzzer_resume():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_resume(project_id)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/pause', methods=['POST'])
def fuzzer_pause():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_pause(project_id)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/stop', methods=['POST'])
def fuzzer_stop():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_stop(project_id)
        mongo.update_one("Project", {"_id": ObjectId(project_id)}, {"$set": {"status": "stop"}})
        TargetCoverageMap[project_id] = {}
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/skip', methods=['POST'])
def fuzzer_skip():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_skip_cur_case(project_id)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/start', methods=['POST'])
def fuzzer_start():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        project_obj = mongo.find_one("Project", {"user_id": user['_id'], "_id": ObjectId(project_id)})
        if project_obj is None:
            raise NetworkException(400, f'project {project_id} 不存在')
        container_id = project_obj["container_id"]
        container = mongo.find_one("Container", {"container_id": container_id})
        if container is None:
            raise NetworkException(400, f'container 在数据库中 {container_id} 不存在')
        dm = DockerManager()
        container_obj = dm.get_container(container_id)
        if container_obj is None:
            raise NetworkException(400, f'container 在Docker服务中 {container_id} 不存在')
        if container_obj.get_status() != 'running':
            raise NetworkException(400, f'container {container_id} 未运行')

        # 到这里已经能保证，项目是存在的，容器是存在的且正在运行
        # 先将afl-fuzz复制到share中
        # shutil.copy(config.FUZZER_EXECUTABLE_PATH, f"{container_obj.share_dir}/afl-fuzz")
        # 下面就可以运行afl-fuzz
        input_path = project_obj['input_path']
        output_path = project_obj['output_path']
        binary_path = project_obj['binary_path']
        binary_cov_path = project_obj['binary_cov_path']
        binary_args = project_obj['binary_args']

        # container_obj.execute_async(f"/bin/bash /root/run_fuzz.sh {input_path} {output_path} {binary_path} {binary_args}")
        mongo.update_one("Project", {"_id": ObjectId(project_id)}, {"$set": {"status": "running"}})

        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/read/cur', methods=['POST'])
def fuzzer_read_cur():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_read_cur(project_id)
        project_obj = mongo.find_one("Project", {"_id": ObjectId(project_id)})
        dm = DockerManager()
        container_obj = dm.get_container(project_obj['container_id'])
        target_coverage_score = get_target_coverage(project_obj, res, container_obj)
        res['target_coverage_score'] = target_coverage_score
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/read/queue', methods=['POST'])
def fuzzer_read_queue():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_read_queue(project_id)
        project_obj = mongo.find_one("Project", {"_id": ObjectId(project_id)})
        dm = DockerManager()
        container_obj = dm.get_container(project_obj['container_id'])
        for i in range(len(res)):
            target_coverage_score = get_target_coverage(project_obj, res[i], container_obj)
            res[i]['target_coverage_score'] = target_coverage_score

        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/read/stat', methods=['POST'])
def fuzzer_read_stat():
    try:
        project_id = request.json.get('project_id')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_read_stat(project_id)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/write/cur', methods=['POST'])
def fuzzer_write_cur():
    try:
        project_id = request.json.get('project_id')
        queue_cur = request.json.get('queue_cur')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
                {"key": "queue_cur", "val": queue_cur},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_write_cur(project_id, queue_cur)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/write/byid', methods=['POST'])
def fuzzer_write_by_id():
    try:
        project_id = request.json.get('project_id')
        modify_queue_entry = request.json.get('modify_queue_entry')
        modify_queue_entry_idx = request.json.get('modify_queue_entry_idx')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
                {"key": "modify_queue_entry", "val": modify_queue_entry},
                {"key": "modify_queue_entry_idx", "val": modify_queue_entry_idx},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_write_by_id(project_id, modify_queue_entry_idx, modify_queue_entry)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/fuzz/fuzzbyid', methods=['POST'])
def fuzzer_fuzz_target_case_by_id():
    try:
        project_id = request.json.get('project_id')
        target_queue_entry_idx = request.json.get('target_queue_entry_idx')
        checkFrontendArgsIsNotNone(
            [
                {"key": "project_id", "val": project_id},
                {"key": "target_queue_entry_idx", "val": target_queue_entry_idx},
            ]
        )
        user = check_user_before_request(request)
        res = mrequests.fuzzer_target_by_id(project_id, target_queue_entry_idx)
        return build_success_response(res)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')
