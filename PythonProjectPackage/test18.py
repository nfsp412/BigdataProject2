# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test18.py
# @Date   : 2023/12/15 10:09
# @Author : sunpeng
# -----------------------------

"""
模块和包
模块指的是以.py结尾,能定义函数,类,变量,方法
导入:
import 模块
import 模块 as 别名
from 模块 import 类,变量,方法
from 模块 import *
from 模块 import 功能 as 别名


"""
import time
from time import sleep

# time.sleep(1)
# sleep(1)

import time as tt
from time import sleep as sl

# tt.sleep(1)
# sl(1)

"""
自定义模块
当我们自定义模块,然后进行测试时,我们应该在main中测试
"""
import my_module1

my_module1.test(1, 2)

from my_module1 import test

test(1, 2)

"""
当导入多个重名功能时,会使用最后一个,因为代码是按照顺序执行的
"""

"""
使用__all__来设置有哪些功能我们能够使用,是一个列表
我们导入from 模块 import *,只能使用__all__里面的功能
但是实际上还是能使用的,例如from 模块 import 功能
或者import 模块,然后模块.功能 
"""

