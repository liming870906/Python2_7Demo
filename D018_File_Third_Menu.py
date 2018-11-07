# liming
is_Over = False
while not is_Over:
    content = ''
    with open('files/CityThirdMenu','r',encoding='utf-8') as file:
        for i in file:
            content = ''.join([i])
    menu = eval(content)
    current_menu = menu
    current_key = ''
    parent_key = []
    is_Controller = True
    while is_Controller:
        for key in current_menu:
            print(key)
        con1 = input('>>>>>>:').strip()
        if len(con1) == 0:
            print('输入不合法'.center(50,'-'))
            continue
        if con1 in current_menu:
            current_key = con1
            parent_key.append(current_menu)
            current_menu = current_menu[current_key]
        elif con1 == 'q':
            is_Controller = False
            is_Over = True
        elif con1 == 'b':
            if parent_key:
                current_menu = parent_key.pop()
        elif con1 == 'i': #添加操作
            input_content = input(">>>>当前%s标签内添加内容>>>>:"%current_key)
            if len(input_content) != 0 and len(current_key) != 0:
                current_menu.update({input_content:{}})
                with open('files/CityThirdMenu','w',encoding='utf-8') as file:
                    file.write(str(menu))
                    file.flush()
                is_Controller = False
            else:
                print('字符串不合法'.center(50,'-'))
        elif con1 == 'd':
            input_content = input(">>>>请输入删除标签>>>>>:")
            if len(input_content) != 0 and input_content in current_menu:
                current_menu.pop(input_content)
                with open('files/CityThirdMenu','w',encoding='utf-8') as file:
                    file.write(str(menu))
                    file.flush()
                is_Controller = False
            else:
                print('无此标签'.center(50,'-'))
        else:
            print('其他操作')
    else:
        if not is_Over:
            print('更新数据'.center(100,'#'))
else:
    print('程序退出'.center(50,'-'))