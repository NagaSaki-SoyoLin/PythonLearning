# for循环: 遍历输入的字符串
msg = input("请输入需要遍历的字符串: ")

for s in msg:  # s 表示遍历出来的元素; msg 表示需要遍历的数据
    print(f"元素: {s}")
else:
    print("遍历正常结束!")

"""range函数用于生成指定规则的数字序列

range(end) -> 从 0 开始, 到 end-1 结束, 步长为 1
range(start, end) -> 从 start 开始, 到 end-1 结束, 步长为 1
range(start, end, step) -> 从 start 开始, 到end-1 结束, 步长为 step(可以是负数)
"""

# 案例1: 计算 1~100 之间所有的奇数之和
total = 0  # 记录累加之和

# 原始
# for i in range(1, 101):
#     if i % 2 == 1:
#         total += i

# 简化
for i in range(1, 101, 2):
    total += i

print("1~100 之间所有的奇数之和为:", total)

# 案例2: 计算 100~500 之间所有3的倍数的数字之和
total = 0  # 记录累加之和

for i in range(100, 501):
    if i % 3 == 0:  # i是3的倍数
        total += i

print("100~500 之间所有3的倍数的数字之和为:", total)

# 循环嵌套: 根据输入的长方形的长度 m, 宽度 n, 用*打印一个长方形
# 1. 接受键盘录入m, n
m = int(input("请输入长方形的长度: "))  # 长度
n = int(input("请输入长方形的宽度: "))  # 宽度

# 2. 打印长方形
for i in range(n):  # 控制行
    for j in range(m):  # 控制列
        print("*", end="  ")  # end 表示每一次输出以什么结束, 默认是换行符 \n
    print()  # 不加 end 默认换行

# 嵌套循环案例: 打印99乘法表
for i in range(1, 10): # 外层循环 - 控制行
    for j in range(1, i + 1): # 内层循环 - 控制列
        print(f"{j} x {i} = {j * i}", end="\t")
    print()
