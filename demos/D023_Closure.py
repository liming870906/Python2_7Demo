# 闭包
# 对函数扩展开放，对函数修改封闭

# outer是外部函数   a和b都是外部函数的临时变量
def outer( a ) :
    b = 10
    # inner 是内部函数
    def inner():
        # 在内部函数中 用到外部函数的临时变量
        print(a + b)
    # 外部函数返回值为内部函数的引用
    return inner
"""
#   在这里我们调用外部函数传入参数5
#   此时外部函数的两个临时变量 a = 5 b = 10
#   并且创建了内部函数，然后将内部函数的引用返回给了demo
#   外部函数结束的时候，会返现内部函数将会用到外部函数的临时变量，
#   这时这两个临时变量就不会被释放，会绑定给这个内部函数
"""
demo = outer(5)
#   我们可以调用内部函数看一下是不是能能够使用外部函数的临时变量
#   demo存储了外部函数的返回值，也就是内部函数的引用地址，
#   就相当于是inner函数
demo()

demo2 = outer(7)

demo2()

"""
    内部函数修改外部函数的临时变量
    两种方式  1.  Python3使用nonlocal关键字
             2.  Python2中没有nonlocal关键字，只能使用可变类型数据进行修改
"""

def outer_B( a ):
    b = 10
    c = [a]

    def inner_B():
        nonlocal b
        b += 1
        c[0] += 1

        print(c[0])
        print(b)
    return inner_B

demo3 = outer_B(5)

demo3() # 6 11
demo3() # 7 12
"""
    注意： 外部函数的临时变量只会创建一个。也就是上面方法中的outer_B中的a和b
"""


