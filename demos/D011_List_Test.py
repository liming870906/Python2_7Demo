#
# 购物车练习
#


# 定义产品列表

products = [
    ("Java",1000),
    ("Android",2000),
    ("ios",400),
    ("python",100),
    ("C#",500),
]
# 购物车存储类
shopping_car=[]

while True:
    # 输入存储金额
    save_money = input("please save your money:")
    # 判断保存金额是否合法
    if save_money.isdigit():
        save_money = int(save_money)
        break
    else:
        print("invalid error. pleas again print money")
# 展示商品
for i,v in enumerate(products, 1):
    print(i,v)
while True:
    product_number = input("please print product number(exit[q]):")
    if product_number.isdigit():
        product_number = int(product_number)
    if product_number == 'q':
        break
    elif 0 < product_number <= len(products):
    #     获得商品信息
        product = products[product_number -1]
        if save_money > product[1] :
            save_money -= product[1]
            shopping_car.append(product)
            print("you choice product input you shopping car.")
        else:
            print("not more money.")
    else:
        print("you print number is error,please print again.")
print("--------------product menu ------------")
for i in shopping_car:
    print(i)