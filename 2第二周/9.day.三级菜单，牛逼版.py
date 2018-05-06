#_author: "Administrator"
#date: 2017/10/23
zone = {
    "湖北省":{
        "武汉市": {"武昌区":{"东湖路":{},
                              "中北路":{},
                              "汉街":{},
                              },
                    "江汉区":{"汉正街":{},
                               "白马商城":{},
                              },
                    '汉阳区':{},
        },
        "黄石市": {"下陆区":{},
                    "铁山区":{},
                    '西塞山区':{},
        },
        "宜昌市": {"西陵区":{},
                    "点军区":{},
                    '夷陵区':{},
        },
    },
    "山西省":{
        "太原市":{"小店区":{},
                   "尖草坪区":{},
                   '晋源区':{},
        },
        "大同市":{"城区":{},
                   "矿区":{},
                   "南郊区":{},
        },
        "长治市":{"城区":{},
                   "郊区":{},
        },
    },
    "辽宁省":{
        "沈阳市":{"和平区":{},
                  "大东区":{},
                  "铁西区":{},
        },
        "大连市":{"中山区":{},
                   "普兰店区":{},
                   "旅顺口区":{},
        },
        "本溪市":{"平山区":{},
                   "明山区":{},
                   "南芬区":{},
        },
    }
}

flg=False
currer=zone
fathers=[]
while not flg:
	for key in currer:
		print(key)
	chose = input("(用法：quit：退出，b:返回上一层，添加： ，删除：)>>>:").strip()
	if len(chose) == 0:continue
	if chose in currer:
		fathers.append(currer)
		currer=currer[chose]
	elif chose =='b':
		if fathers:
			currer =fathers.pop()
	elif chose == "quit":
		flg = True
	elif chose =="添加":
		insert=input("请输入添加项")
		currer[insert]={}
	elif chose == "删除":
		delete = input("请输入删除项")
		del currer[delete]
	else:
         print("无此项，用法：quit：退出，b:返回上一层，添加： ，删除：")

a=str(zone)
f=open('123.py','r+',encoding='utf8')
print(f.readline())
f.write(a)










