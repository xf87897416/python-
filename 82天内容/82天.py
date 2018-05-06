#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/4/21
import os

'''
ununtu 安装 readis

apt-get install redis-server
readis-cli 连接


http://www.cnblogs.com/alex3714/articles/6217453.html
！！！

设置用户量，
setbit LOGIN_USER 0 0

第一个用户登录
setbit LOGIN_USER 用户唯一id 1
第一个用户退出
setbit LOGIN_USER 用户唯一id 0

统计所有用户一共有几个
bitcount LOGIN_USER

查看用户在不在
getbit LOGIN_USER 用户唯一id


















'''