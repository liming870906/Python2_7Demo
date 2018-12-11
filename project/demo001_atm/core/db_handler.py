


def db_hander(conn_parms):
    """
    连接数据库
    :param conn_parms:
    :return:
    """
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)


def file_db_handle(conn_parms):
    """
    获取文本信息
    :param conn_parms:
    :return:
    """

    db_path = '%s/%s' %(conn_parms['path'],conn_parms['name'])
    return db_path