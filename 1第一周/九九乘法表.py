


print("打印99乘法表")
for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
     print (" ")



for i in range(1,10):
    for j in range(1,i+1):
        print(i, 'X', j, '=', i * j,end="  ")
    print(" ")
