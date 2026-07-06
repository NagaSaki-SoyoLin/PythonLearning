# 案例2: 猜数字游戏
import random

random_num = random.randint(1, 100)  # 生成随机数

while True:
    num = int(input("请输入一个数字: "))  # 接收输入的数字

    # 比较
    if num > random_num:
        print("您输入的数字太大了!")
    elif num < random_num:
        print("您输入的数字太小了!")
    else:
        print("恭喜您猜对了!")
        break  # 跳出循环

print("随机生成的数字是:", random_num)
