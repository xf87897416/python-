#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/15


from multiprocessing import Process,Manager


def f(d,l,n):
    d[n]= '1'
    d['2']=2
    d[0.25]=None
    l.append(n)

if __name__ == '__main__':
    with Manager() as manager:
        d=manager.dict()

        l=manager.list(range(5))
        p_list=[]
        for i in range(10):
            p=Process(target=f,args=(d,l,i))
            p.start()
            p_list.append(p)

        for i in p_list:
            i.join()
        print(d)
        print(l)













