#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/6

# 一、成员修饰符
#     共有成员
# 私有成员, __字段名
# - 无法直接访问，只能间接访问
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         #self.age = age
#         self.__age = age
#
#     def show(self):
#         return self.__age
# obj = Foo('xf','18')
# print(obj.name)
# print(obj.show())
################################
# 普通方法
# class foo:
#     def __f1(self):
#         return 123
#     def f2(self):
#         r=self.__f1()
#         return r
#
# obj=foo()
# ret = obj.f2()
# print(ret)
################################ 继承关系不能访问私有，也必须间接访问
# class F:
#     def __init__(self):
#         self.__father='father'
#
#     def sh(self):
#         return self.__father
# class S(F):
#     def __init__(self,name):
#         self.name = name
#         self.age=18
#         self.__sex = 'man'
#         super(S,self).__init__()
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.__sex)
#         print(self.sh())
# obj=S('xf')
# obj.show()
################################
# def __del__(self):  #被销毁时自动执行  析构方法
#     pass


# class foo:
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.sex='man'
#     def __getitem__(self, item):
#         return item+10
#     def __setitem__(self, key, value):
#         print(key,value)
#     def __delitem__(self, key):
#         print(key)
# # obj=foo('xf',22)
# # ret=obj.__dict__
# # print(ret)
# li=foo('xf',22)
# print(li[2])
# li[999]='xxoo'
# del li[999]

################################
# class foo(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __iter__(self):
#         return iter([11,22,33])
# '''
# 如果类中有__iter__方法，对象=》可迭代对象
# for 循环，迭代器next
# for 循环，可迭代对象，对象.__iter__(),迭代器，next
# 1执行li对象类中的__iter__方法，并取得返回值
# 2，循环上一部中返回对象
# '''
# li=foo('xf',22)
# for iter in li:
#     print(iter)
################################

from django.db import models
class Person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

# p = Person(name="Fred Flinstone", gender="M")
# p.save()
#
# print(p.get_gender_display())









