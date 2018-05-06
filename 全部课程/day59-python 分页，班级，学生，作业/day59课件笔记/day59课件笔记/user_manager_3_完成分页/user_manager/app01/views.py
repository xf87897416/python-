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

from django import views
from django.utils.decorators import method_decorator
"""
def outer(func):
    def inner(request, *args, **kwargs):
        print(request.method)
        return func(request, *args, **kwargs)
    return inner



class Order(views.View):
    pass
# CBV
# @method_decorator(outer, name='dispatch')
class Login(views.View):

    # @method_decorator(outer)
    def dispatch(self, request, *args, **kwargs):
        ret = super(Login, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self,request, *args, **kwargs):
        print('GET')
        return render(request, 'login.html', {'msg': ''})

    def post(self, request, *args, **kwargs):
        print('POST')
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
            return render(request, 'login.html', {'msg': message})

"""

class Login(views.View):

    def get(self,request, *args, **kwargs):
        return render(request, 'login.html', {'msg': ''})

    def post(self, request, *args, **kwargs):
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
            return render(request, 'login.html', {'msg': message})

# FBV
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
    if request.method == "GET":
        # for i in range(1000):
        #     models.Classes.objects.create(caption='全栈一班'+str(i))
        # 获取所有的班级列表
        # models.Classes.objects.create(caption='全栈一班')
        # models.Classes.objects.create(caption='全栈二班')
        # models.Classes.objects.create(caption='全栈三班')

        # 当前页
        current_page = request.GET.get('p',1)
        current_page = int(current_page)

        # 所有数据的个数
        total_count = models.Classes.objects.all().count()

        from utils.page import PagerHelper
        obj = PagerHelper(total_count, current_page, '/classes.html',5)
        pager = obj.pager_str()

        cls_list = models.Classes.objects.all()[obj.db_start:obj.db_end]

        current_user = request.session.get('username')
        return render(request,
                      'classes.html',
                      {'username': current_user, 'cls_list': cls_list, 'str_pager': pager})


    elif request.method == "POST":
        # Form表单提交的处理方式
        """
        caption = request.POST.get('caption',None)
        if caption:
            models.Classes.objects.create(caption=caption)
        return redirect('/classes.html')
        """
        # Ajax
        import json

        response_dict = {'status': True, 'error': None, 'data': None}

        caption = request.POST.get('caption', None)
        print(caption)
        if caption:
            obj = models.Classes.objects.create(caption=caption)
            response_dict['data'] = {'id': obj.id, 'caption': obj.caption}
        else:
            response_dict['status'] = False
            response_dict['error'] = "标题不能为空"
        return HttpResponse(json.dumps(response_dict))

@auth
def handle_add_classes(request):
    message = ""
    if request.method == "GET":
        return render(request, 'add_classes.html', {'msg': message})
    elif request.method == "POST":
        caption = request.POST.get('caption',None)
        if caption:
            models.Classes.objects.create(caption=caption)
        else:
            message = "标题不能为空"
            return render(request, 'add_classes.html', {'msg': message})
        return redirect('/classes.html')
    else:
        return redirect('/index.html')




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
