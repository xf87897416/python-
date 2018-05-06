from django.db import models

# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(max_length=32)
    d_2_c = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Video(models.Model):
    lv = models.ForeignKey(Level)
    cg = models.ForeignKey(Category)

    title = models.CharField(verbose_name='标题', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=32)
    img = models.ImageField(verbose_name='图片', upload_to='./static/images/Video/')
    href = models.CharField(verbose_name='视频地址', max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title