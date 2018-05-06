#_author: "Administrator"
#date: 2017/10/23

############################基本流程
#能调用方法的一定是对象！！！！
# li=[1,2,3]
# li.append('2')
# 'asc'.capitalize()

#三种基本的操作模式 r(只可读) w（只可写） a（追加）
#流程：1 创建文件对象 2 调用文件方法进行操作  3 关闭文件

# f=open('小重山2','r',encoding='utf8')
# f.write()#报错

# data=f.read(5)
# print(data)
# f.write('\nhello world \n')
# f.write('alex')
#
#注意：if not close,数据会缓存，而不是磁盘！
# time.sleep(30)
# f.close()


# f=open('123','r',encoding='utf8')
# #print(f.readline())
# # print(f.readlines())
# for i,v in enumerate(f.readlines(),1):
#     if i == 5:
#         v="".join((v.strip(),'添加的内容'))
#     print(v.strip())
# f.close()



################################具体操作方法

# number=0
# for i in f:#这是for内部将f对象做成一个迭代器，用一行去一行。
#     number+=1
#     if number == 6:
#         i = ''.join([i.strip(), 'iiiii'])  # 取代万恶的+
#     #     print(i.strip())
#     print(i.strip())


#truncate（）：截断数据(不能在r模式下)
#在w模式下：先清空，再写，再截断
#在a模式下：直接将指定位置后的内容截断
# f.truncate(5)
# f.write('hello world')
# f.truncate(5)
# f.close()


##### r+, w+, a+

# r+:光标默认在0位置，最后位置开始写
# w+:先清空，再写读
# a+:光标默认在最后位置


# f_r=open('123.txt','r',encoding='utf-8')
# f_w=open('test2.txt','w',encoding='utf-8')
# num=0
# for line in f_r:
#     num+=1
#     if num==5:
#         line="".join([line.strip(),'新的内筒\n'])
#     f_w.write(line)



# with open('log', 'r') as f:
#     f.readline()
#     f.read()
# print('hello')

#with 同时管理多个文件对象
# with open('log1','r') as f_read, open('log2','w') as f_write:
#     for line in f_read:
#         f_write.write(line)


