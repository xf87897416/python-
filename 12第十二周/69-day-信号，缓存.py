#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/1/16

import time
'''
django的生命周期：一个请求经过中间建到达url分发给views函数有cbv，fbv，
去数据库和模板拿数据库，经过渲染，得到一个字符串返回给用户。


中间件：


二：CSRF
    FORM提交：
    class Foo:
    def __init__(self, request,html):
        self.req = request
        self.html = html


    def render(self):
        return render(self.req,self.html)

    render
    {% csrf_token %}
    
    AJAX：提交
        cokie中提取随机字符串csrftoken对象的值
        设置请求头：
        XXOO：cookie
        
        
        
        
         $(function () {
         
             $(function () {
        $.ajaxSetup({
           beforeSend:function(xhr,settings) {
               xhr.setRequestHeader('X-CSRFToken',$.cookie('csrftoken'));
           }
        });#整体配置heads
         
         
         
        $('#btn').click(function () {
            $.ajax({
                url : '/index/',
                type:'POST',
                data : {username:'root'},
                headers:{'X-CSRFToken' :$.cookie('csrftoken')},
                success:function (arg) {
                    console.log(arg);
                }
            })
        });
    })
        
from django.views.decorators.csrf import csrf_protect
@csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。
@csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
        
    三缓存：
    
     # 此缓存将内容保存至内存的变量中
    # 配置：
        CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                'LOCATION': 'unique-snowflake',
            }
        }

    # 注：其他配置同开发调试版本
    
    
    
    Model signals
    pre_init                    # django的modal执行其构造方法前，自动触发
    post_init                   # django的modal执行其构造方法后，自动触发
    pre_save                    # django的modal对象保存前，自动触发
    post_save                   # django的modal对象保存后，自动触发
    pre_delete                  # django的modal对象删除前，自动触发
    post_delete                 # django的modal对象删除后，自动触发
    m2m_changed                 # django的modal中使用m2m字段操作第三张表（add,remove,clear）前后，自动触发
    class_prepared              # 程序启动时，检测已注册的app中modal类，对于每一个类，自动触发
Management signals
    pre_migrate                 # 执行migrate命令前，自动触发
    post_migrate                # 执行migrate命令后，自动触发
Request/response signals
    request_started             # 请求到来前，自动触发
    request_finished            # 请求结束后，自动触发
    got_request_exception       # 请求异常后，自动触发
Test signals
    setting_changed             # 使用test测试修改配置文件时，自动触发
    template_rendered           # 使用test测试渲染模板时，自动触发
Database Wrappers
    connection_created          # 创建数据库连接时，自动触发
    
    使用需注册
    from django.core.signals import request_finished
    from django.dispatch import receiver

    @receiver(request_finished)
    def my_callback(sender, **kwargs):
        print("Request finished!")
        
    
    
    
    
    
    
http://www.cnblogs.com/wupeiqi/articles/5246483.html


bootstrap（模板）--响应式+模板
    集成 css，js一个文件夹
v3.bootcss.com
多看
自己改一个后台，前端
！！！！！！！！！


响应式，根据窗口变大而不同
@media
·

'''