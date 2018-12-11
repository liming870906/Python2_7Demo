# 函数递归

mSum = 1
# 创建函数
def recursion_number(number):
    """
    递归实现
    :param number:
    :return:
    """
    global mSum
    if number == 0 : return mSum
    mSum *= number
    recursion_number(number - 1)
recursion_number(10)
print(mSum)



def fact(n) :
    if n == 1 :
        return 1
    return n * fact(n - 1)

print(fact(10))

def fibo(n) :
    if n <= 1:
        return n
    return fibo(n -1) + fibo(n-2)

print(fibo(3))
"""
    关于递归方法：
        方法调用自身函数，并且一定有结束条件。
        注意： 但凡能使用递归可以写的程序循环都可以解决。
              递归效率在一定条件下是很低的不推荐使用。
"""

data = ['a','b','c','d']

def fun1(p):
    if p != 'a':
        return p

print(filter(fun1,data))
print(list(filter(fun1,data)))

def fun2(p):
    return p + '-test'

print(map(fun2,data))
print(list(map(fun2,data)))
print(filter(fun2,data))
print(list(filter(fun2,data)))

def fun3(x, y):
    return x + y

from functools import reduce

print(reduce(fun3,range(1,7),8))