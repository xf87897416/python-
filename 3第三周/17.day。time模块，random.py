#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/10/28

import time
# import datetime
# print(help(time))
# print(time.time()) #1509201892.1248195 时间戳
#print(time.clock())  #计算cpu执行时间
#print(time.gmtime()) 结构化时间，英国标准
# print(time.localtime()) #本地时间
# timez=time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S',timez))  #字符串时间*****
# print(time.strptime('2017-10-28 23:17:27','%Y-%m-%d %H:%M:%S'))
# a=time.strptime('2017-10-28 23:17:27','%Y-%m-%d %H:%M:%S')
# print(a.tm_year)
#转换为元组形式的时间

# print(time.ctime()) #Sat Oct 28 23:23:24 2017

# print(time.mktime(time.localtime()))  #将结构化数据转时间戳

# print(datetime.datetime.now())

import random
import string
# print(random.random())
# print(random.randint(1,8)) #包括1,8
# print(random.choice([1,2,3,67,98,[33,44。day]]))
# print(random.sample(['123',4,[1,2]],1)) #多个序列选几个
# print(random.randrange(1,3))


# num=""
# for i in range(5):
#     a = random.choice('1234567890abcdefghijklmnopqrstuvwxyz')
#     num+=a
# print(num)


# import random
# import string
# c="".join(random.sample(string.ascii_letters + string.digits,8))
# print(c)

##################################
import subprocess   #处理命令

while 1:
    inp = input('>>>:')
    res = subprocess.call(inp,shell=True)
    if res == 0:
        obj = subprocess.Popen(inp, shell=True, stdout=subprocess.PIPE)
        msg = obj.stdout.read()
        msg = str(msg, 'gbk')
    else:
        print("错误命令")

















