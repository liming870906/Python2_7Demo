
# 0到99的奇数获取方法
# for i in range(0,100):
#     if i % 2 != 0:
#         print(i)
for i in range(1,101,2):
    print(i)
# ----------------------------
for i in range(0,100):
    if 50 < i < 70:
        continue
    else:
        print(i)

# for i in range(0,100):
#     if i < 50 or i > 70:
#         print(i)
#     else:
#         continue