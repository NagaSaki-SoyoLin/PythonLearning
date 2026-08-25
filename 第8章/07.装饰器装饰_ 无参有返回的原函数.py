"""
案例: 装饰器装饰_无参有返回的原函数

细节:
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致,
    即:  原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的
        原函数有参有返回的, 则 装饰器的内部函数也必须是 有参有返回的
"""


# 需求: 定义无参有返回值的 get_sum()求和函数, 在不改变其代码的基础上, 添加友好提示:正在努力计算中...
# 1. 定义装饰器
def my_decorator(fn_name):  # fn_name: 被装饰的函数名
    # 1.1 定义内部函数
    def fn_inner():
        # 1.2 # 额外功能
        print('正在努力计算中...')
        # 1.3 # 有引用
        return fn_name()

    # 1.4 有返回, 把 内部函数对象 作为外部函数的执行结果进行返回
    return fn_inner  # 有返回


# 2. 定义原函数
@my_decorator
def get_sum():
    a = 11
    b = 22
    return a + b


# 3. 测试
# 3.1 传统写法
# get_sum = my_decorator(get_sum) # 本质: get_sum = fn_inner
# sum = get_sum()
# print(f'sum求和结果: {sum}')

# 3.2 语法糖写法
print(f'sum求和结果: {get_sum()}')
