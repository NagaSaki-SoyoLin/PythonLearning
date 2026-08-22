"""
鸭子类型: 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
         在鸭子类型中, 关注的不是对象的类型本身, 而是它是否具有某个行为
          鸭子类型的优势是不需要存在继承关系,只要对象有相应的方法就能使用
"""


class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Duck: {self.age} 岁的{self.name} 正在游泳 ..')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Dog: {self.age} 岁的{self.name} 正在游泳 ..')


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Pig: {self.age} 岁的{self.name} 正在游泳 ..')


def go_swimming(duck: Duck):
    duck.swimming()


# 测试代码
if __name__ == '__main__':
    go_swimming(Dog(name='旺财', age=4))
    go_swimming(Duck(name='唐老鸭', age=2))
    go_swimming(Pig(name='佩奇', age=1))
