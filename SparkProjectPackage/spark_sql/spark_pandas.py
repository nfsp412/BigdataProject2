# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : spark_pandas.py
# @Date   : 2023/12/21 0:29
# @Author : sunpeng
# -----------------------------

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pandas as pd
import os

os.environ['PYSPARK_PYTHON'] = 'C:\\Users\\nfsp4\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'

spark = SparkSession.builder.getOrCreate()

pd_df = pd.DataFrame(
    {
        'id': [1, 2, 3],
        'name': ['John', 'Smith', 'Mary'],
        'age': [20, 30, 30]
    }
)

# 将Pandas的DF转换成Spark的DF
schema_type = StructType().add("ID", StringType(), True).add("Name", StringType()).add("age", IntegerType(), True)
spark_df = spark.createDataFrame(pd_df, schema_type)

#
spark_df.show()
spark_df.printSchema()

# Spark的DF转换成Pandas的DF
pd_df_new = spark_df.toPandas()

spark.stop()
