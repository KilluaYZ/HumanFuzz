import requests
import json
import config

def request_to_string(url, headers, method: str, data={}, param={}):
    return f"""request请求参数如下:
url: {url}
headers: {headers}
method: {method}
data: {data}
param: {param}
    """

def post(url: str, data: dict) -> dict:
    headers = {
        "Content-Type": "application/json",
    }
    try:
        res = requests.post(url, data=json.dumps(data), headers=headers).json()
        if(res['statusCode'] != 200):
            raise Exception(res['message'])
        return res
    except Exception as e:
        raise Exception(f"请求失败！{request_to_string(url, headers, method='POST', data=data)}\n错误信息:{e}")


FUZZER_SERVER_HOST = config.FUZZER_SERVER_HOST
def fuzzer_add(fuzzer_id: str, shared_file_path: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
        "shared_file_path": shared_file_path
    }
    return post(f"{FUZZER_SERVER_HOST}/add", data=data)

def fuzzer_pause(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    return post(f"{FUZZER_SERVER_HOST}/pause", data=data)

def fuzzer_resume(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    return post(f"{FUZZER_SERVER_HOST}/resume", data=data)

def fuzzer_stop(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    return post(f"{FUZZER_SERVER_HOST}/stop", data=data)

def fuzzer_skip_cur_case(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    return post(f"{FUZZER_SERVER_HOST}/skip", data=data)

def fuzzer_read_all(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    res = post(f"{FUZZER_SERVER_HOST}/read/all", data=data)
    res_json = json.loads(res['message'])
    return res_json

def fuzzer_read_queue(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    res = post(f"{FUZZER_SERVER_HOST}/read/queue", data=data)
    res_json = json.loads(res['message'])
    return res_json

def fuzzer_read_cur(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    res = post(f"{FUZZER_SERVER_HOST}/read/cur", data=data)
    res_json = json.loads(res['message'])
    return res_json

def fuzzer_read_stat(fuzzer_id: str) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
    }
    res = post(f"{FUZZER_SERVER_HOST}/read/stat", data=data)
    res_json = json.loads(res['message'])
    return res_json

def fuzzer_write_cur(fuzzer_id: str, queue_cur: dict) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
        "queue_cur": queue_cur
    }
    return post(f"{FUZZER_SERVER_HOST}/write/cur", data=data)

def fuzzer_write_by_id(fuzzer_id: str, modify_queue_entry_idx: int, modify_queue_entry: dict) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
        "modify_queue_entry": modify_queue_entry,
        "modify_queue_entry_idx": modify_queue_entry_idx
    }
    return post(f"{FUZZER_SERVER_HOST}/write/byid", data=data)

def fuzzer_target_by_id(fuzzer_id: str, target_queue_entry_idx: int) -> dict:
    data = {
        "fuzzer_id": fuzzer_id,
        "target_queue_entry_idx": target_queue_entry_idx
    }
    return post(f"{FUZZER_SERVER_HOST}/fuzzbyid", data=data)
