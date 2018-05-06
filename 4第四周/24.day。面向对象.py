#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/4



# def foo(name,age,sex,content):
#     print(name,age,sex,content)
#
# foo('xf','22','man','有啥不一样')
# foo('xf','22','man','我们不一样')
# foo('xf','22','man','咱当兵的就是不一样')

# class bar():
#     def zoo(self,content):
#         print(self.name, self.age, self.sex, content)
# obj=bar()
# obj.name='xf'
# obj.age='22'
# obj.sex='man'
#
# obj.zoo('我们不一样')
# obj.zoo('有啥不一样')

#三大特点，封装
######################################
#构造方法
# class msg:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#         self.x='o'
#     def show(self):
#         print("%s--%s--%s" % (self.n,self.a,self.x))
#
# xf=msg('xf',18)
# xf.show()

#############################

#面向对象三大特性之二：继承
# class 父类:
#     pass
# class 子类(父类):
#     pass


# 2、重写
# 防止执行父类中的方法
# 3、self永远是执行改方法的调用者
# 4、
# super(子类, self).父类中的方法(...)
# 父类名.父类中的方法(self, ...)
# 5、Python中支持多继承
# a.左侧优先
# b.一条道走到黑
# c.同一个根时，根最后执行

# class base():
#     pass
#
# class mother(base):
#     def liker(self):
#         print("mother liker")
#         self.skill()
#     def skill(self):
#         print("mother,skill")
#
# class father:
#     def skill(self):
#         print("father,skill")
#
# class son(father,mother):
#     pass
# obj=son()
# obj.liker()
###########################################
#练习
# class Foo:
#
#     def __init__(self, name):
#         # 普通字段
#         self.name = name
#
#     # 普通方法
#     def show(self):
#         print(self.name)
# obj = Foo('alex')
# obj.name
# obj.show()
#############################################
#静态方法   直接调用类
class foo:
    def bar(self):
        print("is bar")
    @staticmethod
    def sta():
        print('is sta')

# foo.sta()
# obj=foo()
# obj.bar()
#############################################
#属性分页@property
# list=[]
# for i in range(1000):
#     list.append(i)
# while True:
#     chose=input("your chose page:")
#     class fuction:
#         def __init__(self,chose):
#             self.page=int(chose)
#         @property
#         def start(self):
#             val=(self.page - 1)*10
#             return val
#         @property
#         def end(self):
#             val2=(self.page * 10)
#             return val2
#     obj = fuction(chose)
#     print(list[obj.start:obj.end])
















