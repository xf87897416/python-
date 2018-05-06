#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/8



import subprocess,sys
import socket
import os
# sk=socket.socket()
# address=('127.0.0.1',8000)
# sk.connect(address)
#
# BASE_NAME=os.path.dirname(os.path.abspath(__file__))
# while 1:
#     inp = input(">>>:") .strip()  #post|11.png
#     cmd,path=inp.split('|')
#     path=os.path.join(BASE_NAME,path)
#     filename=os.path.basename(path)
#     file_size=os.stat(path).st_size
#     # file_md5=a
#     file_info='post|%s|%s|$s'%(filename,file_size,file_md5)
#     sk.sendall(bytes(file_info,'utf8'))
#     f=open(path,'rb')
#     has_sent=0
#     while has_sent!=file_size:
#         data = f.read(1024)
#         sk.sendall(data)
#         has_sent+=len(data)
#         jd=round(has_sent / file_size,2)*100
#         s = "\r进度为"+ str(jd)+'%'
#         sys.stdout.write(s)
#     print("上传成功")
# sk.close()
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
sk.connect(address)

BASE_NAME=os.path.dirname(os.path.abspath(__file__))
while 1:
    inp = input(">>>:") .strip()  #post|11.png
    cmd,path=inp.split('|')
    path=os.path.join(BASE_NAME,path)
    filename=os.path.basename(path)
    file_size=os.stat(path).st_size
    file_md5=str(get_md5_02(path))
    file_info='post|%s|%s|%s'%(filename,file_size,file_md5)
    sk.sendall(bytes(file_info,'utf8'))  #请求文件
    has_sent = 0
    msg=str(sk.recv(2048),'utf8')

    if msg == 'ok':
        f = open(path, 'rb')
    else:
        chose = input(msg + '>>>:').strip()
        if chose == 'Y':
            sk.sendall(bytes('Y', 'utf8'))
            old_file_size = int(str(sk.recv(1024), 'utf-8'))
            has_sent += old_file_size
        else:
            sk.sendall(bytes('N', 'utf8'))
        f = open(path, 'rb')
        f.seek(has_sent)
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
        jd = round(has_sent / file_size, 2) * 100
        s = "\r进度为" + str(jd) + '%'
        sys.stdout.write(s)
    print("上传成功")

sk.close()












