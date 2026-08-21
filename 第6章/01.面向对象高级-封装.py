"""
封装: 将数据(属性)和操作数据的方法绑定在一起, 形成一个独立的单元(类), 保护数据不被外部访问, 通过访问修饰符实现封装
    1. 私有属性: 在属性名前加双下划线 __
    2. 私有方法: 在方法名前加双下划线 __
注意: python中没有真正的私有机制, 只是通过命名规则来区分私有属性和私有方法, 但是可以通过 _类名__属性名 来访问私有属性
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
        print(f'{self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def get_owner(self):  # 获取所有人
        return self.__owner

    def set_owner(self, owner):  # 设置所有人
        self.__owner = owner

    def __control_fuel(self):  # 控制燃油(私有方法)
        print(f'{self.brand} {self.model} 正在控制燃油...')


if __name__ == '__main__':
    car = Car('宝马', 'X5', '黑色', '张三')
    print(car.get_owner())
