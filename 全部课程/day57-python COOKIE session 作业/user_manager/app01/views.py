from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
# def test(request):
#     print(request.COOKIES)
#     # return HttpResponse('Ok')
#     obj = HttpResponse('Ok')
#     import datetime
#     # v = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
#     # # obj.set_cookie('k3','333333',max_age=10,expires=v,path='/')
#     # obj.set_cookie('k5','v5',max_age=10,expires=v, domain='oldboy.com')
#     # # oldboy.com   k5:v5
#     # obj.set_cookie('k6','v6')
#     obj.set_cookie('k7','v7',httponly=True)
#     return obj
#
# def xiaohu(request):
#     v = request.COOKIES.get('k7')
#     return HttpResponse(v)



"""
def login(request):
    message = ""
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:

            rep = redirect('/index.html')
            # rep.set_cookie('username', user)
            # rep.set_cookie('account', "123123123")
            # rep.set_cookie('pwd', "asdfasdfasdfasdf")
            rep.set_signed_cookie('username', user)
            rep.set_signed_cookie('account', "123123123")
            rep.set_signed_cookie('pwd', "asdfasdfasdfasdf")
            return rep

            # return redirect('/index.html')
        else:
            message = "用户名或密码错误"
    return render(request,'login.html', {'msg': message})

def index(request):
    # 如果用户已经登录，获取当前登录的用户名
    # 否则，返回登录页面
    # username = request.COOKIES.get('username')

    username = request.get_signed_cookie('username')
    if username:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('/login.html')

"""
# def js_cookie(request):
#     print(request.COOKIES)
#     obj = render(request, 'js_cookie.html')
#     obj.set_cookie('guoyongchang', 'girl')
#     return obj


def login(request):
    message = ""
    v = request.session
    print(type(v))
    from django.contrib.sessions.backends.db import SessionStore
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
    obj = render(request,'login.html', {'msg': message})
    return obj

def logout(request):
    request.session.clear()
    return redirect('/login.html')



def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')
    return inner

@auth
def index(request):
    current_user = request.session.get('username')
    return render(request, 'index.html',{'username': current_user})

@auth
def handle_classes(request):

    current_user = request.session.get('username')
    return render(request, 'classes.html', {'username': current_user})


def handle_student(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return render(request, 'student.html', {'username': current_user})
    else:
        return redirect('/login.html')


def handle_teacher(request):
    is_login = request.session.get('is_login')
    if is_login:
        current_user = request.session.get('username')
        return render(request, 'teacher.html', {'username': current_user})
    else:
        return redirect('/login.html')
