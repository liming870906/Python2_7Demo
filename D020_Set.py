"""
集合Set
    特点：1.去重，把一组列表自动去掉重复数据
         2.测试关系， 测试两组数据交集、并集、差集、对称差集等关系
"""
# 创建集合
# 字符串
data_set_01 = set('abcdefghijklmnopqrstuvwxyz')
# 每次打印顺序不定
print(data_set_01)
# 列表
data_set_02 = set([1,2,3,4,5,'a',6,7,8])
# 打印列表
print(data_set_02)
# 创建列表
# li1 = [[1,2],3,4,5]     集合成员为可哈希值的数据也就是不能是列表和字典
# data_set_03 = set(li1)
# print(data_set_03)

# 创建集合
# 可变集合 set  不可变及和frozenset
data_set_04 = frozenset('hello,world')
print(data_set_04,type(data_set_04))

# 访问集合  in  /  not in

print('h' in data_set_04)
print('x' not in data_set_04)

data_set_05 = set()
# 向set中添加数据
# data_set_05.add('abc')
data_set_05.add(('123','234',))
print(data_set_05)
# 更新数据和添加基本一样
data_set_05.update('abc123')
data_set_05.update('123456')
data_set_05.update(('123','555',))
data_set_05.update(('666','555',))
print(data_set_05)
# 移除数据
print(data_set_05.remove('123'))
print(data_set_05.pop())
print(data_set_05)
print(data_set_05.clear())
print(data_set_05)
# 子集 超级
data_set_06 = set('123456')
data_set_07 = set('123456789')
print(data_set_06.issuperset(data_set_07))
print(data_set_07.issuperset(data_set_06))
print(data_set_06 < data_set_07 )
print(data_set_06.issubset(data_set_07))
print(data_set_07.issubset(data_set_06))
print(data_set_06 > data_set_07 )
# 联合  '|'/union方法
data_set_08 = set('123456')
data_set_09 = set('456789')

print(data_set_08 | data_set_09)
print(data_set_08.union(data_set_09))
# 交集 '&'/ intersection方法
print(data_set_08 & data_set_09)
print(data_set_08.intersection(data_set_09))
# 差集  '-'/difference方法
print(data_set_08 - data_set_09)
print(data_set_08.difference(data_set_09))
print(data_set_09 - data_set_08)
print(data_set_09.difference(data_set_08))
# 对称差集 '^' / symmetric_difference方法
print(data_set_08 ^ data_set_09)
print(data_set_08.symmetric_difference(data_set_09))
print(data_set_09 ^ data_set_08)
print(data_set_09.symmetric_difference(data_set_08))













