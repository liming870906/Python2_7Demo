age_of_princal = 56

guess_age = int(input(">>:"))
"""
    if guess_age == age_of_princal then 
        print("yes")
    else
        print("not")
"""

if guess_age == age_of_princal:
    print("Yes ,you got it...")
elif guess_age > age_of_princal:
    print("try small")
else:
    print("try bigger")

# 字符串拼接
content = "abc" + "qwe"
print(content)

p1 = input("Enter:")
print(int(p1))
print(str(p1))
