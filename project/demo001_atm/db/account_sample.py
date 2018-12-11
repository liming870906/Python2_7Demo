"""
生成Json数据
"""
import json
acc_dic = {
    'id':1234,
    'password':'123456LM',
    'credit': 15000,
    'balance': 15000,
    'enroll_date':'2018-12-06',
    'expire_date':'2022-01-01',
    'pay_day':22,
    'status':0   # 0 = normal, 1 = locked, 2 = disabled
}


json.dump(acc_dic,open('accounts/user_info_1234.json','w',encoding='utf8'))

 