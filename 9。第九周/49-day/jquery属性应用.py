#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/6

import time
'''
for 循环

    dic={'name':'alex','age':'45'}
    li=[10,20,30,40]
    $.each(dic,function(i,x) {
        console.log(i,x);
    })

    $("table tr").each(function(){
        console.log($(this).html());
    })

$(:test).val()    #value()
内部插入
var ele=$("p")
$("#div1").append(ele)    一个是用父亲标签插入
ele.appendTo($("#div"))   一个是用子集标签被插入  

prepend   向上插入
prependTo
外部插入
after
before

---------------------------------
clone

empty   清空
remove   删除标签
 

后台管理布局：
absoulte  +   overflow:auto

.scrollTop()   设置滚轮高度

$(..).offset()    #获取当前标签距离文档顶部的高度
$(..).height()   #自身高度
$(..).innerHeight()   自身加2倍padding
$(..).outerHeight(false)   自身加2倍padding 2倍边框 
$(..).outerHeight(true)   自身加2倍padding 2倍边框 +2倍margin


'''