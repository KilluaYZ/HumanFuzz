# clriocahxwmsdcfg
# IMAP/SMTP 设置方法
# 用户名/帐户： 你的QQ邮箱完整的地址
# 密码： 生成的授权码
# 电子邮件地址： 你的QQ邮箱的完整邮件地址
# 接收邮件服务器： imap.qq.com，使用SSL，端口号993
# 发送邮件服务器： smtp.qq.com，使用SSL，端口号465或587

import smtplib
from email.mime.text import MIMEText #邮箱正文
from email.mime.multipart import MIMEMultipart #邮箱主体
from email.header import Header #邮箱头、标题、收件人
from codecheck.emailSender.emailHtmls import getRegisterEmail, getChangePasswdEmail
mail_host = 'smtp.qq.com'
mail_user = '2959243019@qq.com'
mail_pass = 'clriocahxwmsdcfg'
sender = '2959243019@qq.com'
title = 'CodeCheck令牌验证'
def sendEmail(mail_title: str, mail_content: str, mail_receiver: str, mail_type='html'):
    msg = MIMEMultipart()
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['From'] = sender
    if mail_type == 'html':
        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    elif mail_type == 'plain':
        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, mail_receiver, msg.as_string())
        smtpObj.quit()
        print(f'向{mail_user}发送邮件成功')
    except smtplib.SMTPException as e:
        print(f'Error: 无法向{mail_user}发送邮件')
        print(e)

def sendRegisterEmail(userName: str, checkCode: str, mail_receiver: str):
    sendEmail(title, getRegisterEmail(userName, checkCode), mail_receiver)

def sendChangePasswdEmail(userName: str, checkCode: str, mail_receiver: str):
    sendEmail(title, getChangePasswdEmail(userName, checkCode), mail_receiver)
#
# sendRegisterEmail('ziyang','57736','2020201694@ruc.edu.cn')
# sendChangePasswdEmail('ziyang','57736','2020201694@ruc.edu.cn')
