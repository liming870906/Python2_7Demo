# 迭代器与迭代对象

from _collections_abc import Iterator,Iterable

print(isinstance([],Iterable))
print(isinstance([],Iterator))
print(isinstance(iter([]),Iterator))

print(isinstance({},Iterable))
print(isinstance({},Iterator))

print(isinstance((),Iterable))
print(isinstance((),Iterator))

print(isinstance('abc',Iterable))
print(isinstance('abc',Iterator))

print(isinstance((x for x in range(10)),Iterable))
print(isinstance((x for x in range(10)),Iterator))


"""
注意：文件也是一个可迭代对象
"""

def add(s, x):
    print('--------------11111-------------s:%d == x:%d'%(s,x))
    return s + x

def gen():
    print('--------------22222-------------')
    for i in range(4):
        print('--------------33333-------------i:%d'%i)
        yield i  # 0~3
print('--------------44444-------------')
base = gen()
print('--------------55555-------------')
for n in [1,10]:
    print('--------------66666-------------n:%d'%n)
    base = (add(i,n) for i in base)
    print('--------------77777-------------n:%d'%n)
print('--------------88888-------------')
print(list(base))
print('--------------99999-------------')


"""
文件最长的一行
"""

print(
    max(
        len(x.strip()) for x in open('files/Text_Content','r',encoding='utf-8')
    )
)
"""
time模块使用
"""
import time
print(help(time))
print(time.time())#时间戳
print(time.gmtime())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strptime("2018-11-11","%Y-%m-%d"))


mT= time.strptime("2018-11-11","%Y-%m-%d")
print(mT.tm_year)
print(mT.tm_mday)
print(mT.tm_wday)
print(time.ctime())
print(time.ctime(1542357428))
print(time.mktime(mT))

import datetime

print(datetime.datetime.now())
"""
随机数模块
"""
import random

print(random.random())
print(random.randint(1,8))
print(random.randrange(1,10))
print(random.choice('abcdefghijklmnopqrstuvwxyz'))
print(random.choice([123,321,234,354,6777,8,9,911,7,65,5,4444,5667,'asdfsf']))
data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(random.sample(data,len(data)))

def v_code():
    """
    验证码方法
    :return: 返回5位的验证码
    """
    _code = []
    for i in range(10):
        _code.append(str(i))
    for j in range(65,91):
        _code.append(chr(j))
    print("".join(random.sample(_code,5)))
v_code()