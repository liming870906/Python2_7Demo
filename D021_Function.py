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
    _date = time.strftime("%Y/%m/%d %H:%M:%S",time.gmtime())
    with open('files/logger.txt','a+',encoding='utf-8') as file:
        file.write("%s is logger -> %s \n"%(_date,content))
        file.flush()

for i in range(10):
    logger("Application is id : %d"%i)
    time.sleep(5)