#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/13

import time
'''
http://www.cnblogs.com/yuanchenqi/articles/6083427.html
ORM对象关系映射
优点
1 ORM使得我们的通用数据库交互变得简单易行，
而且完全不用考虑该死的SQL语句。快速开发，由此而来。
2 可以避免一些新手程序猿写sql语句带来的性能问题。


缺点：1  性能有所牺牲，不过现在的各种ORM框架都在尝试各种方法，
比如缓存，延迟加载登来减轻这个问题。效果很显著。
2  对于个别复杂查询，ORM仍然力不从心，为了解决这个问题，ORM一般也支持写raw sql。



增加
创建单表方式一
from app01.models import * 

create 方式一 
    Author.objects.create(name="alvin",age="22")

create 方式二
    Author.objects.create(**{"name":'alex',"age":'22'})
!!!!!!!!推荐
save方式一
    author=Author(name='alvin')
    author.save()

save方式二
    author=Author()
    author.name="alvin"
    author.save()
    
如果有外键：
    一对一：OneToOne 通过一个Forignkey 约束unique
        unique=true
    一对多：
   models.Book.objects.create(title="python",price=12,publish_id=2)
   models.Book.objects.create(title="python",price=12,publish=obj)
    多对多：
    add()
    remove()
    book=models.Book.object.filter(id=2)[0]
    authors=models.Author.object.filter(id__gt=2)
    book.author.add(*authors)
    -------------------------------反向查询
    author=models.Autor.bojects.filter(id=3)[0]
    books=models.Book.objects.filter(id__ge=2)
    author.book_set.add(*books)
    
    
    
    
    
    
删除：
    Book.objects.filter(id=1).delete()

改：update和save
    author=Author.objects.get(id=5)#对象
    author.name="alvin"
    author.save()
    
    Publisher.objects.filter(id=2).update(name='American publisher')
    #不能用get（id=2）  集合
        !!!!!推荐

查：
    filter(**kwargs):
    all():
    get(**kwargs):

# 查询相关API：

#  <1>filter(**kwargs): 它包含了与所给筛选条件相匹配的对象

#  <2>all():         查询所有结果

#  <3>get(**kwargs):    返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。

#-----------下面的方法都是对查询的结果再进行处理:比如 objects.filter.values()--------

#  <4>values(*field):        返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列 model的实例化对象，而是一个可迭代的字典序列
                                     
#  <5>exclude(**kwargs):     它包含了与所给筛选条件不匹配的对象

#  <6>order_by(*field):      对查询结果排序

#  <7>reverse():             对查询结果反向排序

#  <8>distinct():            从返回结果中剔除重复纪录

#  <9>values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

#  <10>count():              返回数据库中匹配查询(QuerySet)的对象数量。

# <11>first():               返回第一条记录

# <12>last():                返回最后一条记录

#  <13>exists():             如果QuerySet包含数据，就返回True，否则返回False。


迭代器用多少拿多少
obj_set.iterator()


#--------------------对象形式的查找--------------------------
    # 正向查找
    ret1=models.Book.objects.first()
    print(ret1.title)
    print(ret1.price)
    print(ret1.publisher)
    print(ret1.publisher.name)  #因为一对多的关系所以ret1.publisher是一个对象,而不是一个queryset集合

    # 反向查找
    ret2=models.Publish.objects.last()
    print(ret2.name)
    print(ret2.city)
    #如何拿到与它绑定的Book对象呢?
    print(ret2.book_set.all()) #ret2.book_set是一个queryset集合

#---------------了不起的双下划线(__)之单表条件查询----------------
#    models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
#
#    models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
#    models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
#
#    models.Tb1.objects.filter(name__contains="ven")
#    models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
#
#    models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and
#
#    startswith，istartswith, endswith, iendswith,

---------->聚合查询和分组查询
from django.db.models import Avg,Min,Sum,Max
>>> Book.objects.all().aggregate(Avg('price'))
{'price__avg': 34.35}


<2> annotate(*args,**kwargs):
Book.objects.filter(authors__name='alex').values("title")

Book.objects.values("authors__name").annotate(Sum("price"))


--------->F查询和Q查询
# from django.db.models import F
# models.Tb1.objects.update(num=F('num')+1)

# Q 构建搜索条件
from django.db.models import Q

Book.objects.get(
        Q(title__startswith='P'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )

九 admin的配置

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
admin
admin123





注意base.html里面 导致无css
'''