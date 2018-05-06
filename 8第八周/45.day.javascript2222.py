#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/1

import time

'''
typeof只能判断基本数据类型

instanceof 
    var s= new String("hello");
    alert(typeof(s));    object
    alert( s2 instanceof String);   true

---------------------------------------------
创建String对象
    var s="hello";
    var s2= new String("hello2");

对象属性length
alert（s.length）;

for (var i in s){console.log(s[i])}
-----------------String方法-------------------
编排方法：
    document.write(s.italics())
    document.write(s.bold())
    document.write(s.anchor())
大小写转换：
    console.log(s.toUpperCase())
    console.log(s.toLowerCase())
获取指定字符：
    console.log(s.charAt(3));  l
    console.log(s.charCodeAt(3)); 76 ACCISS 的值


查询字符串：
    match(); search(); 
    console.log(s.search("1"))    返回匹配第一个取得索引值
    console.log(s.match("1"))     返回数组，里面是所有匹配结果
    
    console.log(s.indexOf("l"));    2
    console.log(s.lastIndexOf("l"));    4
    
    //replace concat split
    s.replace("E","e");
    s.split("E");
    s.concat(" world")     字符串拼接
    
   截取字符串：
   console.log(s.substr(1,2)); 
   console.log(s.substring(1,3));    从索引1到3-1的位置
   console.log(s.slice(1,-3));    左取又不取



-----------------------------------------------
数组创建方式
   方式一
            var arr=[1,2,3,4,5];
   方式二
        var arr2= new Array(5,4,3,2);
如果采用初始化对象方式创建数组，如果只有一个只切为数字，则表示长度，不是内容

数组是可变长的！！


==================================================
二维数组：数组里面有数组    ****
var arr2=[true,2,"hello",4,[8,9]];


将数数组内的字符串拼接成一个字符串      在Arry
数组对象的方法：
    var ret=["hello","xiaohu"].join("+++");
    hello+++xiaohu

shift  unshift  pop   push  -------栈操作-----
压栈   和    弹栈  
队列:先进先出     栈：先进后出 

var arr5=[1,4,6];
arr5.push(13);   放到最后面
ret= arr5.pop();      删除最后一个   可以取出来

shift  unshift   在顶部操作

------------排序---------------
sort reverse

var arr6=[1,3,6,100];
arr6.reverse();
arr6.sort(mysort);

function mysort(a,b){
    return a-b;
}

按照字符串ASCII 顺序排

arr6.concat(4,5);  添加


======================Date===============
创建方式：
    var date_obj=new Date();
    alert(date_obj.toLocaleString());

    var date_obj2=new Date("2016/3/14 15:30 50");
    alert(date_obj2.toLocaleString());

方法：
    var date_obj=new Date();
    console.log(date_obj.getFullYear());
    console.log(date_obj.getMonth());
    console.log(date_obj.getDate());
    console.log(date_obj.getDay());
    console.log(date_obj.getHours());
    console.log(date_obj.getMinutes());
    console.log(date_obj.getSeconds());
    console.log(date_obj.getHourMinuteSecond);
    console.log(date_obj.getMilliseconds());
    
    function num_week(n){
        week=["星期日","星一","星期二","星期三","星期四","星期五","星期六"]
        return week[n]
    }
    function f(num){
        if (num<10){
            return "0"+num;
        }
        return num;
    }
    
    date_obj.setFullYear();
    date_obj.setMonth();
    
    
-----------------------正则------------------------------
创建方式一：
var re_obj=new RegExp("\d+","g ")
alert(re_obj.test("asd123afaf"))

方式二：
    var re_obj2=/\d+/g;
    alert(re_obj2.test("asd123afaf"))

var s="hello123afaf"


s.match(/\d+/g);    取出所有匹配内容放到数组
s.search(/\d+/g);   取出第一个结果的索引值
s.split(/\d+/g);        

---------------------Math------------------------
直接用
alert(Math.random())   //  (0,1)
laert(Math.round(2.8))  // 四舍五入
alert(Math.pow(2,3))    2的三次方


=======================window  对象=================================

alert confirm  prompt    

    ret=confirm("是否确认")   #有返回值
    prompt("hello")    #输入框
    

-------------------定时器------------------------

var ID=setInterval(begin,1000);  每秒中执行begin

clearInterval(ID);    取消





'''


















