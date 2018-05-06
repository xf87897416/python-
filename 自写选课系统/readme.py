#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11

import os

# class Student():
#     def __init__(self,student_name,student_age):
#         self.student_name=student_name
#         self.student_age=student_age
#
# class Course():
#     def __init__(self,course_name,course_price,course_time):
#         self.course_name=course_name
#         self.course_price=course_price
#         self.course_time=course_time
#
# class Class():
#     def __init__(self,class_name,course_obj):
#         self.class_name=class_name
#         self.course_obj=course_obj
#         self.student={}
#
# class Teacher():
#     def __init__(self,teacher_name,teacher_salary):
#         self.teacher_name = teacher_name
#         self.teacher_salary = teacher_salary
#         self.teacher_class=[]
#     def teacher_add_class(self,class_name,class_obj):
#         self.teacher_class[class_name]=class_obj
#
# class School():
#     def __init__(self,school_name,school_addr):
#         self.school_name = school_name
#         self.school_addr = school_addr
#         self.school_course={}
#         self.school_teacher={}
#         self.school_class = {}
#         # self.school_student = {}



import pickle


class course:  # 课程类：老师类和学生类 都有课程 所以称为组合关系
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

class Person:  # 人类：老师和学生类 的父类  ，他们之间的关系称为 继承
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

class Teacher(Person):  # 老师类人类的派生类：派生了level 职业等级，也继承了父类 人类的 姓名，年龄，课程 属性
    def __init__(self, name, age, course, level):
        Person.__init__(self, name, age, course)
        self.level = level

        # def __init__(self,name,age,course):   #继承了父类 减少了代码
        #     self.name=name
        #     self.age=age
        #     self.course=course

class Students(Person):  # 学生类：派生了ID属性 学生ID，同时也继承了父类人类的 姓名，年龄，课程 属性
    def __init__(self, name, age, course, id):
        # Person.__init__(self, name, age, course)
        super(Students, self).__init__(name,age,course)
        self.id = id
        # self.name = name
        # 继承了父类 减少了代码
        # self.age = age
        # self.course=course
        # self.age = age #self.course=course



python_obj = course('python', 15800, '7m')
t = Teacher('egon', 34, python_obj, '高级讲师')
s = Students('张根', 24, python_obj, 8668)
print('''%s正在学习%s课程 价格：%s 周期：%s 他的学生ID：%s %s正在教%s课程 价格：%s 周期：%s 他的教师职称：%s''' % (
s.name, s.course.name, s.course.price, s.course.time, s.id, t.name, t.course.name, t.course.price,
t.course.time, t.level))

linux_obj=course('linux',6000,'6m')
s2=Students('熊蜂',22,linux_obj,9588)
print('''%s正在学习%s课程 价格：%s 周期：%s 他的学生ID：%s %s正在教%s课程 价格：%s 周期：%s 他的教师职称：%s''' % (
s2.name, s2.course.name, s2.course.price, s2.course.time, s2.id, t.name, t.course.name, t.course.price,
t.course.time, t.level))

























