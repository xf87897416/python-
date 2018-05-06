#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/10/30

# import configparser
#
# config= configparser.ConfigParser()
# config["DEFAULT"] = { 'ServerAliveInterval':'45',
#                        'Compression':'yes',
#                        'CompressionLevel':'9'}
# config['server']= {'hostname':'xf',
#                     'ip':'192.168.0.6',
#                     'port':'3306'}
# config.set('server','hostname','hfy')   #修改其中的值
# with open('config.conf','w') as configfile:
#     config.write(configfile)

# config.read('config.conf')   #查看
# print(config.defaults())
# print(config['server']['hostname'])
#
# for key in config['DEFAULT']:
#     print(key)

# config.remove_section('server')  #删除
# config.remove_option('server','hostname')
# config.write(open('config.conf','w'))
# print(config.has_section('server')) #判断

###################################################
#正则表达式
import re
#  . ^ $
# 次数匹配
#    * [0,+00]
# + 至少一次 [1,+00]
# ？  [0,1]
#  {n}  匹配前面n次   {n，m}  匹配n到m次

#字符集[]    取消元字符的特殊功能   列外(\  ^ -  )

# ret=re.findall('a[a-z]c','avc')
# print(ret)

#  \
#  \d  匹配数字 相当于[0-9]
#  \D  匹配任何非数字 相当于[^0-9]
#  \s  匹配任何空白字符 相当于[\t\n\r\f\v]
#  \S  匹配任何非空白字符 相当于[ ^\t\n\r\f\v]
#  \w 匹配任何字母和数字   相当于[a-zA-Z0-9]
#  \W  匹配任何非字母和数字   相当于[^a-zA-Z0-9]
#  \b  匹配一个单词边界  指单词和特殊字符的位置


# ret=re.search('xf','asxfzxfaf')  #只找第一个
# print(ret.group())

# ret=re.search('a\.b','axbaftaga.bgbasb').group()
# print(ret)

# ret=re.findall('x.c','asafzx\csdf')
# print(ret)

##########################################
#  分组
# () | 管道符是或
#
#
# print(re.search('(as)|3','sdada3sas').group())

#加名字
# ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
#
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))

#正则表达式的方法：
# 1， findall():所有结果返回到一个列表里
# 2， search（）：返回匹配到的第一个对象（object），用group调取
# 3，match（）：只在字符串开始匹配,也用group调用对象
# 4, split()
#5, compile 多次调用
# ret=re.split('[x,f]','asdxtyfsdg')   #******先分左边，分完分右边
# print(ret)
#替换 可以加n 替换次数
# ret=re.sub('t.o','xx','too many and not two much',n)
# print(ret)

# obj=re.compile('\.com')
# date=obj.findall('www.xfagag.comag')
# print(date)



