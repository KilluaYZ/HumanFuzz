import json
# from dbtest.showdata10 import db # 引入其他蓝图
import re
from typing import Dict, Tuple, Optional

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, url_for, g
from flask_cors import CORS  # 跨域
import config
# app
from codecheck.user import user
# from codecheck.ai import ai_chat
# from codecheck.monitor.monitor import monitor
# from codecheck.manage import project_manage
from codecheck.file import fileManage
from codecheck.container import ContainerManage
from codecheck.project import projectManage
# 创建flask app
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # app.json_encoder = UpdatedJsonProvider(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # 在应用中注册init_db
    # @app.cli.command('init-db')
    # def init_db_command():
    #     """删除现有的所有数据，并新建关系表"""
    #     init_db()

    app.config.from_object(config)

    app.register_blueprint(user.bp)
    app.register_blueprint(fileManage.bp)
    app.register_blueprint(ContainerManage.bp)
    app.register_blueprint(projectManage.bp)

    # 配置定时任务
    # 该任务作用是每个一个小时检查一次user_token表，将超过1天未活动的token删掉（随便定的，后面改
    from codecheck.user.user import checkSessionsAvailability
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=checkSessionsAvailability,
                      id='checkSessionsAvailability',
                      trigger='interval',
                      seconds=3600,
                      replace_existing=True
                      )
    # 该任务作用是每一个小时检查一次check_code_session_key表，删除超过10分钟的过期令牌
    from codecheck.user.user import checkCheckCodeSessionKeysAvailability
    scheduler.add_job(func=checkCheckCodeSessionKeysAvailability,
                      id='checkCheckCodeSessionKeysAvailability',
                      trigger='interval',
                      seconds=3600,
                      replace_existing=True
                      )
    # 启动任务列表
    scheduler.start()
    return app

app = create_app()
