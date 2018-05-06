#猜年龄

age=58
guess=int(input("踩一下年龄吧，范围是1-100："))
while guess!=58:
    print("不好意思猜错了")
    if guess>age:
        print("猜大了")
    else:
        print("猜小了")
    guess=int(input("请重新输入："))
print("恭喜你猜对了")    
