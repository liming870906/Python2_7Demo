
from core import db_handler
from conf import settings

import os,json,time

def auth_acc(account, password) :
    """
    用户验证
    :param account:
    :param password:
    :return:
    """
    # 获取数据库文件夹路径
    db_path = db_handler.db_hander(settings.DATABASE)
    # 获取数据库文件路径
    account_file = '%s/user_info_%s.json' %(db_path,account)
    # 打印输出
    print(account_file)
    #判断文件是否存在
    if os.path.isfile(account_file):
        #如果文件存在
        with open(account_file,'r') as f :
            #获取数据
            account_data = json.load(f)
            #判断密码是否正确
            if account_data['password'] == password :
                #判断时效是否过期
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'],'%Y-%m-%d'))
                if time.time() > exp_time_stamp:
                    print("已经过期")
                else:
                    return account_data
            else:
                print("密码错误")
    else:
        print('无数据库信息')



def acc_login(user_data, log_obj):
    """
    account login func
    :param user_data:
    :param log_obj:
    :return:
    """
    # 初始化认证次数
    retry_count = 0
    # 循环验证，最多三次
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = auth_acc(account,password)
        if auth:
            user_data['is_authenticated'] =  True
            user_data['account_id'] = account
            return user_data
        retry_count += 1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()