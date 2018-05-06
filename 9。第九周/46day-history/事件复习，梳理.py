#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/4

import time
'''

History 对象属性
    back()    加载 history 列表中的前一个 URL。
    forward()    加载 history 列表中的下一个 URL。
    go()    加载 history 列表中的某个具体页面。



DOM 定义了访问 HTML 和 XML 文档的标准：
    *核心 DOM - 针对任何结构化文档的标准模型
    *XML DOM - 针对 XML 文档的标准模型
    *HTML DOM - 针对 HTML 文档的标准模型
    
    
节点(自身)属性:

    attributes - 节点（元素）的属性节点
    nodeType – 节点类型
    nodeValue – 节点值
    nodeName – 节点名称
    innerHTML - 节点（元素）的文本值
    导航属性:
    
    parentNode - 节点（元素）的父节点 (推荐)
    firstChild – 节点下第一个子元素
    lastChild – 节点下最后一个子元素
    childNodes - 节点（元素）的子节点


访问 HTML 元素（节点）,访问 HTML 元素等同于访问节点,我们能够以不同的方式来访问 HTML 元素：

    通过使用 getElementById() 方法 
    通过使用 getElementsByTagName() 方法 
    通过使用 getElementsByClassName() 方法 
    通过使用 getElementsByName() 方法 



HTML DOM Event(事件):
    onclick        当用户点击某个对象时调用的事件句柄。
    ondblclick     当用户双击某个对象时调用的事件句柄。
    
    onfocus        元素获得焦点。               //练习：输入框
    onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
    onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（三级联动）
    
    onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
    onkeypress     某个键盘按键被按下并松开。
    onkeyup        某个键盘按键被松开。
    onload         一张页面或一幅图像完成加载。
    onmousedown    鼠标按钮被按下。
    onmousemove    鼠标被移动。
    onmouseout     鼠标从某元素移开。
    onmouseover    鼠标移到某元素之上。
    onmouseleave   鼠标从元素离开
    
    onselect      文本被选中。
    onsubmit      确认按钮被点击。


<div id="abc" onclick="func1(this)">事件绑定方式1</div>
<div id="id123">事件绑定方式2</div>

var ele=document.getElementById("id123").onclick=function(){
         console.log(this.id);
        //jquery下是$(this), 这种方式不需要this参数;
    }


onload：
onload 属性开发中 只给 body元素加.
这个属性的触发 标志着 页面内容被加载完成.
应用场景: 当有些事情我们希望页面加载完立刻执行,那么可以使用该事件属性.



onsubmit:
是当表单在提交时触发. 该属性也只能给form元素使用.应用场景: 在表单提交前验证用户输入是否正确.如果验证失败.在该方法中我们应该阻止表单的提交.



改变 HTML 内容 
   改变元素内容的最简答的方法是使用 innerHTML ，innerText。

改变 CSS 样式 
<p id="p2">Hello world!</p>
document.getElementById("p2").style.color="blue";<br> 

var ele=document.getElementById("div1");
ele.classList.add("fontSize")  
 .style.fontSize=48px







'''



















































