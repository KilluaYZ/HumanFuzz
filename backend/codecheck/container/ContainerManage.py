from flask import Blueprint, request, send_file, Request
from bson import ObjectId
from codecheck.utils.Tools import *
from flask import Blueprint, request
from codecheck.utils.build_response import *
from codecheck.database.Mongo import Mongo
from codecheck.utils.myExceptions import *
from codecheck.utils.file import *
from codecheck.utils.Logger import logger
import datetime
from codecheck.container.DockerManager import DockerManager, DockerContainer

bp = Blueprint('container', __name__, url_prefix='/container')
mongo = Mongo()

@bp.route('/run', methods=['POST'])
def run_container():
    try:
        name = request.json.get('name')
        checkFrontendArgsIsNotNone(
            [{"key":"name","val":name}]
        )
        user = check_user_before_request(request)
        dm = DockerManager()
        dc = dm.run_container(name, user['_id'])
        return build_success_response(dc.to_dict())

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')


@bp.route('/remove', methods=['POST'])
def remove_container():
    try:
        container_id = request.json.get('container_id')
        checkFrontendArgsIsNotNone(
            [{"key":"container_id","val":container_id}]
        )
        user = check_user_before_request(request)
        dm = DockerManager()
        dc = dm.get_container(container_id)
        dc.remove()
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/list', methods=['POST'])
def list_container():
    try:
        user = check_user_before_request(request)
        dm = DockerManager()
        return build_success_response(dm.list_container(user['_id']))

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/start', methods=['POST'])
def start_container():
    try:
        container_id = request.json.get('container_id')
        checkFrontendArgsIsNotNone(
            [{"key":"container_id","val":container_id}]
        )
        user = check_user_before_request(request)
        dm = DockerManager()
        dc = dm.get_container(container_id)
        dc.start()
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/stop', methods=['POST'])
def stop_container():
    try:
        container_id = request.json.get('container_id')
        checkFrontendArgsIsNotNone(
            [{"key":"container_id","val":container_id}]
        )
        user = check_user_before_request(request)
        dm = DockerManager()
        dc = dm.get_container(container_id)
        dc.stop()
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/get', methods=['POST'])
def get_container():
    try:
        container_id = request.json.get('container_id')
        checkFrontendArgsIsNotNone(
            [{"key":"container_id","val":container_id}]
        )
        user = check_user_before_request(request)
        row = mongo.find_one("Container", {"container_id": container_id, "user_id": user['_id']})
        if row is None:
            row = {}
        return build_success_response(row)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')