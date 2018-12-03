# Python 模块
"""
hashlib
加密

"""

import hashlib

m = hashlib.md5()

m.update('abcedfg'.encode('utf-8'))
print(m.hexdigest())

s = hashlib.sha3_256()
s.update('abcedfg'.encode('utf-8'))
print(s.hexdigest())
print("分隔符".center(100,'-'))

"""
sys 模块
    Python解释器进行交互。
"""
import sys

# print(sys.argv)
# if sys.argv[1] == 'post':
#     print('上传')
print(sys.path)
print("分隔符".center(100,'-'))

"""
os模块
    操作系统交互。
"""

from os import path
import os

# print(os.chdir('/Users/liming'))
print(os.getcwd())
print(os.curdir)
# print(os.makedirs('/Users/liming/abc/123/mmmm'))
# print(os.removedirs('/Users/liming/abc/123/mmmm'))
print(os.listdir())
# os.remove('xxx')   只能删除文件，不能删除文件夹。
# os.rename('oldname','newname')  重命名
info = os.stat('./D030_Module.py')
print(info)
print(info.st_size)
print(os.sep)#路径分隔符'/'也就是斜线
print(os.linesep)# \r\t
print(os.pathsep)#  分隔符  Windows 为'；'  Linux为'：'

print(path.isabs(os.getcwd()))
print(path.isfile(os.getcwd()))

print(os.system('ls'))
print(os.environ)
print(os.path.abspath('./'))
print(os.path.split('./files'))