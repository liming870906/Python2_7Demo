"""
程序入口
"""


# 引用os及sys模块
import os,sys

# 获取到atm目标添加到系统目录中
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
# 添加获取到的atm路径
sys.path.append(base_dir)
# print(sys.path)

from core import main_run

if __name__ == '__main__':
    main_run.start_main()