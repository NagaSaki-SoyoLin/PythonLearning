# __all__ 指定 from ... import * 导入的是哪些功能
__all__ = ["log_separator1", "log_separator3", "PI", "NAME"]

# 常量(不会发生变化的数据; 常量的名称全部大写)
PI = 3.1415926
NAME = "NagaSaki-SoyoLin"


# 函数
def log_separator1():
    print("- " * 30)  # "- "重复输出30次


def log_separator2():
    print("+ " * 30)


def log_separator3():
    print("* " * 30)


def log_separator4():
    print("# " * 30)


# 测试函数
# __name__: Python中的内置变量, 表示当前模块的名字(直接运行该模块则值为"__main__"; 被其他模块导入时则值为模块名, 例如"my_fun")
# 执行当前文件, 则会执行如下代码; 如果被当做模块导入, 代码不执行
if __name__ == '__main__':
    log_separator1()
