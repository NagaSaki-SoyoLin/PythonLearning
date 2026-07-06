# while循环: 打印10遍"人生苦短, 我用Python ~"
i = 0

while i < 10:
    print("人生苦短, 我用Python ~")
    i += 1
else:
    print("循环正常结束")

# while案例: 计算1~100之间所有偶数的和
total = 0  # 记录累加之和
i = 1  # 循环开始数字

while i <= 100:
    if i % 2 == 0:  # 偶数
        total += i
    i += 1

print(f"1~100之间的偶数累加之和为: {total}")
