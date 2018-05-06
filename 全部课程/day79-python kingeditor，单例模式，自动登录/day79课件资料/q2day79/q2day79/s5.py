#__author:  Administrator
#date:  2017/2/9
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


# ############## 方式二2222 ##############

import requests

session = requests.Session()
i1 = session.get(url="http://dig.chouti.com/help/service",
                 headers={
                     'Referer': 'http://dig.chouti.com/',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
                 }
                 )


i2 = session.post(
    url="http://dig.chouti.com/login",
    headers={
                     'Referer': 'http://dig.chouti.com/',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
    },
    data={
        'phone': "8613100704149",
        'password': "abcd421",
        'oneMonth': ""
    }
)
# print(i2.text)

i3 = session.post(
    url="http://dig.chouti.com/link/vote?linksId=8589524",
    headers={
             'Referer': 'http://dig.chouti.com/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
    },
)
print(i3.text)



'''
总结   先get登录，获取session
        利用session post登录
        利用session post点赞
'''


