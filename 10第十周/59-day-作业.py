#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/19

import time
'''

CBV：
    Django:
        url -> def 函数    FBV
        url -> 类           CBV  
        
    注：chrome插件postman
    CBV：
        url -> 类.as_view()
        
        class Index(views.View):
            
            @...
            def dispatch(self,request, *arg, **kwarg):
                super...
            
            def get(self, request, *arg, **kwarg):
                pass
                
            ...
    总结：
        如果对某一种请求做处理：单一装饰器
        如果对请求做处理：      dispatch单一装饰器






'''