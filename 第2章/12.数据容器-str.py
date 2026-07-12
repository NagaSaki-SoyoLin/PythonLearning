# 字符串 基本操作 -> 不可变的(无法修改), 有序性, 可迭代性
s = "Hello-Python"

print(s[4])  # 正向索引, 从 0 开始
print(s[-8])  # 反向索引, 从 -1 开始

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])  # 起始索引默认为 0
print(s[:5:])  # 步长默认为 1
print(s[:5])

print(s[6:12:1])
print(s[6::1])  # 结束索引默认为 -1

# 步长 -> 正数: 从左往右截取, 负数: 从右往左截取
print(s[-1:-7:-1])
print(s[::-1])  # 反转字符串

# 字符串常用方法
s = " Hello-Python-Hello-World"

# find() 查找指定字符串第一次出现的索引位置, 如果不存在则返回 -1
index = s.find("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割, 返回列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格或指定字符
ss = s.strip()
print(ss)

# replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串 开头 / 结尾, 返回布尔值
print(s.startswith("Hello"))
print(s.endswith("World"))

print(s)  # 经过一系列操作, 字符串并没有改变

# 字符串案例
# 案例1: 邮箱格式验证: 用户输入一个邮箱, 验证邮箱格式是否正确(包含一个@和至少一个.), 如果输入正确, 输出"邮箱格式正确", 否则输出"邮箱格式错误"
mail = input("请输入邮箱: ")

if mail.count("@") == 1 and "." in mail:  # in 运算符 -> 判断子串是否存在字符串中, 存在返回 True, 不存在返回 False
    print(f"{mail}是合法的邮箱")
else:
    print(f"{mail}是非法的邮箱")
