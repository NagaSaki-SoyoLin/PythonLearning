# 常见数据类型 -> type(数据) 获取指定的字面量或变量的类型
print("Hello")
print(type("Hello"))  # str

print(type(10))  # int
print(type(3.14))  # float
print(type(True))  # bool
print(type(False))  # bool
print(type(None))  # NoneType

num = -100
print(type(num))  # int

# 常见数据类型 -> isinstance(数据, 类型) -> bool值 -> 判断指定的字面量或变量是否是指定类型
print(isinstance(num, int))  # True
print(isinstance(num, float))  # False
print(isinstance(num, bool))  # False

# 定义字符串的三种方式
s1 = "Hello"  # 双引号定义
s2 = 'Python'  # 单引号定义
s3 = """
Hello:
    Python
    !!!
"""  # 三引号定义(多行字符串)

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

# 转义字符 \n 换行 \t 制表符(缩进) \' 单引号 \" 双引号 \\ 反斜杠
msg = "\"Hello\"的意\\思是\n\t'你好'"
print(msg)

# 字符串拼接
s1 = "人生苦短" "我用Python"
print(s1)

msg1 = "人生苦短"
msg2 = "我用Python"
print("龟叔说：" + msg1 + "，" + msg2)

# 案例 -> str(int数字) -> 将int数字转换为字符串
name = "龟叔"
age = 70
print("我是" + name + "，今年" + str(age) + "岁")

# 字符串格式化 -> 方式一：% 占位符
print("我是%s，今年%d岁" % (name, age))

# 字符串格式化 -> 方式二：f"..{变量名/表达式}.." -> 推荐方式
print(f"我是{name}，今年{age}岁")
