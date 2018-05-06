#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/25

import socket

def main():
    socket = socket.socket()
    socket.bind(('localhost',8000))
    socket.listen(3)

    while True:
        connection,address=socket.accept()

'''
标签
<!DOCTYPE html>   #一般模式
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="keywords" content="IT,技术，开源，网站">
        <meta name="description" content="博客园是一个开源大型网站。。。">
        <meta http-equiv="Refresh" content="2;URL=https://www.baidu.com">
        <meta http-equiv="Refresh" content="2;>  #刷新 ！
        <title>标题1</title>   ！
        <link rel="icon" href="hero1.png">  ！  开头小图标
    </head>

    <body>
        <h1></h1>    #块级标签
        <h2></h2>
        <h3></h3>
        ....
        <h6></h6>
        
        
        <br/>    #换行
        意识地下双
        <p></p>    #隔一行   #块级标签
        <hr>       #水平线
        <div>hello world</div>   #自定义，原始空白 块级标签！ 自动换行
        <span></span>            #内敛标签，对当前范围有效
        
        <b>给字体加粗</b>
        <em>变成斜体</em>    
        
        <strike>去除线</strike>
        <del>去除线</del>
        
        2<sub>3</sub>       下角标
        2<sup>3</sup>       上角标
        
        hello&nbsp;&nbsp;world   #特殊符号，空格
        
        &lt;h1&gt;          #lt 小鱼  gt大于
        
        <img src="hero1.png" width="200px" height="200px" alt="hehe" title="大美女">
        
        <a href="https://www.baidu.com" target="_blank">百度</a>  #超链接  锚
        #target 新打开页面跳转
        title  鼠标悬浮显示
        
        
        <a href="#div1">第一张</a>
        <a href="#div2">第二张</a>
        <a href="#div3">第三张</a>
        
        
        <div id="div1">第一张</div>
        <div id="div2">第二周</div>
        <div id="div3">第三章</div>
        
        
    </body>  

<\html>

所有标签都分为块级标签，和内敛标签
div   块
span  内敛

table  
        border 表格边框
        cellpadding 内边距
        cellspacing 外边距
        width 
        <tr> table row
        <th> :table head cell
        <td>
        
overflow: hidden;


'''