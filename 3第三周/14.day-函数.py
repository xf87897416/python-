#_author: "Administrator"
#date: 2017/10/25

# def loger(time):
# 	f = open('123','a',encoding='utf8')
# 	f.write("\ndate is %s" % time )
# 	print(time)
# loger("2:50")
#简单的函数调用
#函数的作用： 减少重复代码
             #方便修改，易扩展，保持代码一致性


#关键字参数                  形参，实参
# def info_p(name,age,sex='male'):      #默认参数
# 	print('name is %s'%name)
# 	print('age is %d' % age)
# 	print('sex is %s' % sex)
# info_p(age=18,name='xf',sex='female')


# def add(*args):
# 	sum=0
# 	for i in args:
# 		sum += i
# 	print(sum)
# add(1,5,8)


#默认参数   关于不定长参数：args必须放左边，kwargs放右边，默认参数放最左边
# def info_p(**kwargs):
# 	for i in kwargs:
# 		print('%s:%s'%(i,kwargs[i]))
#
# info_p(name='xf',age=18,sex='male')

# def info_p(sex='male',*args,**kwargs):
# 	print(args)
#
# info_p(1,2,34,'female')  #1 传给sex了
# 优先级
# def info_p(name,age=22,*args,**kwargs):


# ab=[1,2,3]
#
# def f(*args):
#     print(args)
# f(*ab)

#将列表的值分别传给args 用*















