#_author: "Administrator"
#date: 2017/10/22



sheng = {
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



# for i in sheng:
#     print(i)
#     for j in sheng[i]:
#         print(j)
#         for k in sheng[i][j]:
#             print(k)


# flg1=1
# flg2=2
# flg3=3
g_break= False
while not g_break:
    for key in sheng:
        print(key)
    chose=input("1>>:").strip()
    if chose in sheng:           #湖北省
        while not g_break:
            for key2 in sheng[chose]:
                print(key2)             #打印武汉市，宜昌市
            chose2=input("2>>:").strip()
            if chose2 in sheng[chose]:
                while not g_break:
                    for key3 in sheng[chose][chose2]:
                        print(key3)
                    chose3 = input("3>>:").strip()
                    if chose3 in sheng[chose][chose2]:
                        while not g_break:
                            for key4 in sheng[chose][chose2][chose3]:
                                print(key4)
                            print('last page!')
                            chose4 = input("请输入选择：cd,or quit:")
                            if chose4 == 'cd':
                                print("返回上层")
                                break
                            elif chose4 == 'quit':
                                g_break = True
                    elif chose3 == 'cd':
                        break
                    else:
                        print("输入错误")
                    if chose3=='quit':
                        g_break = True
            elif chose2 =='quit':
                break
            else:
                print("输入错误")
    else:
        print("输入错误")












