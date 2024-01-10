# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test28.py
# @Date   : 2023/12/15 16:58
# @Author : sunpeng
# -----------------------------

"""
pymysql
"""

from pymysql import Connection

con = Connection(
    host='localhost',
    user='root',
    password='123456',
    port=3306,
    autocommit=True
)

# 查看MySQL版本信息
print(con.get_server_info())

# 先获取游标
cursor = con.cursor()
# 使用游标执行sql
cursor.execute("select * from db1.tb1;")
# 使用游标获取查询结果
# 获取的结果是元组,里面嵌套元组,一个元组是一行数据
res: tuple = cursor.fetchall()
for i in res:
    print(i)

id: int = 1003
name: str = "王五"
# 这里注意都是%s类型,而不是%d
cursor.execute("insert into db1.tb1 (id, name) values (%s, %s)", (id, name))

# 或者手动提交
# con.commit()
# 选择数据库
con.select_db("db1")

con.close()
