"""
记录日志信息
"""

import logging
from conf import settings

def logger(log_type) :
    """
    初始化创建日志对象
    :param log_type: 日志文件名称
    :return:
    """
    # 创建日志对象logger
    logger = logging.getLogger(log_type)
    # 设置日志等级
    logger.setLevel(settings.LOG_LEVEL)
    # 创建控制台流
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)
    # 创建文件流
    # 获取文件存储路径
    log_file = "%s/log/%s" %(settings.BASE_DIR,settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # 创建日志显示格式
    formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
    # 设置格式到流中
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 添加Handler
    logger.addHandler(ch)
    logger.addHandler(fh)
    # 返回logger对象
    return logger