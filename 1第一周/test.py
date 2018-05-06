


f_r=open('123.txt','r',encoding='utf-8')
f_w=open('test2.txt','w',encoding='utf-8')
num=0
for line in f_r:
    num+=1
    if num==5:
        line="".join([line.strip(),'新的内筒\n'])
    f_w.write(line)


