#_author: "Administrator"
#date: 2017/10/28

#生成器都是迭代器
#list,tuple,dict,string:Iterable（可迭代对象可以使用_iter_）
# l=[1,2,3,5,7,9]
# d=iter(l)
#
# print(d)
# 什么是迭代器？
# 满足两个条件：1，有iter方法，2，有next方法
# print(next(d))
# print(next(d))

#for 循环内部三件事：
# 1，调用可迭代对象的iter方法返回一个迭代对象
# 2，不断调用可迭代对象的next方法
# 3，处理stopiteration

# from collections import Iterator,Iterable
# print(isinstance(l,Iterable))  #
# print(isinstance(l,Iterator))  #迭代器


# f=open('登录文件.txt','r',encoding='utf-8')
# # allLines = [line.strip() for line in f]
# allLines=iter(f.readlines())
# f.close()
# longest = 0
# longLine = ""
# for line in allLines:
#     linelen = len(line)
#     if linelen > longest:
#         longest = linelen
#         longLine = line
# print('Longest line: %s' % longLine )
# print('The number of longest line: %s' % longest )










