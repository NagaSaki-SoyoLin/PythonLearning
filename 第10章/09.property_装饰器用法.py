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

    之后, 就可以直接 .上述的函数名 来当做变量直接用
"""


# 需求: 定义学生类, 私有属性 age, 通过property实现简化调用
# 1. 定义学生类
class Student:
    # 1.1 私有属性
    def __init__(self):
        self.__age = 18

    # 1.2 提供公共的方式方式
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        # 可以在这里对传入的age值做判断, 但是一般不做, 重要字段才会做判断
        # 因为实际开发中数据是从前端传过来的, 已经做过判断了, 这里做属于二次校验
        self.__age = age


# 2. 测试
if __name__ == '__main__':
    # 2.1 创建学生对象
    s = Student()
    # 2.2. 设置值
    s.age = 20
    # 2.3 获取值
    print(s.age)
