max=0
num1=int(input("请输入第一个值"))
num2=int(input("请输入第二个值"))
num3=int(input("请输入第三个值"))
for num in (num1,num2,num3):
     min=num
     for i in ((num1,num2,num3)):
        if i <min:
            min=i
        elif num>max:
            max=num

print("最小值为：",min)
print("最大值为：",max)

#################################################


