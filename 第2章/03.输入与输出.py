# 获取键盘上的数据 -- s = input(提示信息) -- 数据类型均为字符串
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")

print(f"您的姓名是：{name}，年龄是：{age}")

# 案例：银行卡ATM取款
total = 10000  # 总金额

password = input("请输入您的银行卡密码：")
print(f"密码正确，{password}")

num = input("请输入取款金额：")

# num 转为 int类型 -> int(num)
print(f"取款后银行卡余额为：{total - int(num)}")
