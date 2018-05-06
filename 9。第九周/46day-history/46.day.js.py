#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/3

import time
'''
-----------------history 对象-----------------------
三种方法：
    forward back go

一个属性：length


-----------------localtion------------------------------

<input type="button" value="重载" onclick="location.reload()"> 
location.href='http://www.baidu.com'


---------------------文档树导航属性-------------------------------

var ele=document.getElementById("div1");

    console.log(ele.nodeName);    DIV
    console.log(ele.nodeType);      
    console.log(ele.nodeValue);

    var ele2=ele.firstChild;    没意义
    var ele2=ele.lastChild;     没意义
    
    
    var ele2=ele.childNodes;   ****
    alert(ele2.nodeName);

    var ele3=ele.parentNode;    
    
    parentElement  父节点标签元素
    
    children    所有子标签
        
    firstElementChild   第一个子标签元素
    
    lastElementChild    最后一个子标签元素
    
    nextElementSibling  下一个兄弟标签元素
    
    previousElementSibling  上一个兄弟标签
    


--------------推荐用的是----------------------
var ele=document.getElementById("div1");
var ele2=ele.firstElementChild;
var ele3=ele.lastElementChild;

var ele_sons=ele.children;

for (var i=0;i<ele_sons.length;i++){
    console.log(ele_sons[i])
}

------------------------------------------------------
通过ID取，还有class取   标签名字   通过自定义name
class 是多个
var ele=document.getElementsByClassName("div2")[0];

var ele2=ele.nextElementSibling;
alert(ele2.innerHTML)
取的文档

var tag=document.getElementsByTagName("p");
    alert(tag[0].innerHTML);
    
----------------------------------------
var tag=document.getElementsByName("alex");

----------------------------------------

局部查找：TagName   ClassName
    var ele=document.getElementByClassName("div3")[0];
    ele.getElementsByTagName("p")[0]; 


=========================================================
事件驱动：
<input class="keyword" type="text" onfocus="func1()" onblur="func2()">

获取焦点，失去焦点触发

<select onchange="func3()">

onkeydown

onload  

window.onload=function(){
    var p=document.getElementById("id1")
    alert(p.nodeName);
}

-----------------------mouse----------------

onmousedown         点击触发

onmousemove         区域中移动就触发

onmouseout          离开区域

onmouseover         移动到区域触发


--------------------submit---------------------------
onsubmit="check()"  只能在form用
return false;    组织提交表单
两种绑定方式：
一：
    var Form=document.getElementById("form");
    Form.onsubmit=function (){
        alert(123);
        return false;
    }

二：
    function check(event){
        alert("验证失败");
        return false;
        event.preventDefault();
    }

三： 

 <form onsubmit="return check()">
    function check() {
        alert("验证失败");
        return false;
    }
==================================================

阻止向外传播  e.stopPropagation();

<div id="div1" onclick="alert('div1')">
    <div id="div2" onclick="func1(event)"></div>
</div>

function func1(e){
    alert('div2');
    e.stopPropagation();
    
}
==================================================
增删改查！！！！！

增：createElement(name)创建元素
    appendChild();将元素添加
    
删：获取
removeChild（）
innerText   只能解析文本与innerHTML类似

改：
var ele=document.getElementById("biger");
ele.classList.add("biger")
ele.classList.remove("biger")

查:    













'''




















