# 装饰器函数
"""
#   简言之，python装饰器就是用于拓展原来函数功能的一种函数，
#   这个函数的特殊之处在于它的返回值也是一个函数，
#   使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。
"""
# 一般而言，我们要想拓展原来函数代码，最直接的办法就是侵入代码里面修改，例如：

import time


def func():
    print("func----Hello_World")
    time.sleep(2)
    print("func------Python")


# 这是我们最原始的的一个函数，然后我们试图记录下这个函数执行的总时间，那最简单的做法就是：

def func_1():
    startTime = time.time()
    print("func1----Hello_World")
    time.sleep(2)
    print("func1------Python")
    endTime = time.time()

    msecs = (endTime - startTime) * 1000

    print("time is %d ms" % msecs)


"""
# 但是如果你的Boss在公司里面和你说：“小祁，这段代码是我们公司的核心代码，你不能直接去改我们的核心代码。
# ”那该怎么办呢，我们仿照装饰器先自己试着写一下：
"""


def deco(func):
    startTime = time.time()
    func()
    endTime = time.time()

    msecs = (endTime - startTime) * 1000

    print("time is %d ms" % msecs)


if __name__ == '__main__':
    deco(func)
"""
# 这里我们定义了一个函数deco，它的参数是一个函数，然后给这个函数嵌入了计时功能。然后你可以拍着胸脯对老板说，看吧，不用动你原来的代码，我照样拓展了它的函数功能。 
# 然后你的老板有对你说：“小祁，我们公司核心代码区域有一千万个func()函数，从func01()到func1kw(),按你的方案，想要拓展这一千万个函数功能，就是要执行一千万次deco()函数，这可不行呀，我心疼我的机器。” 
# 好了，你终于受够你老板了，准备辞职了，然后你无意间听到了装饰器这个神器，突然发现能满足你闫博士的要求了。 
# 我们先实现一个最简陋的装饰器，不使用任何语法糖和高级语法，看看装饰器最原始的面貌：
"""


# 既不需要侵入，也不需要函数重复执行
def deco_1(func2):
    def wrapper():
        startTime = time.time()
        func2()
        endTime = time.time()

        msecs = (endTime - startTime) * 1000

        print("time is %d ms" % msecs)

    return wrapper


@deco_1
def func2():
    print("func2----Hello_World")
    time.sleep(2)
    print("func2------Python")


if __name__ == '__main__':
    f = func2  # 这里f被赋值为func2，执行f()就是执行func2()
    f()
"""
# 这里的deco_1函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。
# 其中作为参数的这个函数func2()就在返回函数wrapper()的内部执行。然后在函数func2()前面加上@deco_1，func()函数就相当于被注入了计时功能，
# 现在只要调用func2()，它就已经变身为“新的功能更多”的函数了。 
# 所以这里装饰器就像一个注入符号：有了它，拓展了原来函数的功能既不需要侵入函数内更改代码，也不需要重复执行原函数。
"""


# 带有参数的装饰器
def deco_2(func3):
    def wrapper(a, b):
        startTime = time.time()
        func3(a, b)
        endTime = time.time()

        msecs = (endTime - startTime) * 1000

        print("time is %d ms" % msecs)

    return wrapper


@deco_2
def func3(a, b):
    print("func3----Hello_World")
    time.sleep(2)
    print("func3------Python")
    print("A+B = %d" % (a + b))


if __name__ == '__main__':
    f = func3  # 这里f被赋值为func3，执行f()就是执行func3()
    f(10, 20)
"""
# 然后你满足了Boss的要求后，Boss又说：“小祁，我让你拓展的函数好多可是有参数的呀，
# 有的参数还是个数不定的那种，你的装饰器搞的定不？”然后你嘿嘿一笑，深藏功与名！
"""


# 带有不定参数的装饰器

def decorator_function(function):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        _ms = (end_time - start_time) * 1000
        print("long time --> %d ms" %_ms)

    return inner_function

@decorator_function
def function_1(a,b):
    print("function 1 params a and b")
    time.sleep(1)
    print('A * B = %d' %(a * b))

@decorator_function
def function_2(a,b,c):
    print("function 1 params a 、b and c")
    time.sleep(1)
    print('A * B + C = %d' %(a * b + c))

if __name__ == '__main__':
    function_1(10,20)
    function_2(5,6,9)
"""
# 最后，你的老板说：“可以的，小祁，我这里一个函数需要加入很多功能，一个装饰器怕是搞不定，装饰器能支持多个嘛” 
# 最后你就把这段代码丢给了他：
"""
# 多装饰器
def decorator_func_01(func):
    print("decorator_func_01-----A")
    def inner_func_01(*args, **kwargs):
        print("inner_func_01-----A")
        func(*args, **kwargs)
        print("inner_func_01-----B")

    print("decorator_func_01-----B")
    return inner_func_01

def decorator_func_02(func):
    print("decorator_func_02-----A")
    def inner_func_02(*args, **kwargs):
        print("inner_func_02-----A")
        func(*args, **kwargs)
        print("inner_func_02-----B")

    print("decorator_func_02-----B")
    return inner_func_02

@decorator_func_02
@decorator_func_01
def test(a,b):
    print("test--start--> a and b")
    time.sleep(1)
    print("a - b = %d" %(a - b))
    print("test--end--> progress is over")

if __name__ == "__main__":
    print("Next".center(50,"#"))
    test(20,5)
"""
#   注意：  多个装饰器是有执行顺序
#   上述结果：decorator_func_01-----A
#           decorator_func_01-----B
#           decorator_func_02-----A
#           decorator_func_02-----B
#           #######################Next#######################
#           inner_func_02-----A
#           inner_func_01-----A
#           test--start--> a and b
#           a - b = 15
#           test--end--> progress is over
#           inner_func_01-----B
#           inner_func_02-----B
"""