# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : hello.py
# @Date   : 2023/12/13 20:24
# @Author : sunpeng
# -----------------------------
import random

if __name__ == '__main__':
    print("Hello World")
    print("helo", "1")
    print(1 + 2)
    money = 50
    print(money)
    print(type(money))
    name = "sunpeng"
    print(type(name))
    weight = 180.3
    print(type(weight))
    # type可以查看数据类型, 返回值就是该数据类型, 可以打印查看
    sql = """
    insert overwrite table tb1
    select *
    from base;
    """
    print(sql)
    name = "1"
    print(int(name))
    intName = int(name)
    print(intName)
    # 任何类型都可以转换成字符串
    f1 = 1.1
    i1 = int(f1)
    # 会丢失精度
    print(i1)
    """
    标识符命名规则
    数字字母下划线
    数字不能开头
    大小写敏感
    关键字和保留字不能使用
    区别于Java, 使用下划线全小写命名
    """
    """
    +-*/ //整除 %取余 **求平方
    """
    print(10 // 3)
    print(10 % 3)
    print(10 ** 3)
    """
    赋值运算符
    = += -= *= /= //= %= **=
    """
    a = 1
    a += 1
    print(a)
    b = 2
    b -= 1
    print(b)
    c = 3
    c *= 2
    print(c)
    d = 4
    d /= 2
    print(d)
    e = 5
    e //= 2
    print(e)
    f = 6
    f %= 2
    print(f)
    g = 7
    g **= 2
    print(g)
    """
    字符串三种定义:
    单引号, 可以包含双引号
    双引号, 可以包含单引号
    使用转义字符(\), 让引号变成普通字符
    三引号, 支持换行书写, 注意前面会有空格或者tab, 使用变量接收就是字符串, 不使用变量接收就是多行注释
    """
    print("\"\'")  # "'
    """
    字符串拼接
    使用加号(+)
    和Java不同, 不能拼接非字符串变量
    """
    """
    格式化输出字符串
    %s 
    %d 
    %f 
    """
    name = "sunpeng"
    age = 18
    height = 140.2
    print("我的名字是: %s, 我的年龄是: %d, 我的体重是: %d" % (name, age, height))
    """
    格式化字符串的精度控制
    %5d 可以用来空格补位 
    %5.2f 宽度5, 小数2
    m和.n都可以省略
    m如果比数字宽度小, 则不生效
    .n会进行四舍五入
    """
    money = 18.2333
    print("金额是: %.2f" % money)
    a = 3
    print("变量a: %5d" % a)
    """
    格式化字符串2
    使用f符号
    不会进行精度控制,也不会考虑类型
    """
    print(f"我是{name},我的年龄是{age},我的体重是{weight}")
    """
    直接输出表达式
    """
    print("1+1=%d" % (1 + 1))
    print(f"1+1={1 + 1}")
    print("类型是%s" % type(name))
    name = "传智播客"
    stock_price = 19.99
    stock_code = "003032"
    stock_price_daily_growth_factor = 1.2
    growth_days = 7
    print(f"公司: {name}, 股票代码: {stock_code}, 当前股价: {stock_price}")
    print("每日增长系数是: %.1f, 经过%d天的增长后, 股价达到了: %.2f" % (stock_price_daily_growth_factor, growth_days,
                                                                        stock_price * stock_price_daily_growth_factor ** growth_days))
    """
    输入: input
    可以在input输入提示语
    键盘输入的内容都理解为字符串类型
    """
    # print("请输入姓名: ")
    # name = input()
    # print(name)
    # user_name = input("请输入姓名")
    # user_type = input("请输入类型")
    # print(f"您好: {user_name}, 您是尊贵的: {user_type} 用户, 欢迎登录")
    a = True
    b = False
    print(f"a:{a},type:{type(a)}")
    print(f"b:{b},type:{type(b)}")
    """
    布尔类型值可以使用字面量定义, 也可以通过比较运算符得到
    比较运算符
    == != > < >= <=
    """
    res = 10 > 5
    print(res)
    """
    if语句: 使用四个空格缩进, 不要忘记后面的引号
    """
    if 10 > 5:
        print("10>5")
    else:
        print("10 < 5")
    print("欢迎")
    age = int(input("请输入年龄: "))

    if age > 18:
        print("请补票")
    else:
        print("欢迎")
    """
    使用int()进行强制类型转换
    """
    weight = float(input("请输入身高"))
    if weight > 120:
        print("超过120")
    else:
        print("未超过120")

    """
    if elif 按照顺序判断, 互斥
    注意空格缩进, 通过空格缩进来判断关系
    """
    a = 10

    if a == int(input("第一次")):
        print("yes")
    elif a == int(input("第二次")):
        print("yes")
    elif a == int(input("第三次")):
        print("yes")
    else:
        print("次数用完")

