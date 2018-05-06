#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/8

import subprocess
import socket
import os
import sys

# sk=socket.socket()
# address=('127.0.0.1',8000)
# sk.bind(address)
# base_dir=os.path.dirname(os.path.abspath(__file__))
# base_dir="".join(base_dir+'\\pig')
# if os.path.isfile(base_dir):
#     os.makedirs(base_dir)
#
# sk.listen(3)
# print("waiting。。。。")
# BASE_NAME=os.path.dirname(os.path.abspath(__file__))
# while 1:
#     conn, addr = sk.accept()
#     while True:
#         data=conn.recv(1024)
#         cmd,filename,file_size=str(data,'utf8').split('|')
#         path=os.path.join(BASE_NAME,'pig',filename)
#         file_size=int(file_size)
#         f=open(path,'ab')
#         has_receive=0
#         while has_receive!=file_size:
#             data=conn.recv(1024)
#             f.write(data)
#             has_receive+=len(data)
#             jd = round(has_receive / file_size, 2) * 100
#             s = "\r下载进度为" + str(jd) + '%'
#             sys.stdout.write(s)
#         f.close()

import hashlib
import os

def get_md5_02(file_path):
    f = open(file_path, 'rb')
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5

sk=socket.socket()
address=('127.0.0.1',8000)
sk.bind(address)
base_dir=os.path.dirname(os.path.abspath(__file__))
base_dir="".join(base_dir+'\\pig')
if os.path.isfile(base_dir):
    os.makedirs(base_dir)

sk.listen(3)
print("waiting。。。。")
BASE_NAME=os.path.dirname(os.path.abspath(__file__))
while 1:
    conn, addr = sk.accept()
    while True:
        data=conn.recv(1024)
        cmd,filename,file_size,file_md5=str(data,'utf8').split('|')
        path=os.path.join(BASE_NAME,'pig',filename)
        file_size=int(file_size)
        has_received = 0
        if os.path.isfile(path):
            msg="文件已存在，是否需要续传? Y/N:"
            conn.sendall(bytes(msg,'utf8'))
            chose=str(conn.recv(2048),'utf8')
            if chose == 'Y':
                Old_file_size=int(os.stat(path).st_size)
                conn.sendall(bytes(str(Old_file_size), 'utf-8'))
                has_received += Old_file_size
                f = open(path, 'ab')
            elif chose == 'N':
                f = open(path, 'wb')
        else:
            msg = 'ok'
            conn.sendall(bytes(msg, 'utf8'))
            f = open(path, 'wb')
        while has_received != file_size:
            data = conn.recv(1024)
            f.write(data)
            has_received += len(data)
            jd = round(has_received / file_size, 2) * 100
            s = "\r下载进度为" + str(jd) + '%'
            sys.stdout.write(s)
        f.close()




