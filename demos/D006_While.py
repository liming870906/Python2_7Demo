isNext = True
while isNext:
    age = int(input("Age:"))
    if age == 87:
        print("you guess success")
        isNext = False
    elif age > 87:
        print("guess lager")
    else :
        print("guess small")
else:
    print("End")

# number = 1
#
# while number <= 10:
#     print("Number:",number)
#     number += 1

# num = 1
#
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1