import codecheck.database.connectPool
import os
pooldb = codecheck.database.connectPool.pooldb
from codecheck.database.SQLUtils import *
BASE_FILE_STORE_DIR = './code_check_shower_server_data'

"""
-----------------------------trace相关---------------------------
"""

def trace_sqls_get_trace_by_trace_id(trace_id: str) -> dict:
    return execute_sql_query_one(pooldb, " select * from traces where traceId = %s ", trace_id)

def trace_sqls_get_trace_by_project_id(project_id: str) -> List[Dict]:
    return execute_sql_query(pooldb, " select * from traces where projectId = %s ", project_id)

def trace_sqls_get_trace_by_problem_id(problem_id: str) -> List[Dict]:
    return execute_sql_query(pooldb, " select * from traces where problemId = %s ", problem_id)

def trace_sqls_get_trace_by_project_id_and_file_path(project_id: str, file_path: str) -> List[Dict]:
    return execute_sql_query(pooldb, ' select * from traces where projectId = %s and file = %s ', (project_id, file_path))

def trace_sqls_insert_trace(line: int, file: str, kind: str, project_id: int, problem_id: int, desc = "", trans = None):
    sql = " insert into traces(line, file, kind, projectId, problemId, `desc`) values(%s, %s, %s, %s, %s, %s) "
    args = (str(line), file, kind, str(project_id), str(problem_id), desc)
    if trans is not None:
        return trans.execute(sql, args)
    return execute_sql_write(pooldb, sql, args)

def trace_sqls_insert_trace_by_trace_obj(trace_obj: dict, project_id: int, problem_id: int, trans=None):
    line = trace_obj['line']
    file = trace_obj['file']
    kind = trace_obj['kind']
    desc = trace_obj['desc']
    if line is None or file is None or kind is None:
        raise Exception("trace_sqls_insert::缺少line或file或kind重要参数")
    return trace_sqls_insert_trace(line, file, kind, project_id, problem_id, desc, trans)
