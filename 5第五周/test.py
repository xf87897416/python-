#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/8

import socket,os,subprocess,re
#
# sk=socket.socket()
# address=('127.0.0.1',8000)
# sk.connect(address)
# while True:
#     inp=(input("请输入"))
#     if inp == 'exit':
#         break
#     data = sk.send(bytes(inp, 'utf8'))
#     data = sk.recv(1024)
#     print(str(data, 'utf8'))
# sk.close()

# size=os.stat('11.jpg').st_size
# print(size)


# for i in range(65, 91):
#     s = "\r{name:s}".format(name=chr(i))
#     time.sleep(0.5)
#     sys.stdout.write(s)

import time,sys

# for i in range(50):
#     s = "\r进度".format()+str(i)+'%'
#     time.sleep(0.5)
#     sys.stdout.write(s)

# for i in range(50):
#     s='\r'+str(i)+'%进度'
#     time.sleep(0.5)
#     sys.stdout.write(s)

try:
    data = re.split('\s*', 'hello world my son',1)
    print(data)
except Exception as e:
    pass


