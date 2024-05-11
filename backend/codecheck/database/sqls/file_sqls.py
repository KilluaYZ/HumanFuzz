import codecheck.database.connectPool
import os
pooldb = codecheck.database.connectPool.pooldb
from codecheck.database.SQLUtils import *
BASE_FILE_STORE_DIR = './code_check_shower_server_data'

"""
-----------------------------file相关---------------------------
"""

def file_sqls_get_file_info_by_id(fileId: str) -> dict:
    """
    通过id唯一地找到对应的文件信息
    """
    return execute_sql_query_by_property_unique(pooldb, 'file_info', 'id', fileId)


def file_sqls_get_file_info_by_sha256(sha256_str: str) -> dict:
    """
    通过sha256值唯一地找到对应的文件信息
    """
    return execute_sql_query_by_property_unique(pooldb, 'file_info', 'sha256', sha256_str)


def file_sqls_query_file_info_sql(query_param: dict) -> list:
    sql = f'select * from file_info'
    arg_list = []
    if ('fileName' in query_param
            or 'fileCategory' in query_param
            or 'fileId' in query_param
            or 'sha256' in query_param
            or 'projectId' in query_param
            or 'fileSuffix' in query_param
    ):
        sql = sql + ' where 1=1 '
        if 'fileName' in query_param:
            sql += f' and fileName like %s '
            arg_list.append(f'%{query_param["fileName"]}%')
        if 'fileCategory' in query_param:
            sql += f' and fileCategory=%s '
            arg_list.append(query_param['fileCategory'])
        if 'fileSuffix' in query_param:
            sql += f' and fileSuffix=%s '
            arg_list.append(query_param['fileSuffix'])
        if 'fileId' in query_param:
            sql += f' and id=%s '
            arg_list.append(query_param['fileId'])
        if 'sha256' in query_param:
            sql += f' and sha256=%s '
            arg_list.append(query_param['sha256'])
        if 'projectId' in query_param:
            sql += f' and projectId=%s '
            arg_list.append(query_param['projectId'])

    if 'sortMode' in query_param:
        if query_param['sortMode'] == 'Old':
            sql += ' order by createTime asc '
        else:
            sql += ' order by createTime desc '
    else:
        sql += ' order by createTime desc '

    rows = execute_sql_query(pooldb, sql, tuple(arg_list))
    return rows


def file_sqls_get_project_root_path(projectId: str):
    return os.path.join(BASE_FILE_STORE_DIR, str(projectId))

def file_sqls_get_project_root_src_path(projectId: str):
    return os.path.join(file_sqls_get_project_root_path(str(projectId)), 'src')

def file_sqls_get_project_root_json_path(projectId: str):
    return os.path.join(file_sqls_get_project_root_path(str(projectId)), 'json')

def file_sqls_get_project_root_zip_path(projectId: str):
    return os.path.join(file_sqls_get_project_root_path(str(projectId)), 'zip')

def file_sqls_mkdir_if_not_exist(file_path: str):
    if not os.path.exists(file_path):
        os.mkdir(file_path)

def file_sqls_get_file_path_by_file_info(file_info) -> str:
    """
    根据fileInfo对象，获取该文件的文件路径
    """
    if file_info is None:
        raise Exception("__get_file_path_by_file_info::file_info为None")

    file_path = file_info['filePath']
    file_name = file_info['fileName']
    file_suffix = file_info['fileSuffix']
    file_category = file_info['fileCategory']

    project_id = file_info['projectId']
    print(f'-----------project: {project_id}------------')
    print(f'[DEBUG] file_path = {file_path}')
    print(f'[DEBUG] file_name = {file_name}')
    print(f'[DEBUG] file_suffix = {file_suffix}')
    print(f'[DEBUG] file_category = {file_category}')
    print('---------------------------------------------')
    # if file_category == 'directory':
    #     return f"{file_sqls_get_project_root_path(project_id)}/{file_path}/{file_name}"
    # else:
    #     return f"{file_sqls_get_project_root_path(project_id)}/{file_path}/{file_name}.{file_suffix}"
    return f"{file_sqls_get_project_root_path(project_id)}/{file_path}/{file_name}"
    # return f"{file_path}/{file_name}"


def file_sqls_get_file_path_by_id(fileId: str) -> str:
    """
    根据id获取文件的路径，如果是目录则获取根目录
    """
    file_info = file_sqls_get_file_info_by_id(fileId)

    if file_info is None:
        return None

    return file_sqls_get_file_path_by_file_info(file_info)


def file_sqls_get_dir_file_path_by_project_id(project_id: str) -> str:
    """
    根据项目id获取源码根目录路径
    """
    file_info = file_sqls_get_dir_obj_by_project_id(project_id)
    print(f'[DEBUG] file_info = {file_info}')
    file_path = file_sqls_get_file_path_by_file_info(file_info)
    return file_path


def file_sqls_get_text_file_content_by_id(fileId: str) -> str:
    """
    读取文本数据
    """
    file_path = file_sqls_get_file_path_by_id(fileId)

def file_sqls_get_json_file_obj_by_project_id(project_id: str) -> dict:
    rows = file_sqls_query_file_info_sql({"projectId": project_id, "fileCategory": "text"})
    if rows is None or (rows is not None and len(rows) == 0):
        return None
    return rows[0]

def file_sqls_get_zip_file_obj_by_project_id(project_id: str) -> dict:
    rows = file_sqls_query_file_info_sql({"projectId": project_id, "fileCategory": "zip"})
    if rows is None or (rows is not None and len(rows) == 0):
        return None
    return rows[0]

def file_sqls_get_dir_obj_by_project_id(project_id: str) -> dict:
    rows = file_sqls_query_file_info_sql({"projectId": project_id, "fileCategory": "directory"})
    if rows is None or (rows is not None and len(rows) == 0):
        return None
    return rows[0]

def file_sqls_get_dir_path_by_project_id(project_id: str) -> str:
    file_info = file_sqls_get_dir_obj_by_project_id(project_id)
    if file_info is None:
        return None
    file_path = file_sqls_get_file_path_by_file_info(file_info)
    return file_path

def file_sqls_get_json_file_path_by_project_id(project_id: str) -> str:
    file_info = file_sqls_get_json_file_obj_by_project_id(project_id)
    if file_info is None:
        return None
    file_path = file_sqls_get_file_path_by_file_info(file_info)
    return file_path

def file_sqls_get_zip_file_path_by_project_id(project_id: str) -> str:
    file_info = file_sqls_get_zip_file_obj_by_project_id(project_id)
    # print(f'[DEBUG] 1.1.1')
    if file_info is None:
        return None
    # print(f'[DEBUG] file_info = {file_info}')
    file_path = file_sqls_get_file_path_by_file_info(file_info)
    # print(f'[DEBUG] 1.1.2')
    return file_path

def file_sqls_insert_file(fileName: str,
        filePath: str, fileCategory: str,
        project_id: str,fileSuffix='',trans=None):
    sql = ' insert into file_info(fileName, filePath, fileSuffix, fileCategory, projectId) values(%s, %s, %s, %s, %s) '
    args = (fileName, filePath, fileSuffix, fileCategory, project_id)
    if trans is None:
        return execute_sql_write(pooldb, sql, args)
    else:
        return trans.execute(sql, args)

def file_sqls_del_file_by_file_id(fileId: str, trans=None):
    sql = ' delete from file_info where id = %s '
    if trans is not None:
        return trans.execute(sql, fileId)
    return execute_sql_write(pooldb, sql, fileId)

def file_sqls_del_file_by_project_id(projectId: str, trans=None):
    sql = ' delete from file_info where projectId = %s '
    if trans is not None:
        return trans.execute(sql, projectId)
    return execute_sql_write(pooldb, sql, projectId)

def file_sqls_del_file_by_file_id_with_delete_file(fileId: str, trans=None):
    file_path = file_sqls_get_file_path_by_id(fileId)
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            os.removedirs(file_path)
        elif os.path.isfile(file_path):
            os.remove(file_path)
    return file_sqls_del_file_by_file_id(fileId, trans)


def file_sqls_del_file_by_project_id_with_delete_file(project_id: str, trans=None):
    delete_ids = []
    files_list = file_sqls_query_file_info_sql({"projectId":project_id})
    for file in files_list:
        file_path = file_sqls_get_file_path_by_file_info(file)
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                os.removedirs(file_path)
            elif os.path.isfile(file_path):
                os.remove(file_path)
        del_file_id = file_sqls_del_file_by_project_id(file['id'], trans)
        delete_ids.append(del_file_id)
    return delete_ids


def file_sqls_path_join(path_a: str, path_b: str) -> str:
    """
    /home/sdf/123  /aaa/bbb -> /home/sdf/123/aaa/bbb
    """
    return f'{path_a}/{path_b}'

def file_sqls_get_file_suffix(_file_path: str) -> str:
    """
    /home/sdf/a.txt -> txt
    """
    return (os.path.splitext(_file_path)[-1][1:]).lower()

def file_sqls_get_file_path_without_suffix(_file_path: str) -> str:
    """
    /home/sdf/a.txt.zip -> /home/sdf/a.txt
    """
    return _file_path[:_file_path.rindex('.')]

def file_sqls_get_file_name_without_suffix(_file_path: str) -> str:
    """
    /home/sdf/a.zip -> a
    """
    return file_sqls_get_file_path_without_suffix(file_sqls_get_file_name(_file_path))

def file_sqls_get_file_name(_file_path):
    """
    /home/sdf/a.zip -> a.zip
    """
    return _file_path[_file_path.rindex('/') + 1:]

