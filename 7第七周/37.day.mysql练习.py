#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/21



'''

sum(case when student.score > 60 then 1 else 0 END)/count(course_id)


select (select count(1) from students where Gender='M') as man,(select count(1) from students where Gender='F') as wumen;

视图  create view v1 as sql语句
        相当于快捷方程式  零食表，
    drop view v1;


存储过程
    c1=>  sql
    call c1()
    ########
    delimiter $$     #终止符换为$$
    create procedure p1()
    BEGIN
    select * from test;
    END$$
    delimiter ;

pymysql 中执行函数
cursor.callproc('p2')

drop procedure p1
删除
################################################
declare 在存储过程内部声明变量时，必须使用
delimiter $$
create procedure p1(
     in  i1 int,
     in  i2 int,
     inout i3 int,
     out r1 int
)
BEGIN
    DECLARE temp1 int;
    DECLARE temp2 int default 0;

    set temp1 = 1 ;

    set r1=i1 + i2 + temp1 + temp2 ;

    set i3 = i3 +100;

    select * from table;
end$$
delimiter ;
存储过程会返回两个，一个是数据集，一个是返回值
################################################






触发器


函数


索引


















'''



















































