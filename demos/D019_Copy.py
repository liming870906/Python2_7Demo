# 数据拷贝之深浅拷贝(列表的拷贝copy()方法）

s = [1,'benben','Java']

s1 = s.copy()#浅拷贝

print(s)
print(s1)

s1[0] = 2
print(s1)

other = [[1,2],'mama','Android']
other1 = other[:]#浅拷贝 等同于copy方法

print(other)
print(other1)

other1[1] = 'xiongmao'
print(other)
print(other1)

other1[0][1] = 3

print(other)
print(other1)

a = [[9,8],7,6]
b = a #浅拷贝

b[1] = 123
b[0][1] = 999

print(a)
print(b)

c = a.copy()
c[1] = 321
c[0][1] = 888

print(a,b,c)

# 深拷贝需要模块引用方可实现
import copy
# copy.copy()  与上面的拷贝一样代表浅拷贝
# copy.deepcopy() 代表深拷贝内用完全一致

d = copy.deepcopy(a) #深拷贝
d[1] = 777
d[0][0] = 444

print(a,b,c,d)