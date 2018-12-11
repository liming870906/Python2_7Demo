"""
主逻辑入口
"""
from core import logger_me
from core import auth

# 认证初始化信息
user_data = {
    'account_id' : None,
    'is_authenticated':False,
    'account_data':None
}
# 获得日志对象
trans_logger = logger_me.logger('transaction')
access_logger = logger_me.logger('access')


def start_main():
    access_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = access_data
    print(access_data)