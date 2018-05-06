#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/30

import time


'''

ECMAscript    DOM   BOM

JS
变量 需要声明  关键字 var

变量民命规范 imyTest 90
            smyTest hi
注释 // 
 /* */

--------------五种基本数据类型---------------------
1  Number 包括整形和浮点型 
2  String   字符串 "" 或 "
3  Boolean  true false 用于调节判断
4  Null   对象 占一个位置
5  Undefined  undefined  未定义

数据类型转换：
    字符串的拼接
parseInt（）  强转整形
        "a3.14"  当转换数百就是NaN 属于Number
            // NaN 数据在表达式中一定结果为false，除了！=
            
typeof ： 测试数据类型            
            
parseFloat()   浮点型

eval()


=================================================
var a=1
var b=a++  先赋值 后加减

var b= ++a 先加减后赋值
###################################
##python三元运算符1 if 5>3 else 0###
###################################

一元加减法：
var a="3"
    b=+a     处理必须是数字

逻辑与 &&    1 && 0 ----》0
            0 && 0 -----》0
            1 && 1 -----》1  
              
逻辑或       1 || 0 ---->1
            0 || 0 ----->0
            1 || 1 ------1
逻辑非 ！            
   var a =1;         
  if (a<10 && a>0){
    ++a
  }          
            
     
     2=="2"  true
     2==="2"  false 
     
     全等号不进行数据转换
     
     
等性运算符
null==undefined   true
"NaN"==NaN   flase
false==0    true
true==1     true    
true==2    false
5=="5"   true
     
    
    
    
控制语句

        if(){
        
        
        }else{
        
        
        }else if(){
        
        
        }
----------------------------------  
    switch(x){
    case 1:y="星期一"; break
    case 2:y="星期二"; break
    case 3:y="星期三"; break
    case 4:y="星期四"; break
    case 5:y="星期五"; break
    default y="未定义"
    }


var a =[1,'hello',true]    
for  (var i in a){
    console.log(i)    #s索引
    console.log(a[i])
}    



for (var i=1;i<10;++i){
    console.log(i)
}

obj={"1":"111","2":[1,2]}

alert(typeof(obj))    object
alert(obj)     [object Object]
    for (var i in obj){
            console.log(i);
            console.log(obj[i]);
    }
    
try{
}
catch(e){

}
finally{
}

throw Error("xxx")  #主动抛出异常 raise


---------------函数-----------------
创建方式一
function func1(){

    }
创建方式二：
    var func2= new Function("参数一"，"参数二"，"函数体");
    
    var add=new Function("a","b","alert(a+b)");
    add(1,2)
    
    alert(add.length)   #参数的个数
    
第三种方式：
    var func3=function(){
        alert(123);
    }
    func3()     #匿名函数
    
    
----------函数属性和方法-----------------

void  阻止返回值



function a(a,b){
    alert(a+b)
}
var a=1
var b=2
a(a,b)

------------------------arguments对象----------------------------

var ret=0
function add(){
   alert(arguments.length)
   
   for (var i in argments){
           ret+=arguments[i] 
   }
   :return ret;
}
--------------自执行函数----------------------

（function(arg)）{
    console.log(arg);
}("123")

开销小，一次性



         
'''




































































