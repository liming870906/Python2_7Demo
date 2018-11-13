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
    print("mSum%d"%mSum)
    if number == 0 : return mSum
    mSum *= number
    recursion_number(number - 1)
recursion_number(10)
print(mSum)



def fact(n) :
    if n == 1 :
        return 1
    return n * fact(n - 1)

print(fact(120))

"""
    关于递归方法：
        方法调用自身函数，并且一定有结束条件。
        注意： 但凡能使用递归可以写的程序循环都可以解决。
              递归效率在一定条件下是很低的不推荐使用。
"""