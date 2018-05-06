#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/15



from multiprocessing import Process
import time

# def name(name):
#     time.sleep(1)
#     print("hello %s%s"% (name,time.ctime()))
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p=Process(target=name,args=('xf',))
#         p_list.append(p)
#         p.start()
#     for p in p_list:
#         p.join()
#     print("end")
##################################################
class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    def run(self):
        time.sleep(1)
        print("hello",self.name,time.ctime())
    
if __name__ == '__main__':
    p_list=[]
    for i in range(3):
        p=MyProcess()
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    print("end")











