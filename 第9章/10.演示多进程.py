"""
案例: 演示多进程入门案例

多进程目的:
    它属于多任务的一种实现方式, 目的是充分利用CPU资源, 提高程序执行效率

实现方式:
    1. 导包
    2. 创建进程对象, 关联目标函数
    3. 启动进程
"""

# 导包
import multiprocessing
import time


# 1. 定义函数 表示 编写代码
def coding():
    for i in range(1, 11):
        time.sleep(0.1)  # 可以模拟耗时操作, 更好的查看多任务的执行效果.
        print(f'正在敲第 {i} 遍代码!')


# 2. 定义函数 表示 听音乐。
def music():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f'正在听第 {i} 遍音乐......')


# 3. 创建两个进程对象, 分别关联上述的两个 目标函数
# 细节: 通过main进程(主进程)来创建子进程
if __name__ == '__main__':
    # 单任务
    # coding()
    # music()
    # 进程p1关联 coding函数, p1进程抢到(CPU资源了), 就会执行这个函数
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    # 4. 启动进程. 大白话: 表示进程启动了, 就可以开始抢CPU资源了
    p1.start()
    p2.start()
