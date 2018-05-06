#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/15
import time
'''
ajax优点
    局部刷新
    异步传送  发一个请求，无需等待回复，可以发第二个   
    异步传送  发一个请求，无需等待回复，可以发第二个   

缺点，请求数多，良多，对服务器压力大
兼容性


1，基于JS的ajax的实现
    1 var xmlhttp=XMLHttprequest()
    2   xmlhttp.open("")
    3, xmlhttp.send("name=alex")
    4,监听xmlhttp(if ==4:{var context=xmlhttp.responetext})

2，JSON和JSONP
    $.getScript('test.js',function(){
        alert(add(1,6))
    
    }) 绑定事件时再提交，及时加载
    
    $.getJSON()
  
3，基于jquery的ajax的实现  
------------------------------------
$.ajax({
    url:'/juqery_test/',

})

$.ajax('url',{})

----------------------------------------
$.ajax({
    url:'',
    type:'POST',
    data:{}

})


JSON和XML比较
可读性：XML
解码难度：JSON简单
流行度：最开始就是XML，ajax中JSON更好 


1 同源策略机制
所谓同源是指，域名，协议，端口相同。
不同源的客户端脚本(javascript、ActionScript)在没明确授权的情况下，
不能读写对方的资源。



 2 ,JSONP是JSON with Padding的略称。
 可以让网页从别的域名（网站）那获取资料，即跨域读取数据。
 !!!!!!!!!!!!!
 由于浏览器具有同源策略，所以发跨域请求发布过去，依赖于JSONP
 script src不收同源策略约束，所以动态生成script
 
 

<script type="text/javascript" src="/static/jquery-2.2.3.js"></script>

<script type="text/javascript">
   $.ajax({
        url:"http://127.0.0.1:8002/get_byjsonp",
        dataType:"jsonp",            //必须有，告诉server，这次访问要的是一个jsonp的结果。
        jsonp: 'callbacks',          //jQuery帮助随机生成的：callbacks="wner"
        success:function(data){
            alert(data)
        }
   });

</script>
 #-------------------------------------http://127.0.0.1:8002/get_byjsonp
def get_byjsonp(req):

    callbacks=req.GET.get('callbacks')
    print(callbacks)                 #wner  

return HttpResponse("%s('yuan')"%callbacks)





















'''