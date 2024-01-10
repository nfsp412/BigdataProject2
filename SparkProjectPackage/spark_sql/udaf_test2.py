# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : udf_test.py
# @Date   : 2023/12/20 23:09
# @Author : sunpeng
# -----------------------------
from pandas import Series
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, StringType
from pyspark.sql import functions as F
import os

os.environ['PYSPARK_PYTHON'] = 'C:\\Users\\nfsp4\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'

spark = SparkSession.builder.getOrCreate()

r1 = Row(id=1001, name="张三", age=20)
r2 = Row(id=1002, name="李四", age=23)
schema_type = StructType() \
    .add("id", IntegerType(), False) \
    .add("name", StringType(), True) \
    .add("age", IntegerType(), True)
df = spark.createDataFrame([r1, r2], schema_type)
df.show()
df.printSchema()


# 自定义UDAF
# 参数a用来接收整列数据,需要指定为Series类型,返回int类型,这里假设求和的UDAF
# 使用装饰器定义,参数1返回值类型,无需参数2
@F.pandas_udf(IntegerType())
def f1(a: Series) -> int:
    return a.sum()


# 使用register
my_udaf = spark.udf.register('my_udaf', f1)
# 使用
df.select(my_udaf('age')).show()

# 使用sql方式
df.createOrReplaceTempView("tmp")
spark.sql("select my_udaf(age) from tmp").show()

spark.stop()
