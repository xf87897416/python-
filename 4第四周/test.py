#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/10/31

class Foo:

    def __init__(self):
        pass

    def __int__(self):
        return 1111

    def __str__(self):
        return 'alex'

obj = Foo()
# print(obj, type(obj))

# int,对象，自动执行对象的 __int__方法，并将返回值赋值给int对象
r = int(obj)
print(r)
i = str(obj)
print(i)













