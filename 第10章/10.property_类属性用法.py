"""
案例: 演示property属性的用法

property属性介绍:
    概述/目的/作用:
        把 函数 当做 变量来使用
    实现方式:
        方式1: 装饰器
        方式2: 类属性


property的装饰器用法:
    @property               修饰 获取值的函数
    @获取值的函数名.setter     修饰 设置值的函数

property类属性的用法:
    类属性名 = property(获取值的函数名, 设置值的函数名)

    之后, 就可以直接 .上述的函数名 来当做变量直接用
"""


# 需求: 定义学生类, 私有 age属性, 通过property充当类属性用
# 1. 定义学生类
class Student:
    # 1.1 私有age属性
    def __init__(self):
        self.__age = 20

    # 1.2 公共的访问方式
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # 1.3 封装上述的公共方式为 类属性
    # 参1: 获取值的函数名,    参2: 设置值的函数名
    age = property(get_age, set_age)


# 2. 测试
if __name__ == '__main__':
    # 2.1 创建学生对象
    s = Student()
    # 2.2. 设置值
    s.age = 99
    # 2.3 获取值
    print(s.age)
