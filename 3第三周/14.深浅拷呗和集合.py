

# import copy
# husbent=['xf','001',[15000,10000]]
# xiaosan = copy.deepcopy(husbent)
# wife=husbent.copy() #浅拷贝，只拷贝第一层
#                     # 深拷贝=克隆一份
# wife[0]='hfy'
# wife[1]='002'
# # wife[2][1]-=3000
# #xiaosan=copy.copy()  #copy.copy 浅拷贝
# xiaosan[0]='nvren'
# xiaosan[1]='666'
# xiaosan[2][1]-=3000
# # print(wife)
# print(xiaosan)
# print(husbent)


# 整形
# 浮点型
# 字符串
# 列表
# 字典
# 元组
# 布尔
# 集合

# s=['xf','abc','xf']
# s1=set(s)
# print(s1,type(s1))
# s2=list(s1)
# print(s2,type(s2))
#去重复 应用     set集合里面不能有可变元素，必须不可变的
#   set  是无序的，不重复的

# s=set(['xf','abc','hfy'])
# print(s)
# for i in s:
# 	print(i)
# s.add('u') #添加一个元素
# print(s)
# s.update('123')     #添加多个元素
# print(s)



# s.remove('xf')  # 删除指定元素
# print(s)

# s.pop()    #随机删除一个
# print(s)
# s.clear()  #清空所有元素

#集合是有包含关系

# print(set('alex')== set('alexexex'))
# print(set('alex') < set('alexwww'))
#
# a=set([1,2,3,4,5])
# b=set([4,5,6,7,8])
# print(a.intersection(b))      #交集，都有的数据
# print(a & b)
#
# print(a.symmetric_difference(b)) #对称差集，交集取反
# print(a ^ b)
#
# print(a.union(b))            #并集，都加到一起，再去重 |
# print(a | b)
#
# print(a.difference(b))     #差集，a里面有的b没有
# print(a - b)

s=set(['xf','abc','hfy'])

print(s)
s.update('123')
print(s)

