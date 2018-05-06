#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/15

'''
协程：协程是一种用户态的轻量级线程
不需要锁，也没有锁
高并发  nginx就是用协程，没有上下文开销
缺点：用不上多核，阻塞一个其余就都停了


'''

# from greenlet import greenlet
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1=greenlet(test1)
# gr2=greenlet(test2)
# gr1.switch()

#################################











