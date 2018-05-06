#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/8

# import socket
# import socket
# sk=socket.socket()
# address=('127.0.0.1',8000)
# sk.connect(address)
# while True:
#     inp=(input("请输入"))
#     if inp == 'exit':
#         break
#     data = sk.send(bytes(inp, 'utf8'))
#     result_len=int(str(sk.recv(1024),'utf8'))
#     print(result_len)
#     sk.send(bytes('ok', 'utf8'))
#     data=bytes()
#     while len(data)!=result_len:
#         recv = sk.recv(1024)
#         data+=recv
#     print(str(data, 'gbk'))
# sk.close()

import subprocess
import socket

sk=socket.socket()
address=('127.0.0.1',8000)
sk.connect(address)

while 1:
    inp = input(">>>:")
    if inp == 'exit':break
    sk.send(bytes(inp, 'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    sk.sendall(bytes('ok','utf8'))
    data=bytes()
    while len(data) !=result_len:
        recv=sk.recv(1024)
        data+=recv

    print(str(data, 'gbk'))

sk.close()
