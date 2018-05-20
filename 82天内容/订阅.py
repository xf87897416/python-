#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/5/9
import redis

pool= redis.ConnectionPool(host='192.168.0.90',port=6379,password='123',db=1)
r= redis.Redis(connection_pool=pool)

pub= r.pubsub() #打开收音机

pub.subscribe('fm8.7')#调台


pub.parse_response() #准备接受
print("准备监听")


data=pub.parse_response() #正式接受
print(data)







