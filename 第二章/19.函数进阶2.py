# ------------------------------函数的参数类型------------------------------
# 加
def add(x, y):
    return x + y


# 减
def subtract(x, y):
    return x - y


# 乘
def multiply(x, y):
    return x * y


# 除
def divide(x, y):
    return x / y


# 计算
def calc(x, y, oper):
    return oper(x, y)


print(calc(10, 20, add))
print(calc(10, 20, subtract))
print(calc(10, 20, multiply))
print(calc(10, 20, divide))

# ------------------------------匿名函数(lambda 参数列表 : 函数体)------------------------------
# 需求1: 打印一个分割线
# def out_line():
#     print("------------------------------")

out_line = lambda: print("------------------------------")
out_line()

# 需求2: 计算两个数之和
# def add(x, y):
#     return x + y

add = lambda x, y: x + y
print(add(10, 20))

# 需求3: 完成如下列表的排序操作, 按照每一个元素的字符个数, 从大到小排序
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key=lambda item: len(item), reverse=True)  # 匿名函数典型的应用场景
print(data_list)


# ------------------------------案例------------------------------
# 案例1: 计算n的阶乘
# 递归调用: 指的是在函数中自己调用自己的情况, 注意必须要有递归终点
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


result = factorial(10)
print(result)

"""
案例2: 定义一个用于根据传入的一批商品信息(商品名, 价格, 数量), 优惠(优惠券, 积分抵扣), 运费信息计算订单的总金额的函数
具体规则如下:
    1. 优惠券需要商品金额满5000才可以使用, 且优惠券金额不能超过商品总价
    2. 积分抵扣需要商品总金额满5000才可以使用, 100积分抵扣1元(且抵扣金额不能超过商品总价, 积分只能整百抵扣)
"""


def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    """
    据传入的一批商品信息(商品名, 价格, 数量), 优惠(优惠券, 积分抵扣), 运费信息计算订单的总金额
    :param args: 商品信息(商品名, 价格, 数量) -> 如: ("鼠标", 188, 2)("键盘", 388, 1)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    # 1. 计算商品金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2. 扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3. 扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    # 4. 添加运费
    total_cost += express

    return total_cost


# 测试
total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 3999, 1), coupon=10, score=4000, express=9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), coupon=10, score=4000, express=9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1), express=9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1))
print(total)
