name = input("your name:")
age = input("your age:")
death_age  = 80

print("your name:", name)
# 该输出不是拼接
print("you can still live for",death_age-int(age),"years...")


# 字符串拼接
print("you can still live for "+str(death_age-int(age))+" years...")