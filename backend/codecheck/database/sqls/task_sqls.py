import codecheck.database.connectPool

pooldb = codecheck.database.connectPool.pooldb
from codecheck.database.SQLUtils import *

"""
-----------------------------task相关---------------------------
"""
def task_sqls_get_tasks_list_by_project_id(project_id: str) -> List[Dict]:
    return execute_sql_query(pooldb, ' select * from tasks where projectId = %s order by createTime desc ', project_id)

def task_sqls_update_task_status(task_id: str, status: str, trans = None):
    if status not in ['created', 'unzipping', 'analysing', 'pulling', 'waiting', 'success', 'error']:
        raise Exception(f"sqls::sqls_update_task_status, 参数status={status}不合法")
    if trans is None:
        return execute_sql_write(pooldb, ' update tasks set status = %s where taskId = %s', (status, task_id))
    else:
        return trans.execute(' update tasks set status = %s where taskId = %s', (status, task_id))

def task_sqls_init_task(project_id: str):
    return execute_sql_write(pooldb, ' insert into tasks(projectId) values(%s) ', project_id)


def task_sqls_del_by_task_id(task_id: str, trans=None):
    sql = ' delete from tasks where taskId= %s '
    if trans is not None:
        return trans.execute(sql, task_id)
    return execute_sql_write(pooldb, sql, task_id)

def task_sqls_del_by_project_id(project_id: str, trans=None):
    sql = ' delete from tasks where projectId= %s '
    if trans is not None:
        return trans.execute(sql, project_id)
