#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/15

#
# import gevent,time
#
# def foo():
#     print("Running in foo",time.ctime())
#     gevent.sleep(1)
#     print("runng in foo 2",time.ctime())
# def bar():
#     print("Start in bar",time.ctime())
#     gevent.sleep(2)
#     print("start in bat 2",time.ctime())
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

##########################################
# import gevent
# from gevent import monkey
# from urllib.request import urlopen
# import time
# monkey.patch_all()
# def f(url):
#     print("GET:%s"%url)
#     resp=urlopen(url)
#     data=resp.read()
#
#     print("%d bytes received from %s"%(len(data),url))
#
# l=['http://www.xiaohuar.com/','https://www.aliyun.com/','https://www.bilibili.com/','https://bangumi.bilibili.com/guochuang/']
#
# start=time.time()
# for url in l:
#     f(url)
#
#
# # gevent.joinall([
# #     gevent.spawn(f,'http://www.xiaohuar.com/'),
# #     gevent.spawn(f,'https://www.aliyun.com/'),
# #     gevent.spawn(f,'https://www.bilibili.com/'),
# #     gevent.spawn(f,'https://bangumi.bilibili.com/guochuang/'),
# # ])
#
#
# print(time.time()-start)