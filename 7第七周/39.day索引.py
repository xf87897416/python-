#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/23

import time
'''
索引  种类
普通索引    加速查找
唯一索引    加速查找，单列数据不能重复
主键索引    加速查找，单列数据不能重复，不能为null
组合索引    
  联合唯一（两列可以一起）   多列可以创建一个索引
   非联合索引 


普通索引--------
1   CREATE INDEX 索引名字 ON table_name (column_list)
2   create table tb1(
ID auto_increment primary key,
name varchar(20),
index in1 (name)
)engine=innodb default charset=uft8
创建索引时查找块，但是空间变大，插入和删除时变慢
删除索引
DROP INDEX 索引名字 ON talbe_name
查看索引
show index from tb1;

唯一索引-------

1   CREATE UNIQUE INDEX index_name ON table_name (column_list)
2   create table tb1(
ID auto_increment primary key,
name varchar(20),
unique in1 (name)
)engine=innodb default charset=uft8

删除索引
DROP INDEX index_name ON talbe_name




主键索引-------
不能重复，不能为空
alter table 表名 add primary key(列名)
alter table 表名 drop primary key


组合索引----------
name，pwd 
普通组和索引：
    无约束
    name，pwd
联合唯一索引：
    有约束：
    name，pwd    
CREATE INDEX 索引名字 ON table_name (list1，list2)
查找：最左匹配


#################################################
1   覆盖索引
select * from tb where id =1
先去索引中找
再去数据表找

select id from where id <10
先去索引找
--情况应用上索引，并不用去数据表中操作，覆盖索引
--只需要在索引表中就能获得数据时

2   合并索引
id name（单独索引） email（单独） pwd


######################################################
通过EXPLAIN来分析索引的有效性：

EXPLAIN SELECT clause
获取查询执行计划信息，用来查看查询优化器如何执行查询；

输出：
id: 当前查询语句中，每个SELECT语句的编号；

    复杂类型的查询有三种：
        简单子查询；
        用于FROM中的子查询；
        联合查询：UNION；

    注意：UNION查询的分析结果会出现一外额外匿名临时表；

select_type：
    简单查询为SIMPLE
    复杂查询：
        SUBQUERY: 简单子查询；
        DERIVED: 用于FROM中的子查询；
        UNION：UNION语句的第一个之后的SELECT语句；
        UNION RESULT: 匿名临时表；

table：SELECT语句关联到的表；

type：关联类型，或访问类型，即MySQL决定的如何去查询表中的行的方式；
    ALL: 全表扫描；
    index：根据索引的次序进行全表扫描；如果在Extra列出现“Using index”表示了使用覆盖索引，而非全表扫描；
 -- range：有范围限制的根据索引实现范围扫描；扫描位置始于索引中的某一点，结束于另一点；
    ref: 根据索引返回表中匹配某单个值的所有行；
    eq_ref：仅返回一个行，但与需要额外与某个参考值做比较；
    const, system: 直接返回单个行；
从上往下性能最高


possible_keys：查询可能会用到的索引；

key: 查询中使用了的索引；

key_len: 在索引使用的字节数；

ref: 在利用key字段所表示的索引完成查询时所有的列或某常量值；

rows：MySQL估计为找所有的目标行而需要读取的行数；

Extra：额外信息

    Using index：MySQL将会使用覆盖索引，以避免访问表；
    Using where：MySQL服务器将在存储引擎检索后，再进行一次过滤；
    Using temporary：MySQL对结果排序时会使用临时表；
    Using filesort：对结果使用一个外部索引排序；
    
limit 

select * from toc where ID =5657 limit 1;    
效率更高
    
---sql:all,index,都是有优化的余地-----

range
对索引进行范围查找
对于！=  和>   不能走索引!!!!!!!!!!!!


#################################################

4 如何命中索引
id  name  ctime
            2016-9-10 11:57 

or    其中有一个不是索引就走不了
数据类型不一致也不走索引

！=  >   都不走  主键还是会走   数字走


order by  映射不是索引就不走
主键还是走


创建表时，char 代替varchar
定长往前放 ，变长后放
组合索引代替单个索引（经常使用多个条件查询时）

####指定列前几个字符创建索引
使用连接join ，来代替子查询（sub）

短索引  
alter table  aid_info add index aid(aid(4));
必需为char类型
'''



















