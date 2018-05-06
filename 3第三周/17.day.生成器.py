#_author: "Administrator"
#date: 2017/10/28

# def add(n):
#     return n*n*n
# a=[add(x) for x in range(10)]
# print(a)


# a=(x*2 for x in range(10))
# print(next(a))   #PY2 :a.next()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#生成器就是一个可迭代对象
#####################################
# for i in a:
#     print(i)

#生成器两种创建方式
#1,a=(x*2 for x in range(10))
#2,yield
#什么是可迭代对象（拥有iter方法的）

# def foo():
#     print("ok")
#     yield 1
#     print("ok2")
#     yield 2
#
# for i in foo():
#     print(i)


# def feibo(max):
#     n,befor,after=0,0,1
#     while n< max:
#         print(befor)
#         befor,after=after,befor+after
#         n+=1
# feibo(8)
#print(feibo(8)) #<generator object feibo at 0x0000000001E07A40>



# def bar():
#     print('ok1')
#     count=yield 1
#     print(count)
#     print('ok2')
#     yield 2
# b=bar()
# b.send(None) #next.(b)
# b.send('eee')













