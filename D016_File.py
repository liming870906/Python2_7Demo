




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

str = file.read()
print ("读取数据: %s" % (str))
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