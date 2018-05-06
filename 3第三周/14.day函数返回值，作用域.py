#_author: "Administrator"
#date: 2017/10/26


# def f():
# 	print('ok')
# 	return 'abc'   #结束函数时返回给调用者一个值
# 	print('xf')
#返回什么内容 ，给谁？
# a=f()
# print(a)
#注意点：函数如果没有return，会默认返回None
#如果return返回多个对象，则会用元组（），返回


#  内函数不能改外变量的值
# count=10
# def outer():
#     global count
#     print(count)
#     count=5
# outer()
# print(count)


# count=30
# def outer():
#     count = 10
#     def inner():
#         global count
#         count=20
#         print(count)
#     inner()
# outer()
# print(count,'is')

#变量查找范围LEGB
#内部作用域声明就会覆盖外部作用域
#局部作用域---》外层嵌套作用域---》全局变量----》系统内置









