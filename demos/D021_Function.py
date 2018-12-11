# 函数
"""
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

    格式：
        def 函数名（参数列表）:
            函数体


    define译为：定义
"""


def sun(number1, number2):
    """
    注释地方
    :param number1:
    :param number2:
    :return:
    """
    # print("number1 + number2 = %d"%(number1 + number2))
    return number1 + number2


import time


# print(time.strftime("%Y/%m/%d %H:%M:%S",time.gmtime()))
# print(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()))
# print(time.strftime("%Y/%m/%d %H:%M:%S"))
def logger(content):
    """
    记录日志
    :param content:
    :return:
    """
    _date = time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime())
    with open('files/logger.txt', 'a+', encoding='utf-8') as file:
        file.write("%s is logger -> %s \n" % (_date, content))
        file.flush()


# for i in range(10):
#     logger("Application is id : %d"%i)
#     time.sleep(5)
"""
    参数包含：
        必须参数：   
        关键字参数：  通过关键字设置参数数据，可以不考虑顺序。
        默认参数：   为参数直接赋值。默认参数一定要跟在其他参数的后面。不然无法编译通过。
        不定长参数：  使用一个*放在参数名称前，需要传递一个元组数据
                （注意*使用的是无命名参数）
                    **双星号参数将参数存为了字典，实际传入使用键值对的方式。
    参数的位置关系，不能错乱。
"""


def sum(*ages):
    """
    加法器
    :param ages:
    :return:
    """
    _sum = 0
    for i in ages:
        _sum += i
    else:
        print("Sum=%d" % _sum)


sum(1, 2, 3, 4, 5, 6, 7, 8, 9)


def print_info(*args, **kvargs):
    """

    :param args: 无名称参数（元组）
    :param kvages: 键值对参数（字典）
    :return:
    """
    print(args)
    print(kvargs)


print_info('aaa', 12, 'bbbb', NickName='benben', Age=18)


def abc(nick='smile', *ages, sex='w', **kvargs):
    """
    默认参数的形参默认获取实参数据。
    :param nick:
    :param ages:
    :param sex:
    :param kvargs:
    :return:
    """
    print('nick:%s' % nick)
    print('sex:%s' % sex)
    for i in ages:
        print(i)
    for j in kvargs:
        print(j)


abc('hello', 10, "World", Age=10, Name='benben')

def bcd(): return 'abc',11,22,[1,2,3,4]

print(bcd())

out_p = 20

def changeIn():
    global out_p
    print(out_p)
    out_p = 30
    in_p = 50
    def inner():
        nonlocal in_p
        print(in_p)
        in_p = 40
        print(in_p)
    inner()

changeIn()
print(out_p)

def insertList(*args):
    print(args)

insertList(*[1,2,3,4],*[33,44,55])

def insertDist(**kwargs):
    print(kwargs)


insertDist(**{'name':'libenben','age':18,'set':'woman'})


# 高级函数

def square(number):
    return number * number

def foo(number1, number2, square_function):
    return square_function(number1) + square_function(number2)

print(foo(5,2,square))