# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : test14.py
# @Date   : 2023/12/15 8:45
# @Author : sunpeng
# -----------------------------

"""
文件操作
如何查看文件编码:例如使用记事本等软件
编码和解码一致性
文件操作三步骤:
打开文件
读写文件
关闭文件
"""
# f是一个文件对象
# f = open("1.txt",'r',encoding='utf8')
f = open("C:\\sunpeng\\pythonProject\\1.txt", 'r', encoding='utf8')

"""
使用open函数得到一个文件对象f,
该函数有三个参数,
参数1文件路径,相对或者绝对路径,绝对路径如果是window需要双\\
参数2是打开的模式,即对于文件的访问模式,有r只读,w只写(文件不存在是新增,文件存在是覆盖写),a追加(文件不存在是新增,文件存在是追加写)
参数3是编码格式
"""

# print(f)

# cnt = f.read(1024)
# print(type(cnt))
# print(cnt)
# for i in cnt:
#     print(i)

"""
得到的f文件对象,有多种方法
read(字节数),默认读取文件所有内容,可以指定一次性读取的字节数
这里注意,中文会理解为1个字节?字符?
换行符等特殊字符也会读取出来,那么打印的时候也会打印出来
一般会设置1024,然后通过循环方式读取

readlines,一次性读取一行
可以传入参数,代表读取几行数据,默认不传入是读取所有数据

readline,一次性读取一行,读完为止,所以应该结合循环和异常判断

read和readlines区别在于,read返回str字符串,不会显式的展示特殊字符
而readlines返回列表,每一行的数据是一个元素,特殊字符也会展示出来
readline,一次性读取一行,参数指的是读取一行的几个字符?字节?,可以读取多次,每一次从之前结束的位置读取
不传参数就是一次读一行,传参数就是一次读几个
"""
# cnt2 = f.readlines()
# print(cnt2)
# print(type(cnt2))

# c = f.readline()
# print(c)
#
# print("第二次")
# c = f.readline()
# print(c)
#
# print("第三次")
# c = f.readline()
# print(c)
# print("结束")

# 循环读取,直接遍历f文件对象,每一个元素就是一行数据
# for i in f:
#     print("占位")
#     print(i)


f.close()

# 使用with语法避免忘记close关闭资源,
# with open('C:\\sunpeng\\pythonProject\\1.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)


# 统计单词次数
num = 0
with open("datas/2.txt", "r", encoding="utf-8") as f:
    # 获取每一行数据
    for line in f:
        for i in line.strip().split(" "):
            # 得到的list会携带\n特殊字符,所以需要去除,使用replace或者strip去除
            # strip可以去除空格和换行符
            if i == "itheima":
                num += 1
print(num)
