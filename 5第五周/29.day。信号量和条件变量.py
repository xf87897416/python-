#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11
import threading
import time
from random import randint
# semaphore=threading.BoundedSemaphore(5)
#限制车辆
# class myThread(threading.Thread):
#     def run(self):
#         if semaphore.acquire():
#             print(self.name)
#             time.sleep(3)
#             semaphore.release()
#
# if __name__ == '__main__':
#     semaphore=threading.BoundedSemaphore(5)
#     thrs=[]
#     for i  in range(23):
#         thrs.append(myThread())
#     for i in thrs:
#         i.start()

#条件变量就是一把锁  wait（）notify（），notifyAll（）
##################################
####条件变量，可以等待限制线程，
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            print('生产者',self.name,':Append'+str(val),L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()
            if len(L)==0:
                lock_con.wait()
                print('ok')
            print("消费者",self.name,"Delete"+str(L[0]),L)
            del L[0]
            lock_con.release()
            time.sleep(0.25)

if __name__ == '__main__':
    L=[]
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()

