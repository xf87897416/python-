#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/23


import time

'''
事务：innodb


delimiter $$
create PROCEDURE p1(
    out p_return_code tinyint
)
BEGIN

    DECLARE exit handler for sqlexception
    BEGIN
        --ERROR
        set p_return_code = 1;
        rollback;
    END;    
    
    DEWCLARE exit handler for sqlwarning
    BEGIN
        --WARNING
        set p_return_code = 2;
        rollback;
    END;
    
    START TRANSACTION;
        DELETEfrom tb1;
        insert into tb2(name)values('senev');
    COMMIT;
    -- SUCCESS
    set p_return_code = 0;
END $$
delimiter;        

#################################################################
内置函数
char_length（srt）
返回长度

concat('xf','hello','world')
'xfhelloworld'

concat_ws('_','xf','nihao')  #自定义拼接符
'xf_nihao'

insert(str,pos,len,newstr)
select insert('alex',2,2,'G')
'aGx'


LEFT(str,len)
select left('alxe',2)
'al'

right(str,len)

locate(substr,str,pos)
select locate('ex','alexalex',1)
pos起始位置

REPEAT（str,count）
重复


substring（str,pos） substring（str,pos,len） 
select substring('aqwrezvluh',5)
'ezvluh'


select substring('aqwrezvluh',5,3)
ezv

select substring('aqwrezvluh',5,-3)
wre


reverse（）反转



trim('  alex ')  两边括号没有
trimleft（）
trimright（）


######################################################
自定义函数
delimiter $$
create function f1(
    i1 int,
    i2 int
)
returns int
BEGIN
    delcare num int;
    set num = i1 +i2;
    return(num)
END$$
delimiter;

函数里面不能获取结果集
######################################################

















'''






























