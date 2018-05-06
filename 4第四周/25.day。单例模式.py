#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/6
#永远使用一个对象，单例模式
# class foo:
#     __v = None
#     @classmethod
#     def get_instance(cls):
#         if cls.__v:
#             return cls.__v
#         else:
#             cls.__v=foo()
#             return cls.__v
# obj=foo.get_instance()
# print(obj)
#
# obj2=foo.get_instance()
# print(obj2)
############################################

class F1:
    def __init__(self):
        self.name= 'xf'

class F2:
    def __init__(self,a):
        self.ff = a

class F3:
    def __init__(self,b):
        self.dd = b

f1 = F1()
f2 = F2(f1)
f3 = F3(f2)

print(f3.dd.ff.name)















