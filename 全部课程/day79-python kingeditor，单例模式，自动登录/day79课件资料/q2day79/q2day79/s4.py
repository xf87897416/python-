#__author:  Administrator
#date:  2017/2/9
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests.auth import HTTPProxyAuth

import requests

# ############## 方式一 ##############

i1 = requests.get(url="http://dig.chouti.com/help/service",
                  headers={
                      'Referer': 'http://dig.chouti.com/',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
                  }
                  )
i1_cookies = i1.cookies.get_dict()

# print(i1_cookies)


i2 = requests.post(
    url="http://dig.chouti.com/login",
    headers={
      'Referer': 'http://dig.chouti.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
                  },
    data={
        'phone': "8613100704149",
        'password': "abcd421",
        'oneMonth': "1"
    },
    cookies=i1_cookies
)

print(i2.text)

# ## 3、点赞（只需要携带已经被授权的gpsd即可）
gpsd = i1_cookies['gpsd']
# print(gpsd)

i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=18090231",
    cookies={'gpsd': gpsd},
    headers={
      'Referer': 'http://dig.chouti.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
                  },
)

print(i3.text)

'''
总结   先get登录，获取cookies
        post用户登录带cookies
        gpsd=cookies['gpsd']
        点赞页面使用cookies={'gpsd': gpsd}
'''








