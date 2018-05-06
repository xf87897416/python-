#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/12

import time
'''
博客：http://www.cnblogs.com/yuanchenqi/articles/6083427.html


什么是模板语言？
    html+逻辑控制语句 

 示例
 def current_time(req):
    now=date.date.now()
    return render(req,"index.html",{current_date}:now)
 
 
 
 
 
 
1  {{变量}}
 
2  万能的句点号
可以拿方法，属性，值

3 {% if %}
{% endif %}


4  {% for i in obj reversed %}  反序
循环里面可以用{% if forloop.first %}    last
用来判断第一次是否为true，是就走
不是就else




{% for i in obj %}
    <p>{{ forloop.counter }}:{{ i }}</p>

{% endfor %}

5 过滤器
filter



addslashes   #给变量中的引号加斜线


{#{{ obj|upper }}#}
{#{{ obj|lower }}#}
{#{{ obj|first }}#}
{#{{ obj|capfirst }}#}

{{ obj|add:6 }}

{{obj|default:"空"}}


{% autoescape off %}
    {{ obj }}
{% endautoescape %}
{{ values|safe }}

告诉浏览器需要渲染


替换复杂变量名
{% with %}
{% with total=afasafafadfgafadfa %} {{ total}}
{% endwith %}

取消渲染 直接显示
{% verbatim %}
{{ name }}
{% endverbatim %}
---------------------------------------------------
---------------------------------------------------
自定义标签！！！！！！！！！！！！！！！！

在app下创建templatetags文件

创建文件my_tag
from django import template
from django.utils.safestring import mark_safe


INSTALLED_APPS =     'app01.apps.App01Config',


register= template.Library()  #register 是固定变量名，不能变
from django.utils.safestring import mark_safe


@register.filter
def my_add100(v1):
    return v1+100
#参数不能超过两个


#不能用if
@register.simple_tag
def my_add(v1,v2,v3):
    return v1+v2+v3

{% if forloop.counter|test:"3,1" %}



------------------------------------------
html页面
{% load my_tag %}

{% my_add100 4 %}

{{ num|my_add100 }}

{% my_add 12 34 56 %}




'''















