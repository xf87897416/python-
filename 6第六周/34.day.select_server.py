#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/17


# import socket,time
# import select
#
# sk=socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen(5)
#
# sk1=socket.socket()
# sk1.bind(('127.0.0.1',8000))
# sk1.listen(3)
#
# while True:
#     r,w,e=select.select([sk,sk1],[],[],5)
#     for i in r:
#         conn,addr=i.accept()
#         print('conn',conn)
#         print("hello")
#
#     print("r>>>>:",r)


#######################toalk_server##############

import socket,select
sk=socket.socket()

sk.bind(('127.0.0.1',8000))
sk.listen(3)
inp=[sk,]

while True:
    inputs,outputs,errors=select.select(inp,[],[],5)

    for obj in inputs:
        if obj == sk:
            conn,addr=obj.accept()
            print(conn)
            inp.append(conn)
        else:
            try:
                data = obj.recv(1024)
                print(data.decode('utf8'))
                Inputs = input("回答%s>>>:" % inp.index(obj))
                obj.sendall(Inputs.encode('utf8'))
            except Exception as e:
                del inp[inp.index(obj)]
                obj.close()





















