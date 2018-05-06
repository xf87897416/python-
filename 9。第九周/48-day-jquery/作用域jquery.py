#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/5


import time


'''
js中函数先加载完，覆盖之前的函数，再执行


面试题:
for(var i=1;i<=9;i++){
    setTimeout( function timer() {
        console.log(i);
    },1000);
}

调用jquery!
<script src="/jquery-3.2.1.js"></script>

基本语法
$(selector)action()

$("*").css("color","red")
$("#div2").css("color","yellow")

组合选择器
$(".outer p").css("color","red")
$(".outer>p").css("color","red")  儿子层

$(".div li:first").css("color","red")
$(".div li:last").css("color","red")
$(".div li:eq(2)").css("color","red")
$(".div li:lt(2)").css("color","red")
$(".div li:gt(2)").css("color","red")

属性选择器:
    $("[alex]").css("color","red")
    $("[alex='lsb']").css("color","red")

表单选择器：
    $("[type='button']")------>$(":button")  只适用于input
    
    $("input:checked")

筛选器：

    $(".div1").children(".div3").css("color","red") 只找儿子层
    $(".div1").find(".div3").css("color","red")     儿子层都找

    $(".div2").next().css("color","red")   下一个
    $(".div2").nextAll().css("color","red")   下一级
    $(".div2").nextUntil(".div6").css("color","red")   下面直到div6
    
    $(".div2").prev().css("color","red")   上一个
    $(".div2").prevAll().css("color","red") 
    $(".div2").prevUntil("div8").css("color","red")

    $(".div2").parent().css('color','red');
    $(".div2").parents().css('color','red');  最外层
    $(".div2").parentsUntil('.div4').css('color','red');  

    $(".div2").siblings().css('color','red')



----------------示例-----------------
function show(self){
    $(self).next().removeClass("hide");
    $(self).parent().siblings().children('.con').addClass('hide');
}























'''
