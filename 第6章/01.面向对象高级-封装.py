"""
封装: 将数据(属性)和操作数据的方法绑定在一起, 形成一个独立的单元(类), 保护数据不被外部访问, 通过访问修饰符实现封装
    1. 私有属性: 在属性名前加双下划线 __
    2. 私有方法: 在方法名前加双下划线 __
"""


class Car:

    def __init__(self, brand, model, color):
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色

    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')

    def run(self):  # 行驶
        print(f'{self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')
