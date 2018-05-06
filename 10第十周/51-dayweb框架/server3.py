#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/9
from wsgiref.simple_server import make_server
import time

def current_time(request):
    cur_time=time.ctime(time.time())
    with open('index.html','rb') as f:
        data=f.read()
        data=str(data,'utf8').replace("!current_time!",cur_time)
    return [data.encode('utf8')]

def f1(request):
    return [b'<h1>hello book</h1>']

def f2(request):
    return [b'<h1>hello Web</h1>']

def login(request):
    print(request)

    return [b'<h1>hello user</h1>']

def routers():
    urlpatterns=(
        ('/book',f1),
        ('/web',f2),
        ('/login',login),
        ('/current_time',current_time),
    )
    return urlpatterns

def application(environ,start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])

    path=environ["PATH_INFO"]

    print(path)
    urlpatterns=routers()
    func=None
    for i in urlpatterns:
        if i[0] == path:
            func=i[1]
            break
    if func:
        return func(environ)
    else:
        return ['<h1>404</h1>'.encode("utf8")]



httpd=make_server('localhost',8080,application)

print('Serving HTTP on port 8080...')

httpd.serve_forever()










