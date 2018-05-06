#_author: "Administrator"
#date: 2017/10/28

login_status=False
def outer(flg=''):
    def auth(func):
        def login(*args,**kwargs):
            global login_status
            count=0
            while count<=2:
                if login_status:
                    func(*args,**kwargs)
                else:
                    name=input("your name :").strip()
                    passwd=input("your passwd:").strip()
                    with open('登录文件.txt','r',encoding='utf-8') as f:
                        line=f.readline()
                    my_dic = eval(line)
                    if name ==my_dic['name'] and passwd ==my_dic['password']:
                        func(*args,**kwargs)
                        login_status=True
                        count=4
                    else:
                        print("your input not exists")
                        count+=1
                    if flg=='jd':
                       print("is jd")

        return login
    return auth

@outer()
def home(*args,**kwargs):
    if len(args)!=0:
     print("this is %s %s"%args)
    else:
        print("请输入2个数字")
home(1,2)


























