# if条件判断：如果分数超过680，就去清华读书
score = int(input("请输入你的分数："))
if score > 680:
    print("欢迎你来清华读书")
    print("也恭喜你即将踏入精彩的大学生活")

print("------------------------")

# if案例：完成B站登陆功能的实现
# 正确的账号和密码
ok_account = "18888888888"
ok_password = "666888"

# 1. 接收用户输入的账号和密码
account = input("请输入你的账号：")
password = input("请输入你的密码：")

# 2. 判断账号和密码是否正确，如果正确则登录成功进入B站首页
if account == ok_account and password == ok_password:
    print("登录成功 ~")
    print("进入B站首页 ~")

# 3. 如果账号或密码不正确，则提示用户账号或密码错误
if account != ok_account or password != ok_password:
    print("登录失败 ！")
    print("账号或密码错误 ！")

# if...else...案例：完成B站登陆功能的实现
# 正确的账号和密码
ok_account = "18888888888"
ok_password = "666888"

# 1. 接收用户输入的账号和密码
account = input("请输入你的账号：")
password = input("请输入你的密码：")

# 2. 判断账号和密码是否正确，如果正确则登录成功进入B站首页，否则提示用户账号或密码错误
if account == ok_account and password == ok_password:
    print("登录成功 ~")
    print("进入B站首页 ~")
else:
    print("登录失败 ！")
    print("账号或密码错误 ！")

# 案例1：根据用户输入的年份，判断是闰年还是平年
year = int(input("请输入需要判定的年份："))

if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")

# if...elif...else... 案例：根据用户输入的数字，判断是正数，负数还是零
num = int(input("请输入一个数字："))

if num > 0:
    print(f"{num}是正数")
elif num < 0:
    print(f"{num}是负数")
else:
    print(f"{num}是零")

# 多行注释使用三引号
"""
案例：角形类型判断:根据输入的三个边的边长（正整数）,判定是等边三角形、等腰三角形、普通三角形,还是不能构成三角形。
    1. 构成三角形的条件：两边之和大于第三边
    2. 三角形判定规则：
        三个边都相等：等边三角形
        两个边相等：等腰三角形
        三个边都不相等：普通三角形
"""
# 1. 接收用户输入的三个边长
a = int(input("请输入第一个边长："))
b = int(input("请输入第二个边长："))
c = int(input("请输入第三个边长："))

# 2. 判断是否构成三角形 -- pass 是一个空语句，起到一个语法占位的作用
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print(f"{a},{b},{c}这三个边长构成等边三角形 ~")
    elif a == b or b == c or a == c:
        print(f"{a},{b},{c}这三个边长构成等腰三角形 ~")
    else:
        print(f"{a},{b},{c}这三个边长构成普通三角形 ~")
else:
    print(f"{a},{b},{c}这三个边长不能构成三角形！！！")
