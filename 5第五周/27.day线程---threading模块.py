#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/9

'''
Cpython里面有GIL  同一时刻只有一个线程能执行   锁
在python里：
  if 任务是IO密集型的 可以用多线程
         是计算密集型的，sorry 改C

进程里面包含多个线程
每个线程可以共享数据
区别是： 共享数据，创建开销，能否通信，互相操作

'''
from time import sleep,ctime
import threading
def music(func):
    print(threading.current_thread())
    for i in range(2):
        print("开始听%s .%s"%(func,ctime()))
        sleep(2)
        print('结束听%s'%ctime())

def move(func):
    print(threading.current_thread())
    for i in range(5):
        print("开始看%s .%s"%(func,ctime()))
        sleep(2)
        print("结束看%s"%ctime())
threads=[]
t1=threading.Thread(target=music,args=("七里香",))
threads.append(t1)
t2=threading.Thread(target=move,args=("阿甘正传",))
threads.append(t2)


if __name__ == '__main__':
    # t2.setDaemon(True)

    for t in threads:
        t.setDaemon(True)
        t.start()
    # t.join()
    print(threading.current_thread())
    print(threading.active_count())  #看存活进程数量
    print("所有的事情都做完了 %s"%ctime())

#守护谁，就不要等谁，等别的执行完


















