#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/1/6


import time
'''


'''
import random
def random_code():
    code = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp = chr(random.randint(65,90))
        else:
            temp = random.randint(0,9)
        code += str(temp)
    return code
from django import forms

import datetime
class SendMsgForm(forms.Form):
    email=forms.EmailField(error_messages={'invalid':'邮箱格式错误'})

class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    email_code=forms.CharField()

class LoginForm(forms.Form):
    user=forms.CharField()
    pwd=forms.CharField()
    code=forms.CharField()


class BaseResponse:
    def __init__(self):
        self.status=False
        self.code=None
        self.data=None
        self.summary=None
        self.message={}

def send_msg(request):
    rep=BaseResponse()
    form =SendMsgForm(request.POST)
    if form.is_valid():
        _value_dic=form.clean()
        email=_value_dic['email']
        has_exists_email=models.UserInfo.objects.filter(email=email).count()
        if has_exists_email:
            rep.summary='此邮箱已经注册'
            return HttpResponse(json.dumps(req.__dict__))
        current_date=datetime.datetime.now()
        code=random_code()
        count=models.SendMsg.objects.filter(email=email).count()

        if  not count:
            models.SendMsg.objects.filter.create(code=code,email=email,ctime=current_date)
            rep.status=True

        else:#存在用户
            limit_day=current_date - datetime.timedelta(hours=1)

            times =models.SendMsg.objects.filter(email=email,ctime__gt=limit_day,times__gt=9).count()
            if times:
                rep.summary="'已超最大次数（1小时后重试）'"
            else:
                unfreeze=models.SendMsg.objects.filter(email=email,ctime__lt=limit_day).count()
                if unfreeze:
                    models.SendMsg.objects.filter(email=email),update(time=0)

                from django.db.models import F

                models.SendMsg.objects.filter(email=email).update(code=code,ctime=current_date,times=F('times'+1))
                rep.status = True
    else:
        rep.summary=form.errors['email'][0]
    return HttpResponse(json.dumps(rep.__dict__))




























































