"""
继承: 描述的是两个类之间的关系, 子类继承父类, 就可以获取到父类中的属性和方法(非私有)
"""


class Car(object):  # python中的object是所有类的基类, 定义类时默认继承object类

    def __init__(self, brand, model, color, owner):
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色
        self.__owner = owner  # 所有人(私有属性)

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):  # 行驶
        print(f'{self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def get_owner(self):  # 获取所有人
        return self.__owner[0:1] + "**"

    def set_owner(self, owner):  # 设置所有人
        self.__owner = owner

    def __control_fuel(self):  # 控制燃油(私有方法)
        print(f'{self.brand} {self.model} 正在控制燃油...')


# 燃油车
class FuelCar(Car):
    pass


# 电动车
class ElectricCar(Car):
    pass


if __name__ == '__main__':
    c1 = FuelCar("宝马", "X5", "黑色", "张三")
    c1.start()
    c1.run()
    c1.stop()
    print(c1.get_owner())
    print(c1.model)
    print(c1.color)
