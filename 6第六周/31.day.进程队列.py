#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/15

# from  multiprocessing import Process,Queue
# def f(q):
#     q.put([42,2,'hello'])
#     print("sub id :", id(q))
# if __name__ == '__main__':
#     q=Queue()
#     p_list=[]
#     print("main id :",id(q))
#     for i in range(3):
#         p=Process(target=f,args=(q,))
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     for i in p_list:
#         i.join()

################################################

from multiprocessing import Process,Pipe

def f(conn):
    conn.send("约吗")
    conn.send("约吗")
    print(conn.recv())
    conn.close()

if __name__ == "__main__":
    parent_conn,child_conn=Pipe()
    p=Process(target=f,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("约你老母")



















