#_author: "Administrator"
#date: 2017/10/20
list=[
    ('xiaomi',2000),
    ('iphone',6000),
    ('honor',3500),
    ('pen',30),
    ('desk',50),
    ('computer',4600),
]
money=input("请输入money:")
shopping_car=[]
if money.isdigit():
    money=int(money)
    while True:
        for i,v in enumerate(list,1):
            print(i,'>>>',v)
        chose=input("请选择商品，quit退出：")
        if chose.isdigit():
            chose=int(chose)
            if chose > 0 and chose <= len(list):
                p_item=list[chose-1]
                if p_item[1]>money:
                    print("余额不足：还剩%s"%money)
                else:
                    money-=p_item[1]
                    shopping_car.append(p_item)
            else:
                print("编码不存在")

        elif chose=='quit':
             print("----您购买商品如下------")
             for i  in shopping_car:
                print(i)
             print("余额为%s"%money)
             break
        else:
            print("错误输入")
#################################################
#简易版
list=[
    ('xiaomi',2000),
    ('iphone',6000),
    ('honor',3500),
    ('pen',30),
    ('desk',50),
    ('computer',4600),
]
flg=False
money=int(input("请输入money:"))
shopping_car=[]
while not flg:
    for key,v in enumerate(list,1):
        print(key,'>>>',v)
    chose = input("(quit:退出)>>>:").strip()
    if chose.isdigit():
        chose=int(chose)
        p_item = list[chose-1]
        if p_item[1] > money:
            print("余额不足：还剩%s" % money)
        else:
            money -= p_item[1]
            shopping_car.append(p_item)
    elif chose =='quit':
        print("您购买以下商品".center(20,'-'))
        for i in shopping_car:
            print(i)
        print("还剩%s" % money)
        flg=True






