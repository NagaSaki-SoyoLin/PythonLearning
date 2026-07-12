# 定义类 ---> 不推荐定义类后动态地为对象添加属性
class Car:
    pass


# 创建对象
c1 = Car()
# 动态地为对象添加属性
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000

print(c1)
print(c1.brand)
print(c1.__dict__)  # 会将对象中的所有属性以字典的形式输出出来


# 定义类
class Car:
    # __init__ 方法: 初始化方法, 在创建对象时会自动调用, 可以在该方法中为对象设置属性
    # self: 是第一个参数, 表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象的初始化完毕, 对象属性已经添加完毕.")


# 创建对象
c1 = Car("红色", "BMW", "X7", 800000)
print(c1.__dict__)

c2 = Car("蓝色", "奔驰", "E300", 450000)
print(c2.__dict__)


# ------------------------------定义类-实例方法------------------------------
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象的初始化完毕, 对象属性已经添加完毕.")

    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中...")

    def total_cost(self, discount, rate=0.1):
        """
        计算提车的总费用, 包含两个部分: 车的价格, 税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost = self.price * discount + self.price * rate
        return total_cost


# 测试
c1 = Car("红色", "BMW", "X7", 800000)

# 调用对象中的方法
c1.running()

total1 = c1.total_cost(0.9, 0.1)
print(total1)

total2 = c1.total_cost(0.9)
print(total2)


# ------------------------------定义类-魔法方法------------------------------
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象的初始化完毕, 对象属性已经添加完毕.")

    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中...")

    def total_cost(self, discount, rate=0.1):
        """
        计算提车的总费用, 包含两个部分: 车的价格, 税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost = self.price * discount + self.price * rate
        return total_cost

    # 魔法方法
    def __str__(self):  # 在打印对象时, 会自动调用该方法, 将该方法的返回值打印出来
        return f"{self.brand} {self.name} {self.color} {self.price}"

    def __eq__(self, other):  # 在比较两个对象是否相等时, 会自动调用该方法, 如果该方法的返回值为True, 则认为两个对象相等, 否则不相等
        return self.price == other.price and self.brand == other.brand and self.name == other.name and self.color == other.color

    def __lt__(self, other):  # 在比较两个对象的大小时, 会自动调用该方法, 如果该方法的返回值为True, 则认为第一个对象小于第二个对象, 否则不小于
        return self.price < other.price


# 测试
c1 = Car("白色", "BYD", "汉", 180005)
print(c1)

c2 = Car("白色", "BYD", "汉", 180000)
print(c2)

print(c1 == c2)

print(c1 > c2)


# ------------------------------实例属性与类属性------------------------------
class Car:
    # 类属性 (所有实例对象共享的)
    wheel = 4  # 轮胎数量
    tax_rate = 0.1  # 购置税税率

    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象的初始化完毕, 对象属性已经添加完毕.")

    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中...")

    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + self.price * rate
        return total_cost


# 测试
c1 = Car("白色", "BYD", "汉", 180000)
print(c1.brand)
print(c1.wheel)  # 通过实例对象查找属性时, 会先在实例对象中查找, 如果没有找到, 则会继续在类对象中查找

# 通过类名访问类属性
print(Car.wheel)
