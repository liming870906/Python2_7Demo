"""
配置信息
"""

import logging,os


# 日志级别
LOG_LEVEL = logging.INFO

# 根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

# 设置文本日志文件名称
LOG_TYPES={
    'transaction':'transaction.log',
    'access':'access.log'
}

# 数据库信息
DATABASE = {
    'engine':'file_storage',
    'name':'accounts',
    'path':'%s/db' % BASE_DIR
}