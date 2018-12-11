

# 列表感觉相当于Java中的数组或者List集合
names = ["zhaoqian",'sunli',"zhouwu","zengwang","taiyang","yuan"]

print(names[2])
# 取多这个    这种方式叫做切片
print(names[1:3])
# 切片获得动小标开始到结尾的数据

print(names[2:])
# 去掉最后一个元素可以使用负数代表从右向左的元素
print(names[2:-1])

print(names[1::2])

print(names[-1::-2])

# b = names[-1::-1]
#
# print(b)

names.append("liming")
names.insert(names.index("sunli"),"lidaming")

print(names)

names.pop(names.index("sunli"))

print(names)
names.reverse()
names.sort(reverse=False)
print(names)
names[0:2] = ["a","b"]
print(names)

del names[0]

print(names)

print(names.count("yuan"))

print(type(len(names)))

names[names.index("b")] = "feel"


print(names)
# # 删除对象
# del names
# # 回报异常，因为对象被删除了。
# print(names)
