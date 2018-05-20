#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/5/9

import redis

pool= redis.ConnectionPool(host='192.168.0.90',port=6379,password='123',db=1)

r= redis.Redis(connection_pool=pool)

r.publish('fm8.7','nihao!')















