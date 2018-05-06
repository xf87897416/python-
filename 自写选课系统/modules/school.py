#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/11

from modules.course import Course
from modules.classes import Class
from modules.teacher import Teacher
from modules.student import Student

class School():
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course={}
        self.school_teacher={}
        self.school_class = {}
        # self.school_student = {}

    def create_course(self, course_name, course_price, course_time):
        course_obj=Course(course_name, course_price, course_time)
        self.school_course[course_name]=course_obj

    def show_course(self):
        for key in self.school_course:
            course_obj = self.school_course[key]
            print("课程：%s\t价格：%s\t 周期：%s 月" % (course_obj.course_name,course_obj.course_price,course_obj.course_time))

    def create_class(self,class_name,courese_obj):
        class_obj=Class(class_name,courese_obj)
        self.school_class[class_name]=class_obj

    def show_class(self):
        for key in self.school_class:
            class_obj=self.school_class[key]
            print("班级：%s\t关联课程：%s" % (class_obj.class_name,class_obj.class_course.course_name))

    def show_class_course(self):
        for key in self.school_class:
            class_obj=self.school_class[key]
            course_obj=class_obj.class_course
            print("班级：%s\t关联课程：%s\t价格：%s\t周期：%s月"%(class_obj.class_name, course_obj.course_name,course_obj.course_price,course_obj.course_time))

    def create_teacher(self,teacher_name,teacher_salary,class_name,class_obj):
        teacher_obj=Teacher(teacher_name,teacher_salary)
        teacher_obj.teacher_add_class(class_name,class_obj)
        self.school_teacher[teacher_name]=teacher_obj

    def update_teacher(self,teacher_name,class_name,class_obj):
        teacher_obj = self.school_teacher[teacher_name]
        teacher_obj.teacher_add_class(class_name, class_obj)

    def show_teacher(self):
        for key in self.school_teacher:
            teacher_obj=self.school_teacher[key]
            class_list=[]   #一个老师有多个班级列表
            for i in teacher_obj.teacher_class:
                class_list.append(i)
            print("讲师：%s\t薪资：%s\t关联班级：%s" %(teacher_obj.teacher_name, teacher_obj.teacher_salary,class_list))

    def create_student(self,student_name,student_age,class_choice):
        student_obj=Student(student_name,student_age)
        class_obj=self.school_class[class_choice]
        class_obj.class_student[student_name] = student_obj
        self.school_class[class_choice]=class_obj

    def show_teacher_classinfo(self,teacher_name):
        teacher_obj=self.school_teacher[teacher_name]
        for i in teacher_obj.teacher_class:
            class_obj=self.school_class[i]
            student_list=[]
            for k in class_obj.class_student:
                student_list.append(k)
            print("班级：%s\t关联课程：%s\t学员:%s"%(class_obj.class_name,class_obj.class_course.course_name,student_list))



