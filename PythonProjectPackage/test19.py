# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test19.py
# @Date   : 2023/12/15 10:24
# @Author : sunpeng
# -----------------------------

"""
包
模块多了就组织为包
本质上还是模块,只不过有一个__init__.py文件
在该文件有__all__ 也是管理能用的模块
同样针对的是from 包 import * 这种方式来的
"""

from my_package import *

my_module1.f1()

"""
安装第三方的包
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

"""