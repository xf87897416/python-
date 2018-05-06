#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/6


# try:
#     ipt=input("请输入序号：")
#     i = int(ipt)
#     print(i)
#     int('123')
# except IndexError as e:
#     print('IndexError')
# except Exception as e:
#     print("error 403")
#     print(e)
# else:
#     print('else')
# finally:
#     print("最后一定执行")
#########################################
#主动触发异常
# try:
#     int('xfxfa')
#     # raise Exception("不过日子了")
# except Exception as e:
#     print(e)
#########################################
# print(123)
# assert 1==1
# print(456)
#一般用于强制用户服从
#########################################
#反射  通过字符串的方式操作对象中的成员
#去什么东西里面获取什么属性
# class foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# obj=foo('xf',22)
# val=getattr(obj,'name')
# print(val)
# print(hasattr(obj,'age'))  #判断有没有成员
# delattr(obj,'name')  #删除成员

##############################################
# import s2
# inp=input("请输入url")
# if hasattr(s2,inp):
#     func=getattr(s2,inp)
#     ret=func()
#     print(ret)
# else:
#     print('404')






