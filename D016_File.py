




file = open('files/文件联系目标1','r+',encoding='utf-8')
# file.write('白日依山尽，黄河入海流。\n欲穷千里目，更上一层楼。\n')
# file.write('Hello world.\n')
# print(file.readlines())


# -------------------
# number = 0
# for i in file.readlines():
#     number += 1
#     if number == 6:
#         i = ''.join([i.strip(),'00000000'])
#     print(i.strip())
# ----------------------
# data = file.readlines()
# data[5] = ''.join([data[5].strip(),'888888888'])
# for i in data :
#     print(i.strip())
# ---------------------
# for i in file:
#     print(i.strip())
# --------------------
# print(file.tell())
# print(file.read(5))
# print(file.tell())
# file.seek(0)
# print(file.read(4))
# --------------------
# print ("文件名: ", file.name)
#
# line = file.readline()
# print ("读取行: %s" % (line))
#
# file.truncate()
# line = file.readlines()
# print ("读取行: %s" % (line))
# ----------------------
print ("文件名为: ", file.name)

# 截取10个字节
file.truncate(10)

strn = file.read()
print ("读取数据: %s" % (strn))
file.close()
# data = file.read(5)
# print(data)
# ----------------------
# 进度条
# import sys, time
# for i in range(50):
#     # sys.stdout.write('#')
#     # sys.stdout.flush()
#     print('*',end='%',flush=True)
#     time.sleep(0.1)

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

with open('files/CityThirdMenu','a+',encoding='utf-8') as f:
    f.write(str(menu))
    f.flush()