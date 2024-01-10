# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : udf_test.py
# @Date   : 2023/12/20 23:09
# @Author : sunpeng
# -----------------------------
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, StringType

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

# 自定义函数,返回一个注册函数,使用这个函数应用在DSL
MyUDF1 = spark.udf.register("MyUDF1", lambda col: "Name:" + col, StringType())

# 使用自定义UDF
df.createOrReplaceTempView("tmp")
# 在SQL使用UDF
spark.sql("select MyUDF1(name) from tmp;").show()
# 在DSL使用UDF
df.select(MyUDF1("name")).show()

spark.stop()
