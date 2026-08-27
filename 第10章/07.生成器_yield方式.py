"""
案例: 演示生成器之 推导式写法

生成器介绍:
    概述:
        所谓的生成器就是基于 数据规则, 用一部分在生成一部分, 而不是一下子生成完所有
    目的:
        可以节省大量的内存
    实现方式:
        1. 推导式写法
        2. yield关键字
"""

# 需求: 通过yield方式, 获取到生成器之 1 ~ 10之间的整数
# 回顾: 推导式写法
my_g = (i for i in range(1, 11))


# yield方式如下
# 1.定义函数, 存储到生成器中, 并返回
def my_fun():
    # my_list = []              # 创建
    # for i in range(1, 11):
    #     my_list.append(i)     # 添加
    # return my_list            # 返回

    # 效果类似于上边的代码
    # yield在这里做了三件事儿: 1.创建生成器对象.  2.把值存储到生成器中.  3.返回生成器
    for i in range(1, 11):
        yield i


# 2.测试
my_g2 = my_fun()
print(type(my_g2))  # <class 'generator'>

print(next(my_g2))
print(next(my_g2))
print('-' * 23)
for i in my_g2:
    print(i)
