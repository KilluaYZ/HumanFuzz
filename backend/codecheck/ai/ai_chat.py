from flask import Blueprint, request
import codecheck.database.connectPool
from codecheck.utils.build_response import *
from codecheck.utils.auth import *
from codecheck.database.SQLUtils import *
import codecheck.utils.check as check
from codecheck.utils.SourceCodeReader import SourceCodeReader
from codecheck.database.sqls.project_sqls import project_sqls_check_if_project_is_public_by_project_id, project_sqls_get_project_by_project_id
from codecheck.database.sqls.file_sqls import *
from codecheck.database.sqls.problem_sqls import *
from codecheck.database.sqls.trace_sqls import *
from codecheck.ai.WenXinAi import WenXinChat

import base64
bp = Blueprint('AiChat', __name__, url_prefix='/ai')
pooldb = codecheck.database.connectPool.pooldb

@bp.route("/chat", methods=["POST"])
def ai_chat():
    try:
        chat_history = request.json.get("chatHistory")
        check.checkFrontendArgsIsNotNone([
            {"key": "chatHistory", "val": chat_history},
        ])

        new_chat_history, reply = WenXinChat(chat_history)
        response = {
            "reply": reply
        }

        return build_success_response(data=response)

    except NetworkException as e:
        return build_error_response(code=e.code, msg=e.msg)
    except Exception as e:
        check.printException(e)
        return build_error_response(code=500, msg='服务器内部错误')


