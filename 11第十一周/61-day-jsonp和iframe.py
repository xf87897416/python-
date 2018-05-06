#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/12/22

import time
'''

用户管理多对多操作
    

文件上传
    - Form表单上传文件
    - Ajax上传文件
    - 基于form表单和iframe自己实现ajax请求
    
    a. 悄悄的上传
        xmlHttpRequest
            xml = new XMLHttpRequest();
            xml.open('post', '/upload.html', true)
            xml.send("k1=v1; k2=v2;")
        jQuery 
            $.ajax({
                url:
                data: {'k1': 'v1', 'k2': 'v2'}
            })
            
        FormData对象
            dict = new FormData()
            dict.append('k1','v1');
            dict.append('k2','v2');
            dict.append('fafafa', 文件对象);
            
            xml.send(dict)
            
            $.ajax({
                url:
                data: dict,
            })
        
        
            
    b. 让用户看到当前上传的图片



id_list = list(zip(*obj_cls_list))[0] if obj_cls_list else [] 
三元运算
a=b if c>0 else c 




<h1>基于iframe实现form提交</h1>
    <form action="/upload.html" method="post" target="iframe_1" enctype="multipart/form-data">
        <iframe style="display: none"  id="iframe_1" name="iframe_1" src="" onload="loadIframe();"></iframe>
        <input type="text" name="user" />
        <input type="file" name="fafafa" />
        <input type="submit" />
    </form>
    <h1>图片列表</h1>

 

function loadIframe() {
            console.log(1);
            // 获取iframe内部的内容
            var str_json = $('#iframe_1').contents().find('body').text();
            var obj = JSON.parse(str_json);
            if (obj.status){
                var img = document.createElement('img');
                img.src = "/" + obj.path;
                $('#imgs').append(img);
            }
        }



















'''