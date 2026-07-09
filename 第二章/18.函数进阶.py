# ---------------------------------函数-变量的作用域---------------------------------
# 全局变量: 在函数的外部和函数的内部都是可以访问的
num = 100


# 定义函数
def circle_area(r):
    # 局部变量: 只能在函数内部使用
    pi = 3.14
    area = pi * r * r

    global num  # global关键字可以声明全局变量
    num = 10000  # 先声明后使用, 修改全局变量
    print("num = ", num)  # 10000

    return area


# 调用函数
c_area = circle_area(10)
print(c_area)
print("num = ", num)  # 10000


# ---------------------------------函数-传参方式---------------------------------
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功, 姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 传参方式一: 位置参数 -> 顺序必须正确
stu = reg_stu("张三", 18, "男", "北京")
print(stu)

# 传参方式二: 关键字参数 -> 顺序不要求
stu = reg_stu(name="王林", age=28, gender="男", city="北京")
print(stu)

stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
print(stu)

# 传参方式三: 位置参数 + 关键字参数 -> 位置参数在前, 关键字参数在后
stu = reg_stu("李慕婉", age=20, city="北京", gender="女")
print(stu)


# ---------------------------------函数-默认参数---------------------------------
# 定义函数
def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功, 姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 调用函数
stu = reg_stu("王林", 20)
print(stu)

stu = reg_stu("李慕婉", 18, "女")
print(stu)

stu = reg_stu("韩立", 22, city="上海")
print(stu)


# ---------------------------------函数-不定长参数(位置参数 *args -> args是元组)---------------------------------
# 需求: 根据传入的数据, 计算这批数据的最大值, 最小值和平均值
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)


# 调用函数
print(calc_data(2, 7, 9, 10, 45))

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))


# ---------------------------------函数-不定长参数(关键字参数 *kwargs -> kwargs是字典)---------------------------------
# 需求: 根据传入的数据, 计算这批数据的最大值, 最小值和平均值
def calc_data(*args, **kwargs):
    """
    根据传入的数据, 计算这批数据的最大值, 最小值和平均值
    :param args: 不定长位置参数, 需要计算的这批数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数位个数
        print: 是否打印输出
    :return: 最小值, 最大值, 平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值: {avg_data}")

    return min_data, max_data, avg_data


# 调用函数
print(calc_data(2, 7, 9, 10, 45, round=3, print=True))

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, round=4, print=False))
