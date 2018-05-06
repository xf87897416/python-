#_author: "Administrator"
#date: 2017/10/20
flag = False
for i in range(10):
    if i<5:
        continue
    print(i)
    for j in range(10):
        print("layer2",j)
        if j == 6:
            flag=True
            break
    if flag:
         break