#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/9
import socket

sk=socket.socket()
address=('127.0.0.1',8000)
sk.connect(address)
while True:
    print("客户端启动")
    inp=input(">>>>:").strip()
    sk.sendall(bytes(inp,'utf8'))

    server_respon=sk.recv(1024)
    print(str(server_respon,'utf8'))










