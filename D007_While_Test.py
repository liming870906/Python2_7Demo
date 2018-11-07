num1 = 1

while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print(str(num1)+"*"+str(num2)+"=",num1 * num2,end=" ")
        num2 +=1
    num1 += 1
    print()
