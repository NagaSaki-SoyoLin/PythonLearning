"""
案例: 演示多个装饰器装饰一个函数

记忆:
    多个装饰器装饰一个原函数, 是按照 由内向外 的顺序来装饰的
    但如果要是用 装饰器的写法来做, 看到的效果是, 从上往下 执行的
"""


# 需求: 发表评论前, 需要先登录, 再验证验证码. 请用所学, 模拟该功能
# 1. 定义装饰器, 表示: 登录
def check_login(fn_name):
    # 1.1 定义内函数
    def fn_inner():
        # 1.2 额外功能
        print("校验登录!")
        # 1.3 调用原函数
        fn_name()

    # 1.4 返回内函数
    return fn_inner


# 2. 定义装饰器, 表示: 验证验证码
def check_code(fn_name):
    # 2.1 定义内函数
    def fn_inner():
        # 2.2 额外功能
        print("校验验证码!")
        # 2.3 调用原函数
        fn_name()

    # 2.4 返回内函数
    return fn_inner


@check_login
@check_code
# 3. 定义原函数, 表示: 发表评论
def comment():
    print("发表评论")


# 4. 测试
# 4.1 传统写法
# comment = check_code(comment)
# comment = check_login(comment)
# comment()

# 4.2 语法糖
comment()
