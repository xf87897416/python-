#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/10

import json,os,sys
import logging
#
# def data_dump(name):
#     info = {'name': 'xf', 'passwd': 'abc', 'id': 22, 'lock': 0,'balance':10000}
#     # info = {'name': 'hfy', 'passwd': '123', 'id': 20, 'lock': 0,'balance':7000}
#     file_name = "%s.json" % name
#     f = open(file_name, 'w')
#     data = json.dump(info, f)
#     f.close()

def data_load(name):
    file_name = "%s.json" % name
    f=open(file_name,'r')
    data=json.load(f)
    return data

# data_dump('xf')

def logger():
    file_name = "access.log"
    logger = logging.getLogger()
    fn=logging.FileHandler(file_name)
    ch=logging.StreamHandler()
    formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    fn.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fn)
    # logger.addHandler(ch)
    return logger

def logger2(name):
    file_name = "%s.log"% name
    logger2 = logging.getLogger()
    fn=logging.FileHandler(file_name)
    ch=logging.StreamHandler()
    formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger2.setLevel(logging.INFO)
    fn.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger2.addHandler(fn)
    # logger.addHandler(ch)
    return logger2

def account_info(access_data,log_obj):  #{'name': 'hfy', 'passwd': '123', 'id': 20, 'lock': 0}
      print('''
      name:%s
      id:%s
      balance:%s
      '''%(access_data['name'],access_data['id'],access_data['balance']))

def trans(access_data):
    file_name = "%s.json" % access_data['name']
    f = open(file_name, 'w')
    data = json.dump(access_data, f)
    f.close()

def repay(access_data,log_obj):
    flag=True
    while flag:
        inp=input("请输入存款金额（quit：退出）：").strip()
        if inp.isdigit() and int(inp)>0:
            print("已存%s"%int(inp))
            access_data['balance']+=int(inp)
            trans(access_data)
            # file_name = "%s.json" % access_data['name']
            # f=open(file_name,'w')
            # data = json.dump(access_data, f)
            # f.close()
            log_obj.info("%s已存款%s" % (access_data['name'], str(inp)))
            # log_obj.info("nihao")
            return access_data
        elif inp=='quit':
            flag=False
        else:
            print("输入错误请重新输入")

def withdraw(access_data,log_obj):
    flag = True
    while flag:
        inp = input("请输入取款金额（quit：退出）：").strip()
        if inp.isdigit()  and access_data['balance']-int(inp)>0:
            print("已取款%s" % int(inp))
            log_obj.info("%s已取款%s" % (access_data['name'], int(inp)))
            access_data['balance'] -= int(inp)
            trans(access_data)
            # file_name = "%s.json" % access_data['name']
            # f = open(file_name, 'w')
            # data = json.dump(access_data, f)
            # f.close()
            return access_data
        elif inp == 'quit':
            flag = False
        else:
            print("输入错误请重新输入")

def transfer(access_data,log_obj):
    flag=True
    while flag:
        t_name=input("请输入转账账户,退出：quit").strip()
        if user_exist(t_name) and t_name != access_data['name']:
            money=input("请输入转账金额").strip()
            if money.isdigit() and int(money)<=access_data['balance']:
                money = int(money)
                access_data['balance']-=money
                t_data=data_load(t_name)
                t_data['balance']+=money
                trans(t_data)
                # file_name = "%s.json" % t_name
                # f = open(file_name, 'w')
                # data = json.dump(t_data, f)
                # f.close()
                log_obj.info("%s转给%s%s钱" % (access_data['name'], t_data['name'],money))
                flag=False
        elif t_name == 'quit':
            break
        else:
            print("用户不存在")


def paycheck(access_data,log_obj):
    show_info=access_data['name']
    f=open('%s.log'%show_info)
    log=f.read()
    print(log)

def logout(access_data,log_obj):
    log_obj.info("用户%s退出"%access_data['name'])
    sys.exit("谢谢使用")

def login_start(access_data,log_obj):
    while True:
        print("欢迎%s".center(50,'-')%access_data['name'])
        print('''
        1 .账户信息
        2 .存款
        3 .取款
        4 .转账
        5 .账单
        6 .退出
        ''')
        chose=input("请输入数字：").strip()
        menu_dic ={
            "1": account_info,
            "2": repay,
            "3": withdraw,
            "4": transfer,
            "5": paycheck,
            "6": logout
        }
        if chose in menu_dic:
            menu_dic[chose](access_data,log_obj)

def user_exist(name):
    file_name = '%s.json' % name
    if os.path.isfile(file_name):
        return 'ok'
    else:
        print("user not exist")

def login(log_obj):
    retry=0
    while retry<3:
        name = input("your name:").strip()
        passwd = input("your passwd:").strip()
        file_name='%s.json'% name
        if os.path.isfile(file_name):
            data=data_load(name)
            if data['name']==name and data['passwd']==passwd:
                print('user:%s login success'% name)
                log_obj.info('user:%s login success'% name)
                access_data=data
                return access_data
            else:
                print("passwd wrong!")
                log_obj.error("%s login failed"% name)
                retry += 1
        else:
            print('no user!')
            log_obj.warning("login failed" )
            retry+=1
    else:
        print("尝试次数过多！")
        log_obj.warning("尝试次数过多！")
access_log=logger()
access_data=login(access_log)


if access_data:
    acc_name=access_data['name']
    access2_log = logger2(acc_name)
    print("验证成功")
    login_start(access_data,access2_log)
else:
    print("没有验证")









