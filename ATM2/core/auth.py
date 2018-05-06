#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/4

print("BB")
import os
import json
import time

from core import db_handle
from conf import settings
from core import account

def access_auth(account, password, log_obj):
    db_path = db_handle.handle(settings.DATABASE)
    print(db_path)
    account_file = "%s/%s.json" % (db_path, account)  # 用户文件
    if os.path.isfile(account_file):
        with open(account_file, "r", encoding="utf-8") as f:
            account_data = json.load(f)
            print(account_data)
            if account_data["password"] == password:
                expire_time = time.mktime(time.strptime(account_data["expire_date"], "%Y-%m-%d"))
                print(expire_time)
                print(time.strptime(account_data["expire_date"], "%Y-%m-%d"))
                if time.time() > expire_time:
                    log_obj.error("Account [%s] had expired,Please contract the bank" % account)
                    print("\033[31;1mAccount [%s] had expired,Please contract the bank" % account)
                else:
                    print("return")
                    log_obj.info("Account [%s] logging success" % account)
                    return account_data
            else:
                log_obj.error("Account or Passworddoes not correct!")
                print("\033[31;1mAccount or Passworddoes not correct!\033[0m")
    else:
        log_obj.error("Account [%s] does not exist!" % account)
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)


def access_login(user_data, log_obj):
    retry = 0
    while not user_data["is_authenticated"] and retry < 3:
        account = input("Account:").strip()
        password = input("Password:").strip()
        #用户帐号密码正确且信用卡未超期，返回用户数据的字典
        user_auth_data = access_auth(account, password, log_obj)
        if user_auth_data:
            user_data["is_authenticated"] = True   #用户认证为True
            user_data["id"] = account       #用户帐号ID为帐号名
            print("welcome")
            return user_auth_data
        retry += 1      #登陆和信用卡认证出错，则次数加1
    else:        #若次数超过三次，打印相关信息并退出
        print("Account [%s] try logging too many times..." % account)
        log_obj.error("Account [%s] try logging too many times..." % account)
        exit()







