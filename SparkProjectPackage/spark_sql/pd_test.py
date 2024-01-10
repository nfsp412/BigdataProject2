# *-* coding:utf-8 *-*
# -----------------------------
# @Project: pythonProject
# @File   : pd_test.py
# @Date   : 2023/12/20 23:58
# @Author : sunpeng
# -----------------------------

# 如何使用pandas

from pandas import Series, DataFrame

# 定义一列数据
s = Series([1, 2, 3, 4, 5])

# 查看数据
print(s)

# 按照索引取值
print(s[0])

# 手动指定索引
s1 = Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s1)
print(s1['a'])

# 相关方法
print(s.sum())
print(s.mean())
print(s.max())
print(s.min())

# 使用DataFrame类型,并且指定列索引或者说字段名
# 可以通过字典格式定义
df = DataFrame(
    [
        # 第一行,第二行数据
        [101, "张三", 18], [102, "李四", 22]
    ],
    columns=['id', 'name', 'age']
)
print(df)  # 展示二维表格

# 取出数据,先取列索引,后取行索引,一列数据就是Series类型
# 如果设置了列索引名称,那么就不能使用索引下标
# print(df[1][0])
print(df['name'][1])
