"""
案例: 闭包入门

闭包解释:
    概述:
        内部函数 使用了外部函数的变量,这种写法就称之为闭包
    格式:
        def 外部函数名(形参列表):
            外部函数的(局部)变量

            def 内部函数名(形参列表):
                使用外部函数的变量

            return 内部函数名

细节:
    1. 函数名 和 函数名() 是两个概念, 前者表示 函数对象, 后者表示 调用函数, 获取返回值
"""


# 案例1: 函数名 -> 是对象
def get_sum(a, b):
    return a + b


print(get_sum)  # <function get_sum at 0x000001D9E99B32E0>, 对象
print(get_sum(10, 20))  # 调用函数, 获取返回值

# 函数名可以赋值给变量, 这个变量就是: 函数对象
my_sum = get_sum
print(my_sum)  # <function get_sum at 0x000001D9E99B32E0>
print(my_sum(100, 200))  # 300
print('-' * 25)


# 案例2: 演示闭包写法
# 需求: 定义求和的闭包, 外部函数有参数num1, 内部函数有参数num2, 调用, 求解两数之和, 观察结果

# 1. 定义外部函数
def fn_outer(num1):
    # 2. 定义内部函数
    def fn_inner(num2):  # 有嵌套
        # 3. 求和
        sum = num1 + num2  # 有引用
        print(f'求和结果: {sum}')

    return fn_inner  # 有返回


# 4. 调用上述函数
fn_inner = fn_outer(10)
fn_inner(1)  # 11
fn_inner(1)  # 11
fn_inner(1)  # 11

print('-' * 25)

fn_outer(100)(200)
