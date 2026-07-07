# 注意: 函数定义的时候不会执行, 函数被调用才会执行; 函数必须先定义后调用
# 函数定义
def out_line():
    print("-------------------------")
    print("-------------------------")


# 函数调用
out_line()


# 函数的参数与返回值
# 函数1: 计算圆的面积 -- 半径
def circle_area(r):
    area = 3.14 * r ** 2
    return area


area1 = circle_area(10)
print(area1)


# 函数2: 计算长方形的面积 -- 长, 宽
def rectangle_area(l, w):
    """
    根据长方形的长和宽, 计算长方形的面积
    :param l: 长
    :param w: 宽
    :return: 面积
    """
    return l * w


help(rectangle_area)  # 查看函数的帮助文档
print(rectangle_area(20, 10))


# 函数3: 计算圆的面积, 周长 -- 半径 -> 如果函数返回值有多个, 用逗号分隔, 封装到元组之中
def circle_area_perimeter(r):
    """
    根据圆的半径, 计算圆的面积和周长
    :param r: 半径
    :return: 元组(面积, 周长)
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)  # round函数精确到小数点后1位


ap = circle_area_perimeter(10)
print(ap)
print(type(ap))

area3, perimeter3 = circle_area_perimeter(10)  # 元组解包操作
print(area3)
print(perimeter3)


# 函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")


def function_b():
    print("b ... before")
    function_c()
    print("b ... after")


def function_c():
    print("c ... ")


function_a()
print("函数调用完毕 ~")
