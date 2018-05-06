
name=input("Name:")
age=input("Age:")
job=input("Job:")

if age.isdigit():
    age=int(age)
else:
#    print("age must be digit")
    exit("age must be digit")
msg='''
----------info of %s -------
Name: %s
Age:  %s
Job:  %s
you will be retried in 5 yesar
---------end ---------------
'''   %  (name,name,age,job,)
print(msg)
