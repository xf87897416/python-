#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/13


import socketserver,os,sys
DIR=os.path.dirname(os.path.abspath(__file__))
DIR="".join(DIR+'\db')
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

class login():
    def __init__(self,name,passwd):
        self.name=name
        self.passwd=passwd
        self.home_dir=None
        self.c_dir=None
    def md(self):
        file="".join(DIR+'\\'+self.name)
        f=open(DIR+'\\'+ self.name,'r')
        user_data=f.read().strip()
        user_data=eval(user_data)
        name=str(self.name)
        passwd=str(self.passwd)
        if user_data['name'] ==name and user_data['passwd'] ==passwd:
            self.home_dir="".join(file+'123')
            self.c_dir="".join(file+'123')
            return '1'
        else:
            return '0'

class MYSERVER(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务启动。。")
        print(self.client_address)
        while True:
            conn = self.request
            flg=True
            while flg:
                    client_request = conn.recv(1024)  #ag|123
                    client_request=str(client_request, 'utf8')
                    try:
                        name,passwd=client_request.split('|')
                    except Exception:
                        conn.send(bytes('no', 'utf8'))
                        flg=False
                    obj=login(name,passwd)
                    result=obj.md()
                    if result == '1':
                        conn.send(bytes('ok','utf8'))
                        data = conn.recv(1024)
                        cmd, filename, file_size = str(data, 'utf8').split('|')
                        path = os.path.join(BASE_DIR, 'pig', filename)
                        file_size = int(file_size)
                        f = open(path, 'ab')
                        has_receive = 0
                        while has_receive != file_size:
                            data = conn.recv(1024)
                            f.write(data)
                            has_receive += len(data)
                            jd = round(has_receive / file_size, 2) * 100
                            s = "\r下载进度为" + str(jd) + '%'
                            sys.stdout.write(s)
                        f.close()
                    else:
                        print("用户名或密码错误")
                        conn.send(bytes('no', 'utf8'))
                        flg=False




                # inp = input(">>>:")
                # conn.sendall(bytes(inp, 'utf8'))
            # conn.close()

if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8000),MYSERVER)
    server.serve_forever()



# #注册功能
# os.makedirs(DIR+'\hfy123')
# f=open(DIR+r'\hfy','w')
# data={'name':'hfy','passwd':'abc'}
# f.write(str(data))
# f.close()







