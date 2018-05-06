#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/9



import time



'''
MVC模式（M模型  C控制器   V视图）
model  controler view

MTV模型 
model  template   view

创建Djiango





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>123</title>
</head>
<body>
<form action="/userInfo" method="post">
    <p>姓名<input type="text" name="username"></p>
    <p>性别<input type="text" name="sex"></p>
    <p>邮箱<input type="text" name="email"></p>
    <p><input type="submit" name="submit"></p>

</form>
<hr>
<h1>数据展示</h1>
<table border="1px">
    <tr>
        <td>姓名</td>
        <td>性别</td>
        <td>邮箱</td>
    </tr>
{#user_list=[{},{},{}]#}
    {% for i in user_list %}
        <tr>
        <td>{{i.username}}</td>
        <td>{{i.sex }}</td>
        <td>{{i.email  }}</td>
        </tr>
    {% endfor %}
</table>

</body>
</html>


-------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>time</title>
</head>
<body>
<p>time:{{ abc }}</p>
</body>
</html>
----------------------------

from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^userInfo",views.userInfo),
    url(r"^cur_time",views.cur_time),
    # url(r'^articles/2003/$', views.special_case_2003),
]

--------------------------------------------------


import datetime


def cur_time(request):
    # return HttpResponse("<h1>ok</h1>")
    times=datetime.datetime.now()
    return render(request, "time.html", {"abc":times})


def userInfo(req):
    user_list = []
    if req.method=="POST":
        u=req.POST.get("username",None)
        s=req.POST.get("sex",None)
        e=req.POST.get("email",None)
        # user={"username":username,"sex":sex,"email":email}
        #
        # user_list.append(user)
        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,
        )
        user_list = models.UserInfo.objects.all()

    return render(req,'index.html',{"user_list":user_list})

def special_case_2003(req):
    return HttpResponse("2003")




class UserInfo(models.Model):
    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=mo


-----------------------------------------------

[os.path.join(BASE_DIR, "templates")],





命令创建项目：
    django-admin startproject mysite
    
创建app:
     python3 manage.py startapp blog

     python manage.py runserver  127.0.0.1:8090
 
 
 python manage.py makemigrations  
 python manage.py migrate   
 
http://www.cnblogs.com/yuanchenqi/articles/6083427.html


STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"statics"),
)

静态文件







'''