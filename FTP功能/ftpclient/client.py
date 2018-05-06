#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/13

import socket,os,sys
DIR=os.path.dirname(os.path.abspath(__file__))


sk=socket.socket()
address=('127.0.0.1',8000)

sk.connect(address)
print("客户端启动")
flg=True
while flg:
    inp = input("请输入用户密码登陆示例：xf|123 >>>>:").strip()
    name,passwd=inp.split('|')
    sk.sendall(bytes(inp, 'utf8'))
    while True:
        server_respon = sk.recv(1024)
        server_respon = str(server_respon, 'utf8')
        if server_respon == 'ok':
            print("用户连接成功,欢迎%s"%name)
            while True:
                print('''
                1,cmd|命令
                2，post|文件名
                3，get|文件名
                ''')
                inp = input(">>>:").strip()  # post|11.png
                cmd, path = inp.split('|')
                path = os.path.join(DIR, path)
                filename = os.path.basename(path)
                file_size = os.stat(path).st_size
                file_info = 'post|%s|%s' % (filename, file_size)
                sk.sendall(bytes(file_info, 'utf8'))
                f = open(path, 'rb')
                has_sent = 0
                while has_sent != file_size:
                    data = f.read(1024)
                    sk.sendall(data)
                    has_sent += len(data)
                    jd = round(has_sent / file_size, 2) * 100
                    s = "\r进度为" + str(jd) + '%'
                    sys.stdout.write(s)
                print("上传成功")
        elif server_respon == 'no':
            print("用户连接失败")
            break
sk.close()
















