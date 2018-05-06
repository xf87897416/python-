#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/1/30


from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)


p = Person(name='xf',shirt_size='L')
p.save()
print(p.shirt_size)
print(p.get_shirt_size_display())







