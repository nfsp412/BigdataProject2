# -*- coding: utf-8 -*
# -----------------------------
# @Project: pythonProject
# @File   : ATM.py
# @Date   : 2023/12/14 20:29
# @Author : sunpeng
# -----------------------------

def check_balance():
    """
    查询余额函数
    :return: 余额
    """
    print(f"余额: {money}")
    return money


def save_money(save_money):
    """
    存款函数
    :param save_money: 存款金额
    :return: 存款后余额
    """
    if save_money < 0:
        print("存款金额不能为负数")
        return
    global money
    money += save_money
    return money


def get_money(get_money):
    """
    取款函数
    :param get_money: 取款金额
    :return: 取款后余额
    """
    if get_money < 0:
        print("取款金额不能为负数")
        return
    global money
    if get_money > money:
        print("取款金额超过余额")
        return
    money -= get_money
    return money


def main_menu(name):
    """

    :param name:
    :return:
    """
    print(f"{name}您好, 欢迎, 请选择序号")
    print("查询 [1]")
    print("存款 [2]")
    print("取款 [3]")
    print("退出 [4]")


if __name__ == '__main__':
    money = 5000000
    name = input("姓名")

    while True:
        main_menu(name)
        choice = int(input("请输入操作"))
        if choice == 1:
            check_balance()
        elif choice == 2:
            save_money(float(input("请输入存款金额")))
        elif choice == 3:
            get_money(float(input("请输入取款金额")))
        elif choice == 4:
            print("退出,再见")
            break
