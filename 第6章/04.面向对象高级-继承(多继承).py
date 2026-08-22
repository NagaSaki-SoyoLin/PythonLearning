"""
多继承: 一个子类可以继承多个父类
"""


class Car:

    def __init__(self, brand, model, color, owner):
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色
        self.__owner = owner  # 所有人(私有属性)

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):  # 行驶
        print(f'{self.__owner}: {self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃料...')


# 华为智驾
class HuaweiAiDriving:
    """华为AI智能驾驶"""

    def __init__(self, version="V1.0"):
        self.version = version

    def run(self):
        print(f'使用华为AI智能驾驶系统{self.version}正在行驶...')


# 问界汽车
class WenJieCar(Car, HuaweiAiDriving):  # 多继承(父类1, 父类2, ...)
    def __init__(self, brand, model, color, owner, version="V1.0"):
        # super().__init__(brand, model, color, owner)
        Car.__init__(self, brand, model, color, owner)
        HuaweiAiDriving.__init__(self, version)

    def run(self):
        HuaweiAiDriving.run(self)
        Car.run(self)


# MRO: Method Resolution Order -> 方法解析顺序
if __name__ == '__main__':
    c = WenJieCar("问界", "M5", "白色", "王五", "V1.1")
    print(c.__dict__)

    # 查看MRO
    print(WenJieCar.__mro__)
    print(WenJieCar.mro())

    c.run()
