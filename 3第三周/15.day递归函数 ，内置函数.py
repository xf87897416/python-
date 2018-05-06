#_author: "Administrator"
#date: 2017/10/27


#递归函数 ，内置函数

#阶乘

# def f(n):
#     ret=1
#     for i in range(1,n+1):
#         ret=ret*i
#     return ret
# print(f(5))

# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

#关于递归，调用自身函数
#要有结束条件 ，

#但凡是递归可以写出来的，循环都可以解决
#递归效率低，不推荐使用

#菲波那切数列

# def feibo(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return feibo(n-1)+feibo(n-2)
# print(feibo(8))
# for i in range(1,9):
#     print(feibo(i))


# def feibo(n):
#     if n<=1:
#         return n
#     else:
#         return feibo(n - 1) + feibo(n - 2)
#
# num=int(input("请输入："))
# for i in range(num):
#     print(feibo(i))
# 0,1,1,2,3,5,8,13
#
def feibo(n):
    a,b=0,1
    while n:
        print(a)
        a,b,n=b,a+b,n-1
#
# feibo(8)
# !!!!!!!!!!!!!
# fibs = [0, 1]
# for i in range(3):
#  fibs.append(fibs[-2] + fibs[-1])
# print(fibs)

# i, j = 0, 1
# while i < 10000:
#  print(i),
#  i, j = j, i+j


#内置函数
#  filter 过滤器

# str = ['a', 'b', 'c', 'd']
# def fun1(s):
#     if s != 'a':
#         return s
# ret = filter(fun1, str)
# print(list(ret))  # ret是一个迭代器对象

#map 处理
# str = [ 'a', 'b']
# def fun2(s):
#     return s + "alvin"
# ret = map(fun2, str)
# print(ret)  # map object的迭代器
# print(list(ret))  # ['aalvin', 'balvin', 'calvin', 'dalvin']

#3 reduce
# from functools import reduce
# def add1(x,y):
#     return x + y
# print (reduce(add1, range(1,101)))


#lambda    因为lamdba在创建时不需要命名，所以，叫匿名函数
# add = lambda a,b : a + b
# print add(2,3)

# from functools import reduce
# print(reduce(lambda x,y : x*y ,range(1,6)))
#面向函数式编程
