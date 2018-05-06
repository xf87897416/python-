#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11

class Teacher():
    def __init__(self,teacher_name,teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_class={}
    def teacher_add_class(self,class_name,class_obj):
        self.teacher_class[class_name] = class_obj





