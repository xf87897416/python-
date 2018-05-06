#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/1/4

import time
'''

admin 中验证
obj.clean_fields()

form组件验证
model组件操作数据

ModelForm
    组件验证
    用model中的字段

示例：from django import forms

class Test(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField()



class UserForm(forms.ModelForm):
    class Meta:
        model=models.Test
        fields="__all__"
         
自己写的用form  admin用modelForm


























'''



