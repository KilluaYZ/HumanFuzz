from gridfs import *
from codecheck.database.Mongo import Mongo
from codecheck.utils.Logger import logger
from datetime import datetime
from bson import ObjectId
import hashlib
import mimetypes
import base64

mongofs = Mongo(database="CodeCheckFS")
mongo = Mongo()

def uploadFileBinaryToDB(content: bytes) -> ObjectId:
    try:
        db = mongofs.get_db()
        fs = GridFS(db, collection='File')

        current_content_md5 = hashlib.md5(content).hexdigest()
        row = fs.find_one({'md5': current_content_md5})
        if row is not None and row.md5 == current_content_md5:
            return row._id

        return ObjectId(str(fs.put(content, md5=current_content_md5)))

    except Exception as e:
        logger.logger.error(e)
        raise e


def getFileBinaryFromDB(query: dict) -> bytes:
    try:
        db = mongofs.get_db()
        fs = GridFS(db, collection="File")
        grid_out = fs.find_one(query)
        if grid_out is None:
            return None

        return grid_out.read()

    except Exception as e:
        logger.logger.error(e)
        raise e

def getFileBase64FromDB(query: dict) -> str:
    try:
        content = getFileBinaryFromDB(query)
        return base64.b64encode(content).decode('utf-8')
    except Exception as e:
        raise e

def uploadFile(content: bytes, fileName: str, userId: ObjectId, isPrivate: bool = False, fileType: str = 'default') -> ObjectId:
    session = Mongo().get_session()
    session.start_transaction()
    try:
        fileId = uploadFileBinaryToDB(content)
        _id = mongo.insert_one("File", {
            "fileId": fileId,
            "fileName": fileName,
            "mimeType": mimetypes.guess_type(fileName)[0],
            "createTime": datetime.now(),
            "userId": userId,
            "isPrivate": isPrivate,
            "fileType": fileType
        })
        session.commit_transaction()
        return _id
    except Exception as e:
        logger.logger.error(e)
        session.abort_transaction()


def getFile(query:dict, mode='base64') -> dict:
    fileObj = mongo.find_one("File", query)
    if fileObj is None:
        return None
    if mode == 'binary':
        content = getFileBinaryFromDB({"_id": fileObj['fileId']})
    else:
        content = getFileBase64FromDB({"_id": fileObj['fileId']})
    fileObj["fileContent"] = content
    return fileObj

def getFileList(query:dict, mode='base64') -> list:
    fileObjList = list(mongo.find("File", query))
    if fileObjList is None:
        return None
    for i in range(len(fileObjList)):
        if mode == 'binary':
            fileObjList[i]["fileContent"] = getFileBinaryFromDB({"_id": fileObjList[i]['fileId']})
        else:
            fileObjList[i]["fileContent"] = getFileBase64FromDB({"_id": fileObjList[i]['fileId']})
    return fileObjList


def getFileMetaInfoList(query: dict) -> list:
    return list(mongo.find("File", query))

