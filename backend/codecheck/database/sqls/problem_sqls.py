import codecheck.database.connectPool
import os
pooldb = codecheck.database.connectPool.pooldb
from codecheck.database.SQLUtils import *
import json
"""
-----------------------------problem相关---------------------------
"""
def problem_sql_process_problem_json_obj(obj: dict) -> dict:
    file: str = obj['file']
    if file is None:
        raise Exception("problem_sql_process_problem_json_obj传来的obj这个json对象中缺少file属性")
    file = file.replace("\\", '/')
    if file.startswith(".."):
        file = file[2:]
    obj['file'] = file

    if "trace" in obj:
        trace = obj['trace']
        for i in range(len(trace)):
            trace_file = trace[i]['file']
            trace_file = trace_file.replace("\\",'/')
            if trace_file.startswith(".."):
                trace_file = trace_file[2:]
            trace[i]['file'] = trace_file

            trace_snippet_path = trace[i]['snippet_path']
            trace_snippet_path = trace_snippet_path.replace("\\", '/')
            if trace_snippet_path.startswith(".."):
                trace_snippet_path = trace_snippet_path[2:]
            trace[i]['snippet_path'] = trace_snippet_path
        obj['trace'] = trace
    return obj

def problem_sql_insert_problem_json_obj(obj: dict, project_id: str, trans = None):
    obj = problem_sql_process_problem_json_obj(obj)
    filePath = obj['file']
    problemClassName = obj['problem_class']['name']
    severity = obj['problem_class']['severity']
    problemDetail = json.dumps(obj)
    args = (project_id, filePath, problemClassName, severity, problemDetail)
    sql = (' insert into problems(projectId, filePath, problemClassName, severity, problemDetail) '
           ' values(%s, %s, %s, %s, %s) ')
    if trans is not None:
        return trans.execute(sql, args)
    return execute_sql_write(pooldb, sql, args)

def problem_sql_insert_problem_other_obj(value: int, filePath: str, lineNumber: int, project_id: str, trans: SqlTransaction = None):
    problemDetail = json.dumps({'file': filePath, 'line': lineNumber, "value": value})
    args = (project_id, filePath, problemDetail, 'other')
    sql = ' insert into problems(projectId, filePath, problemDetail, problemType) values(%s, %s, %s, %s) '
    if trans is not None:
        return trans.execute(sql, args)
    return execute_sql_write(pooldb, sql, args)

def problem_sql_get_problem_json_obj_by_problem_id(problem_id: str) -> dict:
    sql = ' select * from problems where problemId = %s '
    return execute_sql_query_one(pooldb, sql, problem_id)

def problem_sql_get_problem_json_obj_list_by_project_id(project_id: str) -> List[Dict]:
    sql = ' select * from problems where projectId = %s '
    return execute_sql_query(pooldb, sql, project_id)

def problem_sql_get_problem_json_objs_by_project_id_and_file_path(project_id: str, file_path: str) -> List[Dict]:
    sql = ' select * from problems where projectId = %s and filePath = %s '
    return execute_sql_query(pooldb, sql, (project_id, file_path))

def problem_sql_del_by_problem_id(problem_id: str, trans=None):
    sql = ' delete from problems where problemId= %s '
    if trans is not None:
        return trans.execute(sql, problem_id)
    return execute_sql_write(pooldb, sql, problem_id)

def problem_sql_del_by_project_id(problem_id: str, trans=None):
    sql = ' delete from problems where projectId= %s '
    if trans is not None:
        return trans.execute(sql, problem_id)
    return execute_sql_write(pooldb, sql, problem_id)

def problem_sql_get_problem_cnt_by_project_id(project_id: str):
    return execute_sql_query_one(pooldb, " select count(*) as problemNum from problems where projectId = %s ", project_id)

