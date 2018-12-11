
number1 = int(input("number1:"))
number2 = int(input("number2:"))
number3 = int(input("number3:"))

if number1 >= number2:
    if number1 >= number3:
        print("Max:",number1)
    else:
        print("Max:",number3)
else:
    if number2 >= number3:
        print("Max:",number2)
    else:
        print("Max:",number3)