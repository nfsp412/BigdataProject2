# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : schema_test.py
# @Date   : 2023/12/20 16:01
# @Author : sunpeng
# -----------------------------

from pyspark.sql.types import StructType, IntegerType, StringType

# 定义StructType
# 参数1 字段名
# 参数2 字段类型
# 参数3 是否为空,默认允许为空
structType = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True)

