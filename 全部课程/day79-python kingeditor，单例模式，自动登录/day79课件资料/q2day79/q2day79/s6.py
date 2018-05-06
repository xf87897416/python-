#__author:  Administrator
#date:  2017/2/9


# session = requests.session()
# session.get()
# session.post()
# session.post()
# requests.get()

# from bs4.element import Tag

import json
import requests
from bs4 import BeautifulSoup
import urllib3

boundary='------WebKitFormBoundaryKkYNe1O04TluKApx'
data=[]
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="app_id"\r\n')
data.append('xxxxxx')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="version"\r\n')
data.append('xxxxx')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="platform"\r\n')
data.append('xxxxx')





r1=requests.get(url='https://leetcode.com/accounts/login/',
                headers={
                    'content-type': 'multipart/form-data ',
                    'Referer': 'https://leetcode.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
                },
                )

soup1 = BeautifulSoup(r1.text, features='html.parser')
tag = soup1.find(name='input', attrs={'name': 'csrfmiddlewaretoken'})
csrfmiddlewaretoken = tag.get('value')

cookey1=r1.cookies.get_dict()
r1.close()


files={'login':(None,'xf87897416'),
    'password':(None,'abcd421'),
    'csrfmiddlewaretoken':(None,csrfmiddlewaretoken),
 }



r2=requests.post(url='https://leetcode.com/accounts/login/',
                 headers={
                    'content-type': 'multipart/form-data ',
                     'Referer': 'https://leetcode.com/',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
                 },
                 # data={'login':'xf87897416',
                 #          'password':'abcd421',
                 #          'csrfmiddlewaretoken':'q7EPLeAaZTTU1TkDHsQOKgXau8C6RiaCSpo2hX6LdcyJSZ0pAyuMog7LstZcgOzw'},
                 files=files,
                 cookies=cookey1,
                 )
print(r2)











