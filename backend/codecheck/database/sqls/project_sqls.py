import codecheck.database.connectPool

pooldb = codecheck.database.connectPool.pooldb
from codecheck.database.SQLUtils import *
from codecheck.database.sqls.file_sqls import *


"""
-----------------------------project相关---------------------------
"""
def project_sqls_get_project_by_project_id(project_id: str) -> dict:
    return execute_sql_query_by_property_unique(pooldb, 'projects', 'id', project_id)

def project_sqls_get_user_by_project_id(project_id: str) -> dict:
    return execute_sql_query_one(pooldb,
    ' select users.id as id, userName, email, createTime from users, projects '
    ' where projects.id = %s '
    ' and users.id=projects.id ',
    project_id)

def project_sqls_check_if_project_is_public_by_project_id(project_id: str) -> bool:
    project = project_sqls_get_project_by_project_id(project_id)
    if project is None:
        return False
    if not project['isPublic']:
        return False
    return True

def project_sqls_query_project_sql(query_param: dict) -> list:
    sql_select = (' select distinct projects.id as projectId, '
                  ' projects.name as projectName, '
                  ' projects.isPublic as isPublic, '
                  ' projects.projectType as projectType, '
                  ' projects.userId as userId, '
                  ' users.userName as userName, '
                  ' projects.createTime as createTime '
                  'from projects, users where projects.userId = users.id ')

    args_str_list = []
    args_val_list = []

    if 'id' in query_param:
        args_str_list.append(f' and projects.id = %s ')
        args_val_list.append(query_param['id'])
    if 'projectType' in query_param:
        args_str_list.append(f' and projects.projectType = %s ')
        args_val_list.append(query_param['projectType'])
    if 'exact_name' in query_param:
        args_str_list.append(f' and projects.name = %s ')
        args_val_list.append(query_param['exact_name'])
    if 'fuzz_name' in query_param:
        args_str_list.append(f' and name like %s ')
        args_val_list.append(f'%{query_param["fuzz_name"]}%')
    if 'isPublic' in query_param:
        args_str_list.append(f' and projects.isPublic = %s ')
        args_val_list.append(query_param['isPublic'])
    if 'userId' in query_param:
        args_str_list.append(f' and projects.userId = %s ')
        args_val_list.append(query_param['userId'])


    sql = sql_select

    for item in args_str_list:
        sql += item

    sql += ' order by projects.createTime desc '

    rows = execute_sql_query(pooldb, sql, tuple(args_val_list))
    return rows

def project_sqls_insert(project_name: str, is_public: str, project_type: str, user_id: str, trans=None):
    sql = ' insert into projects(name, isPublic, projectType, userId) values(%s, %s, %s, %s) '
    args = (project_name, is_public, project_type, user_id)
    if trans is not None:
        return trans.execute(sql, args)
    return execute_sql_write(pooldb, sql, args)

def project_sqls_check_if_project_belong_to_user_id(projectId: str, userId: str) -> bool:
    project_obj = project_sqls_get_project_by_project_id(projectId)
    if project_obj['userId'] == userId:
        return True
    return False

def project_sqls_del_by_project_id(project_id: str, trans: SqlTransaction):
    # 先删除文件
    file_sqls_del_file_by_project_id(project_id, trans)

    # tasks和problems不用删除，因为在数据库中已经设置了级联删除
    return trans.execute(' delete from projects where id = %s ', project_id)
