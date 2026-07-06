# 算术运算符：+  -  *  /  //  %  **
print("10 + 4 =", 10 + 4)  # 加
print("10 - 4 =", 10 - 4)  # 减
print("10 * 4 =", 10 * 4)  # 乘
print("10 / 4 =", 10 / 4)  # 除（结果为浮点数）
print("10 // 4 =", 10 // 4)  # 整除（结果为整数）
print("10 % 4 =", 10 % 4)  # 取余/求模
print("10 ** 4 =", 10 ** 4)  # 幂指数，10的4次方

# 算术运算符的优先级：**  ->  *  /  //  %  ->  +  -


# 案例：输入两个数字，计算两个数字的和与差
x = float(input("请输入x的值："))
y = float(input("请输入y的值："))

# 涉及浮点数的运算，可能会损失精度
print("x + y = ", x + y)
print("x - y = ", x - y)

# 赋值运算符：= +=  -=  *=  /=  //=  %= **=
num = 85

num += 10  # num = num + 10
print("num += 10 后，num = ", num)  # 95

num -= 10  # num = num - 10
print("num -= 10 后，num = ", num)  # 85

num *= 10  # num = num * 10
print("num *= 10 后，num = ", num)  # 850

num /= 10  # num = num / 10
print("num /= 10 后，num = ", num)  # 85.0

num //= 10  # num = num
print("num //= 10 后，num = ", num)  # 8.0（浮点数参与整除运算结果则为浮点数）

num %= 3  # num = num % 3
print("num %= 10 后，num = ", num)  # 2.0

num **= 3  # num = num ** 3
print("num **= 3 后，num = ", num)  # 8.0

# 比较运算符：==  !=  >  <  >=  <=
print("100 == 100 吗 : ", 100 == 100)  # True
print("'100' == '100' 吗 : ", "100" == "100")  # True
print("100 != 100 吗 : ", 100 != 100)  # False

print("100 < 100 吗 : ", 100 < 100)  # False
print("100 <= 100 吗 ", 100 <= 100)  # True

print("100 > 100 吗 : ", 100 > 100)  # False
print("100 >= 100 吗 ", 100 >= 100)  # True

# 逻辑运算符：and  or  not
num = int(input("请输入一个整数："))

print(f"{num} 在0-100之间吗？{num >= 0 and num <= 100}")  # and（并且，同时成立）
print(f"{num} 在0-100之外吗？{num < 0 or num > 100}")  # or（或者，满足其一）
print(f"{num} 在0-100之外吗？{not (num >= 0 and num <= 100)}")  # not（非，取反操作）
