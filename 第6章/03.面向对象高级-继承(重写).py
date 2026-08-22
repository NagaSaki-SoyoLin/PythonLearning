"""
重写: 子类中与父类同名的方法, 会覆盖父类中的方法
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


# 燃油车
class FuelCar(Car):
    def charge(self):
        # 调用父类中的charge方法, 方式一: super().方法名()
        super().charge()
        print(f'{self.brand} {self.model} 正在加油...')


# 电动车
class ElectricCar(Car):
    def charge(self):
        # 调用父类中的charge方法, 方式二: 类名.方法名(self)
        Car.charge(self)
        print(f'{self.brand} {self.model} 正在充电...')


if __name__ == '__main__':
    c1 = FuelCar("宝马", "X5", "黑色", "张三")
    c1.charge()
    c2 = ElectricCar("特斯拉", "Model 3", "白色", "李四")
    c2.charge()
