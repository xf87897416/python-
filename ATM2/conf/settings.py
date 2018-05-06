#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/3
import os,sys,logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


LOGIN_LEVEL=logging.INFO #(默认日志级别)


LOGIN_TYPE={
    'access':'access.log'
}

DATABASE={
    'db_tool':'file_storage',
    'name':'accounts',
    'path':'%s\db'%BASE_DIR
}
TRANSACTION_TYPE = {
    "repay":{"action":"plus", "interest":0},  #存款
    "withdraw":{"action":"minus", "interest": 0.05},  #取款(提现)
    "transfer_out":{"action":"minus", "interest": 0.05}  #转帐(出)
}








