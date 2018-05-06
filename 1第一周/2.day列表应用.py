#_author: "Administrator"
#date: 2017/10/20


#a=['wuchao','jinxin','xiaohu','sanpang','ligang',['wuchao','jinxin'],'licai']
# print(a[1:])#取到最后
# print(a[1:-1])#取到倒数第二值
# print(a[1:-1:1])#从左到右一个一个去取
# print(a[1::2])#从左到右隔一个去取
#print(a[3::-1]) #倒着取
#print(a[-1::]) #最后一个

#添加 append insert
# a.append('xuepeng')  #默认插入最后一个
# print(a)
# a.insert(2,'nihao')  # 插入任意位置
#print(a)

#修改
#a[1:3]=['haidilao','dahu']
#print(a)

#删除 remove pop del     remove删除内容    pop根据索引删除，可以得到删除值    del 从内存中删除变量
#a.remove('wuchao')
# print(a)
# a.pop(1)
# print(a)
# del a[0:2]
# print(a)

###########################################################
# t=['to','be','or','not','to','be'].count('to')   #计算元素出现次数
# print(t)


#entend    将一类表追加另一列表中
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
#
# print(a)
# print(b )

# a=['wuchao','jinxin','xiaohu','sanpang','ligang',['wuchao','jinxin'],'licai']
#
# print(a.index('wuchao'))

# reverse   倒着取
#a=['wuchao','jinxin','xiaohu','sanpang','ligang','licai']
# a.reverse()
# print(a)

#sort   排序
a=[4,7,5,9,6,1]
a.sort(reverse=True)
print(a)










