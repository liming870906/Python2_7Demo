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

current_layer = menu
parent_layer = []
is_Over = False
while not is_Over:
    for key in current_layer:
        print(key)
    choice = input(">>>>>>>>>:").strip()
    if len(choice) == 0:
        print('输入内容不合法！！！')
        continue
    if choice in current_layer:
        parent_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layer:
            current_layer = parent_layer.pop()
    elif choice == 'q':
        is_Over = True
    else:
        print('没有相关内容'.center(40,'-'))
