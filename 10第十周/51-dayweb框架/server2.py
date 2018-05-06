#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/9
from wsgiref.simple_server import make_server



def application(environ,start_response):
    #通过environ封装一个所有请求信息的对象
    #start_response可以方便的设置响应头
    start_response("200 OK",[('Content-Type','text/html')])
    return [b'<h1>Hello ,web</h1>']

#封装socket对象以及转呗过程（socket，bind，listen）
httpd=make_server('localhost',8080,application)

print('Serving HTTP on port 8080...')

httpd.serve_forever()






















