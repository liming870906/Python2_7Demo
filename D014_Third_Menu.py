"""
   1.可以一层一层的进入所有层
   2.可以在每一层返回上一层
   3.可以在任意层退出
"""
menu={
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                'XX银行':{},
                'CCTV':{}
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '美团':{}
            },
            '三里屯':{
                '优衣库':{},
                '使馆区':{},
                '酒吧':{}
            }
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{}
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{}
            },
            '回龙观':{}
        },
        '海淀':{
            '中关村':{
                '优酷':{},
                '爱奇艺':{},
                '汽车之家':{},
                '新东方':{},
                'QQ':{}
            },
            '五道口':{
                'Google':{},
                '网易':{},
                '腾讯':{},
                '搜狐':{},
                '快手':{}
            }
        }
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                '高盛':{},
                '摩根':{}
            },
            '外滩':{}
        },
        '闵行':{
            '人民广场':{}
        },
        '静安':{}
    },
    '山东':{
        '济南':{},
        '德州':{
            '乐陵':{
                '丁务镇':{}
            },
            '禹城':{},
            '平原县':{}
        },
        '青岛':{}
    }
}

is_back = False
is_quit = False
# 设置循环
while not is_back and not is_quit:
    # 获取到第一层的Key列表
    for key1 in menu:
        print(key1)
    # 获得输入内容，并去掉两端空格
    choice1 = input("1>>>>:").strip()
    if choice1 == 'q':
        is_quit = True
    # 判断是否在是否在第一层 Key
    if choice1 in menu:
        while not is_back and not is_quit:
            for key2 in menu[choice1]:
                print(key2)
            choice2 = input("2>>>>:").strip()
            if choice2 == 'b':
                is_back = True
            if choice2 == 'q':
                is_quit = True
            if choice2 in menu[choice1]:
                while not is_back and not is_quit:
                    for key3 in menu[choice1][choice2]:
                        print(key3)
                    choice3 = input("3>>>>:").strip()
                    if choice3 == 'b':
                        is_back = True
                    if choice3 == 'q':
                        is_quit = True
                    if choice3 in menu[choice1][choice2]:
                        while not is_back and not is_quit:
                            for key4 in menu[choice1][choice2][choice3]:
                                print(key4)
                            choice4 = input("4>>>>:").strip()
                            print(choice4.center(50,"-"))
                            if choice4 == 'b':
                                is_back = True
                            if choice4 == 'q':
                                is_quit = True
                        else:
                            is_back = False
                else:
                    is_back = False
        else:
            is_back = False