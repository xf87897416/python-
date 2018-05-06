#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/9



import socketserver

class MYSERVER(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务启动。。")
        print(self.client_address)
        while True:
            conn = self.request
            while True:
                client_request = conn.recv(1024)
                print(str(client_request, 'utf8'))
                inp = input(">>>:")
                conn.sendall(bytes(inp, 'utf8'))
            conn.close()

if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8000),MYSERVER)
    server.serve_forever()





























