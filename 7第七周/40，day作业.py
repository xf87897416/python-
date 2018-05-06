#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/24
import importlib,pymysql


module = "src.commons"
func_name = 'add'
m = importlib.import_module(module)
func = getattr(m,func_name)
func()
###########动态导入模块###########

'''
每张表写一个类
配置文件
数据库操作
    class userinfo():
        def getall(self):
            sql='select * from userinfo'
            return fetchall()
        def get_one_by_user_pwd(self,username,password):
            sql='select * from userinfo where username=%s and password=%s'
            cursor.excute(sql,username,password)
            return cursor.fetchone()
            
'''

PY_settings={
    "host": '192.168.0.10',
    "port": 3306,
    "user": 'root',
    "passwd": '1234',
    "db": 'userinfo',
    "charset": 'utf8'
}
user_info={}


class DbConnection():

    def __init__(self):
        self.__conn_dict = PY_settings
        self.conn = None
        self.cursor = None

    def connect(self, cursor=pymysql.cursors.DictCursor):
        self.conn = pymysql.connect(**self.__conn_dict)
        self.cursor = self.conn.cursor(cursor=cursor)
        return self.cursor

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


class user():
    def __init__(self):
        self.db_conn=DbConnection()

    def add(self,*args,**kwargs):
        cursor=self.db_conn.connect()
        print(args)
        value_list = []
        for k in args:
            value_list.append(k)

        sql='''insert into user(name,password) values(%s,%s)'''

        cursor.execute(sql,args)

        self.db_conn.close()

    def exist(self, username):
        sql = "select 1 from user where name=%s"
        cursor = self.db_conn.connect()
        cursor.execute(sql, [username,])
        result = cursor.fetchone()
        self.db_conn.close()
        return result

while True:
    choise=input("欢迎来到用户中心,1，添加用户")
    choise=int(choise)
    if choise == 1:
        name=input("请输入用户名称").strip()
        password=input("请输入用户密码").strip()
        obj=user()
        result = obj.exist(name)
        if result:
            print("已存在用户")
            continue
        else:
            obj.add(name,password)

    else:
        print("输入错误")


