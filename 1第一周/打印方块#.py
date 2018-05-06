height=int(input("height:"))
width=int(input("weight:"))

num_h=0
while num_h <height:
    num_w=0
    while num_w<width:
        print("#",end="")
        num_w+=1
    print()
    num_h+=1
######################################
height=int(input("height:"))
width=int(input("width:"))


while height>0 :
    print(width*"#")
    height-=1