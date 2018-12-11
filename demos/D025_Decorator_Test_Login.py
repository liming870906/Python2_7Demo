# 通过装饰器实现应用的登陆操作
"""
# 1.展示模块列表如    首页、金融、生活
# 2.选着模块购物验证是否登陆
# 3.登陆保存用户名、密码及登录状态
# 4.再次选择模块检验是否登陆
# 5.不同模块要求使用不同登陆方式。
"""
def login(function):
    """
    登陆方法
    :return:
    """
    def inner_verify(*args,**kwargs) :
        # 获得用户登陆状态
        _login_statues = getLoginStatues()
        # 获得登陆账户信息列表
        _user_information = getUserInfo()
        # 判断是否登陆
        if _login_statues is False:
            # 输入用户名及密码
            user_name = input("Please input you name:")
            password = input("Please input you password : ")
            # 判断输入用户名、密码是否为None对象
            if user_name is not None and password is not None :
                # 判断存储的用户信息是否为None
                if _user_information and len(_user_information) == 2 :
                    # 判断用户名和密码是否一致
                    if user_name == _user_information[0] and password == _user_information[1]:
                        _login_statues = True
                        saveUserInfo(user_name,password)
                        updateLoginStatues(_login_statues)
                        print("login is success")
                        function(*args,**kwargs)
                else:
                    pass
            else :
                pass
        else :
            function(*args,**kwargs)
    return inner_verify


def getLoginStatues():
    """
    获得登陆状态
    :return:
    """
    _is_statues = False
    with open('files/login_statues', 'r', encoding='utf-8') as file:
        _content = file.readline()
        if _content is not None:
            if _content == 'True':
                _is_statues = True
    return _is_statues

def updateLoginStatues(isStatues):
    """
    更新登陆状态
    :param isStatues:
    :return:
    """
    with open('files/login_statues', 'w', encoding='utf-8') as file:
        file.write(str(isStatues))
        file.flush()

def saveUserInfo(name,passord) :
    """
    保存用户信息
    :param name:
    :param passord:
    :return:
    """
    with open('files/user_info', 'w', encoding='utf-8') as file:
        file.write(name)
        file.write("\n")
        file.write(passord)
        file.flush()

def getUserInfo():
    """
    获取用户信息
    :return:
    """
    _user_information = list()
    with open('files/user_info', 'r', encoding='utf-8') as file:
        for i in file:
            if i is not None:
                _user_information.append(i.strip())
    return _user_information

@login
def home():
    print("you choose home!!!")


@login
def financial():
    print("you choose financial!!!")


@login
def life():
    print("you choose life!!!")

if __name__ == '__main__':
    mData = ('首页',
             '金融',
             '生活')
    is_Quit = False
    while is_Quit is False:
        for i, v in enumerate(mData, 1):
            print(i, v)
        _choose_model = input("please choose model[q is Quit] : ")
        if _choose_model is not None and _choose_model.isdigit():
            _number = int(_choose_model)
            if _number == 1:
                home()
            elif _number == 2:
                financial()
            elif _number == 3:
                life()
            else :
                pass
        elif _choose_model == 'q':
            is_Quit = True
