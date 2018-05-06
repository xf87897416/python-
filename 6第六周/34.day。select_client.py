#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/17


import socket,time

sk=socket.socket()
sk.connect(('127.0.0.1',8000))

while True:
    inp=input(">>>:")
    if inp == 'exit':
        break
    sk.sendall(bytes(inp,'utf8'))
    data=sk.recv(1024)
    print(data.decode('utf8'))





































