
#__author__ = "liming"
# date = 2018/10/29
msg1 = """
    这里看见我们！！！！！
"""

msg2 = '''
    这里使用的是单引号！！！！
'''


print(msg1,msg2)

msg3='''
    name = %s
    age = %d
    job = %s
'''%("liming",32,"IT")

print(msg3)

salary = input("Salary:")

if salary.isdigit():
    salary = int(salary)
else:
    exit("Salary is not number")