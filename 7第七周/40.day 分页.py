#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/24

import time

'''
分页
limit  x,m 扫表x+m
where id > 1000 直接跳过前1000
select * from tb1 where id >1000000 limit 1000000,10




慢日志
slow_query_log = ON
log_queries_not_using_indexes = ON
long_query_time = 0.2
slow_query_log_file = D:\slow.log

内存中直接修改配置信息

重重之重
'''
import pymysql
def sqlexec(last_nid, is_next):


    conn = pymysql.connect(host='192.168.0.10', port=3306, user='root', passwd='1234', db='hellodb', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行存储过程,获取存储过程的结果集，将返回值设置给了  @_存储过程名_序号 =
    if is_next:
        cursor.execute('select * from toc where ID>%s limit 10',last_nid)
        result = cursor.fetchall()
    else:
        cursor.execute('select * from toc where ID<%s order by ID desc limit 10', last_nid)
        result = cursor.fetchall()
        result = list(reversed(result))

    conn.commit()
    cursor.close()
    conn.close()
    return result

current_last_nid = 0
current__nid = 0
while True:
    p = input('1、上一页; 2、下一页\n')
    if p == '2':
        # 点击下一页
        is_next = True
        ret = sqlexec(current_last_nid, is_next)
    else:
        is_next = False
        ret = sqlexec(current_first_nid, is_next)
    current_first_nid = ret[0]['ID']
    current_last_nid = ret[-1]['ID']
    for i in ret:
        print(i)


