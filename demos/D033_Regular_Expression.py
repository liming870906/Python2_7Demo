"""

正则表达式
    在Python中使用re模块调用正则表达式
"""

import re

content = re.findall('w\w{2}l', 'hello world')

print(content)
# .点元字符
ret = re.findall('w..l', 'hello world')
print(ret)

ret.clear()
# .点不能匹配\n换行符
ret = re.findall('w.l', 'hello w\nld')

print(ret)
ret.clear()
# ^  匹配输入字行首。如果设置了RegExp对象的Multiline属性，^也匹配“\n”或“\r”之后的位置。
ret = re.findall('^hello', 'hello world')
print(ret)
ret.clear()
ret = re.findall('^hello', 'abcdefghijjjjjj   hello world')
print(ret)
ret.clear()
# $ 匹配输入行尾。如果设置了RegExp对象的Multiline属性，$也匹配“\n”或“\r”之前的位置。
ret = re.findall('hello$', 'hello world')
print(ret)
ret.clear()
ret = re.findall('hello$', 'abcdefghijjjjjj   hello')
print(ret)
ret.clear()
#  * 匹配前面的子表达式任意次。例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。
ret = re.findall('zo*', 'zooooooa')
print(ret)
ret.clear()
ret = re.findall('al{0,}', 'alllllmmml')
print(ret)
ret.clear()
print("分隔符".center(100, '-'))
"""
---------------------------------------------------------
"""
print(re.match(r'l', 'liuyan1').group())
print(re.match(r'y', 'liuyan1'))
print(re.search(r'y', 'liuyan1').group())

print(re.search(r'[a-z]+', 'benbenAAA1989mmm').group())
print(re.search(r'[a-z]+', 'benbenAAA1989mmm', re.I).group())

if re.match(r'[0-9]', 'a'): print('m')

print(re.split(r'\s+', 'a b c   d    ee ff'))
print(re.split(r'[\s\,]+', 'a,b,c,d ,  , ee, ,ff'))

print("分隔符".center(100, '-'))
"""
---------------------------------------------------------
"""
# 寻找最内侧括号
bracket = re.compile(r'\([^()]+\)')
# 寻找乘法运算符
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')
# 寻找除法运算规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')
# 寻找加法运算规则
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')
# 寻找减法运算规则
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')
# 检查括号内是否运算完毕规则
c_f = re.compile(r'\(?\+?-?\d+\)?')
# 脱括号规则
strip = re.compile(r'[^(].*[^)]')


def _mul(s):
    """计算表达式中的乘法运算"""
    exp = re.split(r'\*', mul.search(s).group())
    return s.replace(mul.search(s).group(), str(float(exp[0]) * float(exp[1])))


def _div(s):
    """计算表达式中的除法运算"""
    exp = re.split(r'/', div.search(s).group())
    return s.replace(div.search(s).group(), str(float(exp[0]) / float(exp[1])))


def _add(s):
    """计算表达式中的加法运算"""
    exp = re.split(r'\+', add.search(s).group())
    return s.replace(add.search(s).group(), str(float(exp[0]) + float(exp[1])))


def _sub(s):
    """计算表达式中的减法运算"""
    exp = sub.search(s).group()
    if exp.startswith('-'):
        exp = exp.replace('-', '+')
        res = _add(exp).replace('+', '-')
    else:
        exp = re.split(r'-', exp)
        res = str(float(exp[0]) - float(exp[1]))
    return s.replace(sub.search(s).group(), res)


def calc():
    while True:
        s = input('请输入计算公式：')
        if s == 'q':
            break
        else:
            s = ''.join([x for x in re.split(r'\s+', s)])
            if not s.startswith('('):
                s = str('(%s)' % s)
            while bracket.search(s):
                s = s.replace('--', '+')
                s_search = bracket.search(s).group()
                if div.search(s_search):
                    s = s.replace(s_search, _div(s_search))
                elif mul.search(s_search):
                    s = s.replace(s_search, _mul(s_search))
                elif sub.search(s_search):
                    s = s.replace(s_search, _sub(s_search))
                elif add.search(s_search):
                    s = s.replace(s_search, _add(s_search))
                elif c_f.search(s_search):
                    s = s.replace(s_search, strip.search(s_search).group())
            print('结果为：%.2f' % (float(s)))


if __name__ == '__main__':
    calc()
