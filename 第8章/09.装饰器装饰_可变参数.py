# 需求: 定义1个可以计算多个数据和字典value值和的函数, 并给其友好提示
# 1. 定义装饰器
def my_decorator(fn_name):
    # 1.1 定义内函数
    def fn_inner(*args, **kwargs):
        # 1.2 额外功能
        print("正在努力计算中...")
        # 1.3 调用原函数
        return fn_name(*args, **kwargs)

    # 1.4 返回内函数
    return fn_inner


# 2. 定义原函数
@my_decorator
def get_sum(*args, **kwargs):
    """
    该函数用于计算 数字元组 和 字典value值 之和
    :param args: 数字元组, *args -> 接收所有的位置参数, 封装到元组
    :param kwargs: 字典, 键是字符串, 值是数字, **kwargs -> 接收所有的关键字参数, 封装到字典
    :return: 结果之和
    """
    # # 2.1 定义求和变量
    # sum = 0
    # # 2.2 遍历元组, 获取每个元素, 求和
    # for i in args:
    #     sum += i
    # # 2.3 遍历字典, 获取到每个值
    # for v in kwargs.values():
    #     sum += v
    # # 2.4 返回结果
    # return sum

    # 优化代码
    return sum(args) + sum(kwargs.values())


# 3. 测试
print(get_sum(1, 2, 3, a=4, b=5, c=6))
