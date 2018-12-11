"""

    Configparser模块  操作句柄
"""


import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'city':'beijing',
    'address':'shanghai',
    'date':'2018-12-03'
}

config['com.lm.test'] = {}
config['com.lm.test']['user'] = 'James'
config['com.lm.test_11'] = {}
c2 = config['com.lm.test_11']
c2['Host_Address'] = 'http://www.baidu.com'
c2['test']='beer'
config['DEFAULT']['test']='beef'


with open('files/d032.txt','w') as files :
    config.write(files)


config.read('files/d032.txt')

print(config.sections())
print(config.defaults())
print(config['com.lm.test_11']['test'])

# config.remove_section('com.lm.test_11')
#
# print(config.has_section('com.lm.test_11'))
#

config.set('com.lm.test_11','test','banana')

print(config['com.lm.test_11']['test'])

config.remove_option('com.lm.test_11','test')

config.write(open('files/d032.txt','w'))
