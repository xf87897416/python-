#__author:  Administrator
#date:  2016/12/29
from django.shortcuts import render
from django import forms
from app01 import models
from django.forms import widgets as ws
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

class UserModelForm(forms.ModelForm):
    name=forms.CharField()
    class Meta:
        model = models.User
        # fields = "__all__"
        fields=['name','email','user_type']
        labels ={
            'email':'邮箱'
        }
        help_texts={
            'email':'输入你他么的邮箱'
        }
        widgets={
            'name':ws.Textarea(attrs={'class':'c1'})
        }
        # validators = {'name':RegexValidator(regex='root_\d+', message='错误了', code='invalid')
        #               }
        error_messages={
            'name':{'required':'必填','invalid':'何时错误!!'},
            'email':{'required':'请输入邮箱','invalid':'何时错误'},
            'user_type':{'required':'请输入用户类型','invalid':'何时错误'},
            'm':{'required':'请输入关系','invalid':'何时错误'},
        }
        field_classes={
            'name':forms.CharField
        }
        localized_fields=('ctime',)



    def clean_name(self):
        value = self.cleaned_data['name']
        if value == '123':
            return value
        else:
            raise ValidationError('错了！！...')
    #
    #
    # def clean(self):
    #     return self.cleaned_data




def index(request):

    if request.method == "GET":
        obj = UserModelForm()
        return render(request,'mf.html',{'obj': obj})
    elif request.method == "POST":
        obj = UserModelForm(request.POST)
        if obj.is_valid():
            # print(obj.cleaned_data)
            # models.User.objects.create(**obj.cleaned_data)
            request.session['is_login'] = True
            obj.save(commit=True)
            """
            mobj = obj.save(commit=False)
            mobj.save()
            obj.save_m2m()
            """
        else:
            request.session['is_login'] = False
        print(obj.errors)

        return render(request, 'mf.html', {'obj': obj})

def edit_index(request,nid):
    if request.method == "GET":
        print(nid)
        model_obj = models.User.objects.get(id=nid)
        obj =UserModelForm(instance=model_obj)
        return render(request, 'mf1.html', {'obj': obj,'nid': nid})
    elif request.method == 'POST':
        model_obj = models.User.objects.get(id=nid)

        obj = UserModelForm(request.POST, instance=model_obj)
        if obj.is_valid():
            obj.save()
        return render(request, 'mf1.html', {'obj': obj})


