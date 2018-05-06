#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11

'''
event.isSet() :返回event的状态值
event.wait()  ：如果event.isSet()==False 将阻塞线程：
event.set()   ：设置even的状态值为True,所有阻塞池的线程激活进入就绪状态，
等待操作系统调度
event.clear()   :恢复event的状态值为False
'''
import threading,time
class Boss(threading.Thread):
    def run(self):
        print("大家今天晚上加班到22:00")
        event.isSet() or event.set()
        time.sleep(5)
        print("22:00，大家可以下班了，回家滚犊子吧")
        event.isSet() or event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("命苦啊，老板不是人")
        time.sleep(1)
        event.clear()
        event.wait()
        print("OhYeah,baby,终于下班了")

if __name__ == '__main__':
    thres=[]
    event=threading.Event()
    for i in range(5):
        thres.append(Worker())
    thres.append(Boss())
    for t in thres:
        t.start()
    for t in thres:
        t.join()























