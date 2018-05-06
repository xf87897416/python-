#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/8

'''
bytes>>>>>str  解码 decoding
str >>>>>bytes 编码 encoding



SOCK_STREAM：TCP
SOCK_DGRAM: UDP

family=AF_INET ：服务器之间的通信
family=AF_INET6 ：服务器之间的通信
family=AF_UNIX : Unix不同进程间通信

server下的方法
     bind()
     listen()
     accept()
     recv()   收
     send（） 发
     sendall（）
     close()


client下的方法
     connetc()
     recv()   收
     send（） 发
     sendall（）
     close()


python3里面传送内容必须是bytes类型

'''
# import subprocess
# import socket
# sk=socket.socket()
# address=('127.0.0.1',8000)
# sk.bind(address)
#
# sk.listen(3)
# print("waiting。。。。")
#
# while 1:
#     conn, addr = sk.accept()
#     print(addr)
#     while True:
#         try:
#            data=conn.recv(1024)
#         except Exception:
#             break
#         if not data:break
#         print(str(data, 'utf8'))
#         obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
#         cmd_result = obj.stdout.read()
#         result_len=bytes(str(len(cmd_result)),'utf8')
#         # inp = (input("请输入"))
#         # conn.send(bytes(inp, 'utf8'))
#         conn.sendall(result_len)  #粘包现象!!!!!
#
#         conn.recv(1024)
#         conn.sendall(cmd_result)
# sk.close()  #只是关闭单独用户的连接

import subprocess
import socket

sk = socket.socket()
address=('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)
print("waiting...")
while 1:
    conn,addr = sk.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)
        except Exception:break
        if not data:break
        print(str(data, 'utf8'))
        obj=subprocess.Popen(str(data, 'utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result=obj.stdout.read()
        cmd_len=bytes(str(len(cmd_result)),'utf8')


        conn.sendall(cmd_len)
        conn.recv(1024)
        conn.sendall(cmd_result)
        # inp = input(">>>:")
        # conn.send(bytes(inp, 'utf8'))
conn.close()



