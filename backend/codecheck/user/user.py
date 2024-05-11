from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from codecheck.emailSender.sendMyEmail import sendRegisterEmail, sendChangePasswdEmail
from codecheck.utils.Tools import *
from codecheck.utils.build_response import *
from codecheck.database.Mongo import Mongo
from codecheck.utils.myExceptions import *
from codecheck.utils.file import *
from codecheck.utils.Logger import logger
import datetime

bp = Blueprint('user', __name__, url_prefix='/user')
mongo = Mongo()

def authorizeEmailPassword(email: str, password: str):
    # user = execute_sql_query_one(pooldb, 'select * from users where email=%s', email)
    user = mongo.find_one("User", {"email": email})
    if user is None:
        raise NetworkException(400, '该邮箱不存在')
    if not check_password_hash(user['password'], password):
        raise NetworkException(400, '密码不正确')
    # 验证正确，返回用户
    return user

def authorizeUserIdPassword(userId: ObjectId, password: str):
    # user = execute_sql_query_one(pooldb, 'select * from users where id=%s', userId)
    user = mongo.find_one("User", {"_id": userId})
    if user is None:
        raise NetworkException(400, '该用户id不存在')
    if not check_password_hash(user['password'], password):
        raise NetworkException(400, '密码不正确')
    # 验证正确，返回用户
    return user


# 用户注册的sql语句, 默认的用户名随机生成，用户用phoneNumber和password注册
def register_user_sql(userName, password, email):
    # execute_sql_write(pooldb, 'insert into users(username,password,email) values(%s,%s,%s)',
    #                   (userName, generate_password_hash(password), email))
    logger.logger.debug({"userName": userName, "password": generate_password_hash(password), "email": email, "crateTime": datetime.datetime.now(), "avatar": [ObjectId('66069dd29aeb444319eb5466')], 'roles': 'common', 'signature': '这个人无话可说~', 'sex': 'female'})
    return mongo.insert_one("User", {"userName": userName, "password": generate_password_hash(password), "email": email, "crateTime": datetime.datetime.now(), "avatar": [ObjectId('66052a3659b8a3a6a13eca88')], 'roles': 'common', 'signature': '这个人无话可说~', 'sex': 'female'})


# 检查email是不是唯一的，如果是则返回True，否则返回False
def checkEmailIsUnique(email: str) -> bool:
    # rows = execute_sql_query(pooldb, 'select * from users where email=%s', (email))
    rows = list(mongo.find("User", {"email": email}))
    if (len(rows) == 0):
        return True
    return False


@bp.route('/register/check', methods=['POST'])
def checkRegisterEmailIsUnique():
    try:
        email = request.json.get('email')
        checkFrontendArgsIsNotNone(
            [{"key":"email","val":email}]
        )
        if checkEmailIsUnique(email):
            return build_success_response({"isExist": False})
        return build_success_response({"isExist": True})

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')


# 检查sessionKey和checkCode是否符合
def checkCheckCode(checkCode: str, sessionKey: str, deltaMinutes=10) -> bool:
    row = mongo.find_one("CheckCodeSessionKey", {"checkCode": checkCode, "sessionKey": sessionKey})

    # 检查该验证码是否存在
    if row is None:
        return False
    # 检查是否超过时限
    createTime = row['createTime']
    now_timestamp = datetime.datetime.now()

    if (now_timestamp - createTime > datetime.timedelta(minutes=deltaMinutes)):
        # 超过时限
        return False
    return True


# 生成一个sessionKey和checkCode
def createCheckCodeAndSession() -> tuple:
    # sessionKey和token生成方式一致，是一串随机的字符串
    sessionKey = buildSessionKey()
    # checkCode则是100000到999999之间的一个数字
    checkCode = str(random.randint(100000, 999999))
    # 将生成的sessionKey和checkCode加入到数据表中
    mongo.insert_one("CheckCodeSessionKey", {"checkCode": checkCode, "sessionKey":sessionKey, "createTime": datetime.datetime.now()})
    # 返回两个数据
    return (checkCode, sessionKey)


def checkCheckCodeSessionKeysAvailability():
    mongo.delete_one("CheckCodeSessionKey", {"createTime": {"$lte": datetime.datetime.now() - datetime.timedelta(minutes=10)}})


@bp.route('/getSessionKeyCheckCode', methods=['POST'])
def getSessionKeyCheckCode():
    try:
        type = request.json.get('type')
        email = request.json.get('email')
        checkFrontendArgsIsNotNone([{"key":"type", "val":type},{"key":"email", "val":email}])
        if type not in ['register', 'changePasswd']:
            raise NetworkException(400, '前端缺少参数type值不正确，type值只能为register, changePasswd')

        if type == 'register':
            userName = request.json.get('userName')
            checkFrontendArgsIsNotNone([{"key": "userName", "val": userName}])
            if not checkEmailIsUnique(email):
                raise NetworkException(400, '该邮箱已被注册')

            checkCode, sessionKey = createCheckCodeAndSession()
            sendRegisterEmail(userName, checkCode, email)
        elif type == 'changePasswd':
            user = mongo.find_one("User", {"email": email})
            if user is None:
                raise NetworkException(400, '该用户不存在')
            userName = user['userName']
            checkCode, sessionKey = createCheckCodeAndSession()
            sendChangePasswdEmail(userName, checkCode, email)
        return build_success_response(data={"sessionKey": sessionKey})

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

@bp.route('/register', methods=['POST'])
def register():
    try:
        userName = request.json.get('userName')
        email = request.json.get('email')
        password = request.json.get('password')
        checkCode = request.json.get('checkCode')
        sessionKey = request.json.get('sessionKey')
        checkFrontendArgsIsNotNone(
            [
                {"key": "userName", "val": userName},
                {"key": "email", "val": email},
                {"key": "password", "val": password},
                {"key": "checkCode", "val": checkCode},
                {"key": "sessionKey", "val": sessionKey}
            ]
        )
        if not checkEmailIsUnique(email):
            raise NetworkException(400, '该邮箱已被注册')

        if not checkCheckCode(checkCode, sessionKey):
            raise NetworkException(400, '验证码错误')

        register_user_sql(userName, password, email)
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')

def change_pwd_sql(email: str, password: str):
    user = mongo.find_one("User", {"email": email})
    if user is None:
        raise NetworkException(400, "此邮箱未注册")
    userId = user['id']
    return mongo.update_one("User", {"_id": userId}, {"$set": {"password": generate_password_hash(password)}})

@bp.route('/updatePwd', methods=['POST'])
def update_pwd():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        checkCode = request.json.get('checkCode')
        sessionKey = request.json.get('sessionKey')
        checkFrontendArgsIsNotNone(
            [
                {"key": "email", "val": email},
                {"key": "password", "val": password},
                {"key": "checkCode", "val": checkCode},
                {"key": "sessionKey", "val": sessionKey}
            ]
        )

        if not checkCheckCode(checkCode, sessionKey):
            raise NetworkException(400, '验证码错误')

        change_pwd_sql(email, password)

        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')


# 收到用户名密码，返回会话对应的token
@bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        checkFrontendArgsIsNotNone(
            [
                {"key": "email", "val": email},
                {"key": "password", "val": password},
            ]
        )
        user = authorizeEmailPassword(email, password)
        token = build_token_and_insert_token_into_db(user['_id'])
        print('[DEBUG] get token, token = ', token)
        return build_success_response({"token": token})

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')


# 退出登录，本质上就是删除与用户建立的对话
@bp.route('/logout', methods=['GET'])
def logout():
    try:
        token = request.headers.get('Authorization')
        if token is None:
            return build_success_response()
        mongo.delete_one({'UserToken': token})
        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(code=500, msg='服务器内部错误')


# data里面应该有user的所有信息
def user_profile_update_user_sql(userId, data):
    return mongo.update_one("User", {'_id': userId}, {"$set": data})


# 获取用户详细信息
@bp.route('/profile/get', methods=['POST'])
def profile_get():
    try:
        user = check_user_before_request(request)
        response = {
            "userInfo": {
                "userId": str(user['_id']),
                "userName": user['userName'],
                "email": user['email'],
                "avatar": user['avatar'],
                "signature": user['signature'],
                "sex": user['sex']
            }
        }
        return build_success_response(response)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response()

@bp.route('/profile/change', methods=['POST'])
def profile_change():
    try:
        token = request.headers.get('Authorization')
        if token is None:
            raise Exception('token不存在，无法修改信息')

        user = check_user_before_request(request)

        data = request.json
        print(f"[DEBUG] {data}")
        user_profile_update_user_sql(user['_id'], data)

        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response()


def user_profile_update_user_pwd(userId: ObjectId, password: str):
    return mongo.update_one("User", {"_id": userId}, {"$set": {"password": generate_password_hash(password)}})


@bp.route('/profile/updatePwd', methods=['POST'])
def updatePwd():
    try:
        data = request.json
        if 'oldPassword' not in data or 'newPassword' not in data:
            raise NetworkException(400, '前端数据错误，不存在oldPassword或newPassword')

        user = check_user_before_request(request)

        res = authorizeUserIdPassword(user['_id'], data['oldPassword'])
        if res is None:
            raise NetworkException(400, '密码不正确')

        user_profile_update_user_pwd(user['_id'], data['newPassword'])

        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(500, "服务器内部错误")




@bp.route('/avatar/list', methods=['POST'])
def avatar_list_api():
    try:
        user = check_user_before_request(request)
        userHistoryFileList = getFileMetaInfoList({
            "userId": user['_id'],
            "fileType": 'avatar'
        })

        processed_userHistoryFileList = []
        for userHistoryFile in userHistoryFileList:
            processed_userHistoryFileList.append(userHistoryFile['fileId'])

        processed_systemAvatarList = []
        systemAvatarList = getFileMetaInfoList({"fileType": 'system-avatar'})
        for systemAvatar in systemAvatarList:
            processed_systemAvatarList.append(systemAvatar['fileId'])

        return build_success_response({
            "userHistoryFileList": processed_userHistoryFileList,
            "systemAvatarList": processed_systemAvatarList
        })

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(500, "服务器内部错误")


@bp.route('/avatar/update', methods=['POST'])
def avatar_update_api():
    try:
        fileId = request.json.get('fileId')
        checkFrontendArgsIsNotNone(
            [
                {"key": "fileId", "val": fileId},
            ]
        )
        user = check_user_before_request(request)
        mongo.update_one("User", {"_id": user["_id"]}, {"$set":{"avatar": fileId}})

        return build_success_response()

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        logger.logger.error(e)
        return build_error_response(500, "服务器内部错误")

# 每过一段时间，都会检查一遍user_token表，看当前时间和visitTime之差，如果二者之差>=3h，说明该用户已经长时间未进行操作了，应该该会话关闭
def checkSessionsAvailability():
    # execute_sql_write(pooldb, 'delete from user_token where timestampdiff(minute,visitTime,CURRENT_TIMESTAMP) >= 1440')
    mongo.delete_many("UserToken", {"visitTime": {"$lte": datetime.datetime.now() - datetime.timedelta(hours=3)}})

