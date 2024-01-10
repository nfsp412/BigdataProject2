# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : setup.py
# @Date   : 2023/12/18 22:13
# @Author : sunpeng
# -----------------------------

from distutils.core import setup

setup(name='my_utils',
      version='1.0',
      description='工具包',
      long_description='工具包 完整信息',
      author='<NAME>',
      author_email='5@163.com',
      url='https://github.com',
      py_modules=['my_utils.file_util', 'my_utils.str_util'])
