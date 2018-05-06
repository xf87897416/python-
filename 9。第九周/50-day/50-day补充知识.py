#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/7
import time

'''

#div1:after{
    content:'。'
    clear:both
    visibility:hidden;
    height:0;
    display: block;
}
通用


visibility:hidden;   隐藏文字
height:0


重要：浮动
一：已知外层高度
    内元素浮动
    
二：未知外层高度
    原始：最底未知<div style="clear:both;"></div>    
    牛逼：
    .clearfix:after{
        content:'。'
        clear:both
        visibility:hidden;
        height:0
    }

    <div class='clearfix'>
        <div>123</div>
        <div>123</div>
        <div>123</div>
        <div>123</div>
    </div>


JavaScript-----函数被调用前，先生成作用域链，一层层往外找------
会先覆盖上一层变量
 
  xo='alex';
    function f1() {
        var xo='eric';
        function f2() {
            console.log(xo);
        }
        return f2
    }
    var xxxx=f1();
    xxxx()

答案eric
---------------------------------

JavaScript  会声明提前变量var ox；var a；

五种基本数据类型
number
undefined
string
boolean
Null

["1", "2", "3"].map(parseInt);
结果 [1, NaN, NaN]

json类型的字符串转换为json对象及取值

var jsonString = '{"bar":"property","baz":3}';

var jsObject = JSON.parse(jsonString);    //转换为json对象
alert(jsObject.bar);    //取json中的值

var st = JSON.stringify(jsObject); //转换为json类型的字符串
------------------------------------------------
//json数组类型字符串取值
var jsonStr = '[{"id":"01","open":false,"pId":"0","name":"A部门"},{"id":"01","open":false,"pId":"0","name":"A部门"},{"id":"011","open":false,"pId":"01","name":"A部门"},{"id":"03","open":false,"pId":"0","name":"A部门"},{"id":"04","open":false,"pId":"0","name":"A部门"}, {"id":"05","open":false,"pId":"0","name":"A部门"}, {"id":"06","open":false,"pId":"0","name":"A部门"}]';
var jsonObj = JSON.parse(jsonStr);//转换为json对象
for(var i=0;i<jsonObj.length;i++){
    alert(jsonObj[i].id); //取json中的值
}
console.log(jsonObj)
var jsonStr1 = JSON.stringify(jsonObj)
console.log(jsonStr1+"jsonStr1")

-----------------------------------------------

var 声明变量局部变量


document.write  和innerHTML
范围不同
DOM的innerHTML是DOM元素对象的一个属性
而write是document对象的一个方法

7.jQuery  
预加载代码
========================
 $(document).ready(function () {
        //代码
    })
=================   
简写方式
$(function () {
        alert(123)
    })
    
普通绑定事件是bind简写：
    后添加的标签不会绑定
    
事件委托：    
$("ul").on("click","li",function(){
    alert(123);
})    


function myHandler(e){
    alert(e.data.foo2);
    }
$("p").on("click",{foo2:"bar"},myHandler)


=================================================
jQuery扩展方法：
$.extend({
    getmax:function (a,b){
        return a>b:a:b
    }
});

alert($.getmax(5,8))

---------------第二种-----------------------

$.fn.extend({
    print:function(){
        console.log($(this).html() )
    }
})
    $("p").print();
==============第三种，推荐==============================

（function (){
    $.fn.extend({
    print:function(){
        console.log($(this).html())
    }
});
}）();

$("p").print();














'''