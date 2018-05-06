#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/10
'''
为什么加锁GIL还要加锁
各有各的功能
防止cpu切换导致数据不一致


'''
import threading
import time
def addNum():
    global num
    r.acquire()  #加锁
    temp=num
    time.sleep(0.00000001)
    num=temp-1
    r.release()     #解锁

num=100

thread=[]
r=threading.Lock()

for i in range(100):
    t=threading.Thread(target=addNum)
    t.start()
    thread.append(t)
for i in thread:
    i.join()

print('final num:',num)




