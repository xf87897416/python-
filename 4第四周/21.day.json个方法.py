#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/1

import json
# 只能转普通数据类型
# dic={'name':'hfy','age':'18'}
# f=open('登陆文件.txt','a')
# data=json.dumps(dic)
# f.write(data)
# f.close()

# data = json.dump(dic, f)


# f=open('登陆文件.txt','r')
# date=f.read()
# data=json.load(f)
# print(data)




#------------------------------------------------
# dic={'name':'xf','age':'18'}
# f=open('登陆文件.txt','w')
# json.dump(dic,f)
# f.close()
# f=open('登陆文件.txt','r')
# data=json.load(f)
# print(data)

####################################
# import pickle
#
# def foo():
#     print('ok')
#
# data=pickle.dumps(foo)
#
# data=pickle.loads(data)

#########################################

import shelve

f=shelve.open('test.txt')
f['users']={'name':'hfy','age':'18'}

f=shelve.open('test.txt')

print(f['users']['name'])

#字典里面可以用
# d={'name':'xf','age':'18'}
# print(d['name'])
# print(d.get('name'))
# print(d.get('hooby','women'))  #默认返回值




