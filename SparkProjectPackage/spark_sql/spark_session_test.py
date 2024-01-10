# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : spark_session_test.py
# @Date   : 2023/12/20 16:06
# @Author : sunpeng
# -----------------------------

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark") \
    .master("local[*]") \
    .getOrCreate()

spark.stop()
