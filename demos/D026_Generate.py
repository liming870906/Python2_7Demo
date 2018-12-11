# 列表生成器

# 列表生成式
a = [x ** 2 for x in range(10)]

print(a)

# 放入函数的列表生成式

def funcation_01(n) :
    return n ** 3

b = [funcation_01(x) for x in range(10)]

print(b)

# 扩展内容-->赋值方式

t = ('123',10)

c,d = t  #相当于 c = t[0] ; d = t[1]

print(c, d)

# 生成器
data = [0,1,30,4,5,6,4,10]
f = (x * 2 for x in data)

print(f) #<generator object <genexpr> at 0x10615db88>
print(f.__next__())  #  Python2 直接调用next方法调用
print(f.__next__())  #  Python3 可以使用__next__方法，该方法为内置方法不建议调用
print(f.__next__())
print(next(f))  #内置next等价于调用内置__next__方法
"""
上述为生成器对象，但内部并没有数据，如果需要数据去生成器中取一个就会生成一个。
"""
print("分隔符".center(100,"-"))
# 通过循环方式获取生成器数据
data1 = [0,1,30,4,5,6,4,10]
g = (x * 2 for x in data)

for i in g:
    print(i)

"""
生成器创建方式：1.（x for x in rang(10)）    
              2. yield创建
"""
print("分隔符".center(100,"-"))
def fib(max) :
    n, a, b = 0,0,1
    while n < max:
        yield b
        a, b = b , a+b
        n += 1
    return 'done'
for i in fib(5):
    print(i)
"""
未获取到函数的返回值
"""
h = fib(10)
while True:
    try:
        _x = next(h)
        print("生成器生成对象：%d"%_x)
    except StopIteration as e:
        print("异常处理："+e.value)
        break
