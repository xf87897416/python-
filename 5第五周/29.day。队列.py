#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11


import queue

d=queue.Queue(3)

d.put('1',0)
d.put('2',0)
d.put('3',0)
# d.put('4',0)
print(d.get())
print(d.get())
print(d.get())
# print(d.get(0))

# size=d.qsize()  #剩余几个空间
# print(size)
# full=d.full()  #看空间是不是填满数据
# print(full)
# empty=d.empty()
# print(empty)     #一个数据没有就是True















