#_author: "Administrator"
#date: 2017/10/27
#闭包 如果在一个内部函数，对外部作用域的变量进行引用，
# name内部函数就被认为是闭包
def outer():
    x=10
    def inner():
        print(x)
    return inner

# outer()()
# f=outer()
# f()
#关于闭包=内部函数+定义函数时的环境































