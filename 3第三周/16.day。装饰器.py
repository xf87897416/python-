#_author: "Administrator"
#date: 2017/10/27
#装饰器  就是一种函数
#功能函数加参数
# def show_time(f):
#     def inner(*x,**y):
#         start = time.time()
#         f(*x,**y)
#         end = time.time()
#         print('speed: %s' % (end - start))
#     return inner
# import time
#
# @show_time
# def foo():
#     time.sleep(2)
#     print('foo....')
#
# @show_time
# def bar():
#     print('bar...')
#     time.sleep(3)

# bar=show_time(bar) #@show_time
# bar()  #执行inner函数
# @show_time
# def add(*a,**b):
#     sums=0
#     for i in a:
#         sums+=i
#     time.sleep(1)
#     print(sums)
#
# add(1,5,8,3)

#装饰器加参数
import time
def loger(flag=''):
    def show_time(f):
        def inner(*x,**y):
            start = time.time()
            f(*x,**y)
            end = time.time()
            print('speed: %s' % (end - start))
            if flag=='true':
                print('日志记录')
        return inner
    return show_time

@loger('true')
def add(*a,**b):
    sums=0
    for i in a:
        sums+=i
    time.sleep(1)
    print(sums)

add(1,7,4)

