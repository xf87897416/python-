#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2018/5/10
import urllib.request
#
# def use_proxy(url,addr):
#     proxy=urllib.request.ProxyHandler({'http':addr})
#     opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
#     return data
#
#
# url='http://www.baidu.com'
# addr='222.93.69.229:8118'
# data =use_proxy(url,addr)
# print(data)
url='http://www.baidu.com'
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)

print(response.info())















