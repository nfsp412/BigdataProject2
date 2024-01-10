# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test9.py
# @Date   : 2023/12/14 21:53
# @Author : sunpeng
# -----------------------------


"""
字符串str
无法修改
只能存储字符串,不可修改,不可变
"""
str1 = "Hello"
str3 = ""
str2 = str("abc")
print(str2)
print(str3)



"""
索引查询字符
index查询子串的第一个字符的索引
replace将子串替换为新的子串,由于不可变,所以得到一个新的字符串
split按照分隔符切割,也是得到新的列表,旧的字符串不变
strip去除前后空格和换行符
strip去除前后的指定的所有的字符,直到没有匹配到为止
统计子串的出现的次数,count,从前到后匹配完,不会重复匹配,
len统计字符的数量,注意数字,字母,符号,中文,都是一个字符,但是不代表是一个字节
"""
print(str1[1])
print(str1.index("el"))

str2 = str1.replace("el", "AA")
print(str1)
print(str2)

print(str1.split("e"))
print(str1)

str1 = "  he  "
print(str1.strip())

str2 = "aasa是是是sssa"
print(str2.strip("as"))

print(str2.count('是是'))

str1 = "itheima itcast boxuegu"
print(str1)
print(str1.count("it"))
new = str1.replace(" ","|")
print(new)
new2 = new.split("|")
print(new2)

