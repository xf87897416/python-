#!/usr/bin/env python
# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(email_list, content, subject="抽屉新热榜-用户注册"):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["抽屉新热榜",'xf87897416@139.com'])
    msg['Subject'] = subject
    # SMTP服务
    server = smtplib.SMTP("smtp.139.com", 25)
    server.login("xf87897416@139.com", "xf87897416")
    server.sendmail('xf87897416@139.com', email_list, msg.as_string())
    server.quit()


# email(['xiaohu@live.com','jinxin@live.com'], 'xiaohuzuishuai')
