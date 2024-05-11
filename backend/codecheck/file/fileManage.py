from flask import Blueprint, request, send_file, Request
from codecheck.utils.build_response import *
from codecheck.utils.Logger import logger
from bson import ObjectId
from codecheck.utils.Tools import *
from codecheck.utils.file import *
import io
import base64

bp = Blueprint('file', __name__, url_prefix='/file')
mongo = Mongo()

@bp.route('/getByFileId', methods=['GET'])
def getFileByIdAPI():
    try:
        fileId = request.args.get('fileId')
        checkFrontendArgsIsNotNone(
            [{'key':"fileId", "val": fileId}]
        )
        fileObj = getFile({"fileId": ObjectId(fileId)})
        if fileObj is None:
            raise NetworkException(code=404, msg=f"fileId为{fileId}的文件不存在")

        if fileObj['isPrivate']:
            # 检查该图片是否属于该用户
            user = check_user_before_request(request)
            if user['_id'] != fileObj['userId']:
                # 如果不属于，则查看该用户是否是admin
                admin_user = check_user_before_request(request, 'admin')

        return send_file(io.BytesIO(fileObj['fileContent']), mimetype=fileObj['mimeType'])

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/getFileObjByFileId', methods=['POST'])
def getFileObjByIdAPI():
    try:
        fileId = request.json.get('fileId')
        checkFrontendArgsIsNotNone(
            [{'key':"fileId", "val": fileId}]
        )
        fileObj = getFile({"fileId": ObjectId(fileId)})
        if fileObj is None:
            raise NetworkException(code=404, msg=f"Id为{fileId}的资源不存在")

        if fileObj['isPrivate']:
            # 检查该图片是否属于该用户
            user = check_user_before_request(request)
            if user['_id'] != fileObj['userId']:
                # 如果不属于，则查看该用户是否是admin
                admin_user = check_user_before_request(request, 'admin')

        return build_success_response(fileObj)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        # logger.logger.error(e)
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')


def fileterFileListByPrivilege(fileList: list, request: Request):
    res = []

    for fileObj in fileList:
        if fileObj['isPrivate']:
            # 检查该图片是否属于该用户
            user = check_user_before_request(request, raise_exc=False)
            if user is None:
                continue

            if user['_id'] != fileObj['userId']:
                # 如果不属于，则查看该用户是否是admin
                admin_user = check_user_before_request(request, raise_exc=False, roles='admin')
                if admin_user is None:
                    continue
            res.append(fileObj)
        else:
            res.append(fileObj)

    return res



@bp.route('/getFileObjListByQuery', methods=['POST'])
def getFileObjListByQueryAPI():
    try:
        query = request.json
        if "fileId" in query:
            query['fileId'] = ObjectId(query['fileId'])

        if "userId" in query:
            query['userId'] = ObjectId(query['userId'])

        fileList = getFileList(query)

        if fileList is None:
            raise NetworkException(code=404, msg=f"资源不存在")

        fileList = fileterFileListByPrivilege(fileList, request)

        for i in range(len(fileList)):
            fileList[i]['fileContent'] = base64.b64encode(fileList[i]['fileContent']).decode('utf-8')

        return build_success_response(fileList)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        # logger.logger.error(e)
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/getFileMetaInfoListByQuery', methods=['POST'])
def getFileMetaInfoListByQueryAPI():
    try:
        query = request.json
        if "fileId" in query:
            query['fileId'] = ObjectId(query['fileId'])

        if "userId" in query:
            query['userId'] = ObjectId(query['userId'])

        fileList = getFileMetaInfoList(query)

        if fileList is None:
            raise NetworkException(code=404, msg=f"资源不存在")

        fileList = fileterFileListByPrivilege(fileList, request)

        return build_success_response(fileList)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        # logger.logger.error(e)
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/uploadFile', methods=['POST'])
def uploadFileAPI():
    try:
        fileName = request.json.get('fileName')
        # fileContent 是base64格式
        fileContent = request.json.get('fileContent')
        isPrivate = request.json.get('isPrivate')
        fileType = request.json.get('fileType')

        checkFrontendArgsIsNotNone(
            [
                {'key':"fileName", "val": fileName},
                {'key':"fileContent", "val":fileContent},
                {'key':"isPrivate", "val": isPrivate},
                {'key': "fileType", "val": fileType}
            ]
        )

        user = check_user_before_request(request)
        # 解码
        decoded_content = base64.b64decode(fileContent)
        fileId = uploadFile(decoded_content, fileName, user['_id'], isPrivate, fileType)

        return build_success_response(data={'fileId':str(fileId)})

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')