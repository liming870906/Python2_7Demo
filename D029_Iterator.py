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