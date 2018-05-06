#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/18

import time
'''

Cookie：
就是保存在浏览器端的键值对
可以利用做登录

1、保存在用户浏览器
2、可以主动清楚
3、也可以被“伪造”
4、跨域名cookie不共享

5、浏览器设置不接受cookie

Cookie是什么？
客户端浏览器上保存的键值对！！！！！！！！！！
设置：
    服务端操作的Cookie
        obj.set_cookie('k1','v1')
        obj.set_cookie('k1','v1',max_age=10)
        
        v = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
        obj.set_cookie('k1','v1',max_age=10,expires=v)
    path: 
                    /       表示，全局生效
                    /xxxx/  表示，只有当前url生效
    domian:
                    obj.set_cookie('k4','v4',max_age=10,expires=v, domain='oldboy.com')
                    obj.set_cookie('k1','v1')
     httponly: 仅仅HTTP网络传输使用
    ======================
客户端浏览器上操作cookie
    $.cookie(k)取值
    $.cookie(k,v)设置值
    $.cookie('k','v'{'path':'/index.html'}) 设置值
    
    
    $.cookie(k)取值
            dom          --> 麻烦
            jquery插件   --> 
                                jquery.cookie.js
                                jquery.cookie.js
                            ...
                            expires: 
                                        10
                                        d = new Date()
                                        d.

http://www.cnblogs.com/wupeiqi/articles/5246483.html


Cookie的应用：
    登录认证
        普通cookie
            - 敏感信息（直接看到），不宜放置在cookie中，敏感信息放在数据库，频繁操作数据库
        签名的cookie
            - 敏感信息（可能会解密），
    
                                   
        不宜放置在cookie中，敏感信息放在数据库，频繁操作数据库
        
        ===========》 cookie时做认证时候，将不敏感的信息放在cookie中，频繁操作数据库 ===========


Session：
    session是服务器端的一个键值对
    session内部机制依赖于cookie
    
    request.session['k']
    request.session['k1'] = v
    request.session['k2'] = v
    
    del request.session['k1']
    request.session.clear()
    
    
    # 获取、设置、删除Session中数据
    request.session['k1']
    request.session.get('k1',None)







'''

































































