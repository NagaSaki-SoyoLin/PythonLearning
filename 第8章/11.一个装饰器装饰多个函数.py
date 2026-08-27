"""
案例:演示 带参数的装饰器

记忆:
    1. 一个装饰器的参数有且只能有一个
    2. 如果装饰器有多个参数, 可以在该装饰器的外边再包裹一层, 把该装饰器当作其 内部函数 返回即可
"""


# 需求: 定义一个既能装饰加法, 又能装饰减法的装饰器 -> 即带有参数的装饰器
# 1. 定义装饰器
def logging(flag):
    def my_decorator(fn_name):
        # 1.1 定义内函数, 格式要和原函数保持一致
        def fn_inner(a, b):
            # 1.2 额外功能
            if flag == '+':
                print("正在努力计算 [加法] 中...")
            elif flag == '-':
                print("正在努力计算 [减法] 中...")
            # 1.3 调用原函数
            return fn_name(a, b)

        # 1.4 返回内函数
        return fn_inner

    # 返回 my_decorator 函数
    return my_decorator


# 2. 定义原函数, 表示: 加法运算
@logging('+')
def get_sum(a, b):
    return a + b


# 3. 定义原函数, 表示: 减法运算
@logging('-')
def get_sub(a, b):
    return a - b


# 4. 测试
print(get_sum(1, 2))
print('-' * 25)
print(get_sub(1, 2))
