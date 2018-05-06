


num=1

while num<=3 :
    name=str(input("your name：" ))
    password=str(input("your password："))
    if name=="xf" and password=="123456":
        print("欢迎登陆！！")
        break
    else:
       print("输入错误！请重新输入")
       num=num+1
else:
      print("帐户密码被锁定！！")
