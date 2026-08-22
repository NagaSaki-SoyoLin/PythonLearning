"""
多态: 指同一个方法, 具有不同的形态、行为、表现
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
        print(f'{self.brand} {self.model} 正在加油...')


# 电动车
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在充电...')


# 补充燃料函数
def handle_charge(car: Car):  # 参数类型为Car的子类对象(包括Car本身)
    car.charge()


# 测试代码
if __name__ == '__main__':
    handle_charge(FuelCar("宝马", "X5", "黑色", "张三"))
    handle_charge(ElectricCar("特斯拉", "Model 3", "白色", "李四"))
