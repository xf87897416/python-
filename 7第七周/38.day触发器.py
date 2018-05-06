#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/22
import time
'''
插入前
delimiter $$
create trigger insert_before_students BEFORE INSERT ON classes FOR EACH ROW
    insert into teachers(name) values('charu1');
END $$
delimiter ;
########################
after 后
########################################################

create trigger tri_before_insert_classes BEFORE INSERT on classes FOR EACH ROW
BEGIN
    if new.name == 'alex' then
        insert into teachers(name) values(NEW.name)
    endif 
end$$


OLD.name  #删除时用
NEW 新传入的值
OLD 原来的值



删除整个表，触发器会每一行都执行一遍
'''













