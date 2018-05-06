#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/20


'''

mysqldump -uroot -p123 数据库名称》路径   #结构+数据
mysqldump -uroot -p123 -d 数据库名称》路径   #结构

select DISTINCT * from 表 where num <60
去重，不用group by 了


python3 -m pip install --upgrade pip

python3 -m pip3 install pymysql



'''


import pymysql
conn=pymysql.connect(host='192.168.0.10',port=3306,user='root',passwd='1234',db='userinfo')

#创建游标
# cursor=conn.cursor()
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)  #字典了
#执行sql，并返回影响行数
# effect_row=cursor.execute("create table tb3(id int not null,name varchar(20))")
# print(effect_row)#受影响的行数
name=input("请输入名字").strip()
password=input("请输入密码").strip()
sql='''insert into user(name,password) values(%s,%s)'''

effect_row=cursor.execute(sql,('test2','123'))


# l=[
#     ('abc'),
#     ('asd'),
#     ('gagg'),
# ]
# effect_row=cursor.executemany("insert into tb1(name) values(%s)",l)

# r=cursor.execute("select * from tb1")

# print(r)


#查询
#fetchall 拿到元组（一条数据），fetchone  就是一个数据
# result=cursor.fetchall()
# print(result)

# result=cursor.fetchone()
# print(result)

# cursor.scroll(0,mode='absolute')   #绝对回到0

# cursor.scroll(1,mode='absolute')   #相对位置1 往下走一个  -1 往上走一个

# result=cursor.fetchone()  #迭代器  指针
# print(result)

# result=cursor.fetchmany(3)
# print(result)

# conn.commit()
#关闭游标

# conn.close()


'''
sql注入攻击
sql="select username,password from userinfo where username='%s' and password='%s'"
sql=sql %('alex',123)
#####sql=sql %('alex " -- ',123)
#####sql=sql %('alex" or 1=1 -- ',123)
cursor.execute(sql)
result = cursor.fetchone()
print(result)

'''

# l=(
#     ('abc'),
#     ('asd'),
#     ('gagg'),
# )
# cursor=conn.cursor()
# r=cursor.executemany("insert into tb1(name) values(%s)",l)

# cursor.execute('select * from students')
# result=cursor.fetchall()
# print(result)


# nid=cursor.lastrowid  #最后一个自增id
# print(nid)
conn.commit()
cursor.close()



