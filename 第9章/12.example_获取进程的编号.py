"""
案例: 演示获取进程的编号

进程的编号解释:
    概述:
        在设备中, 每个程序(进程)都有自己的唯一进程id, 当程序释放的时候, 该进程id也会释放. 即: 进程id是可以重复使用的
    目的:
        1. 查看子进程和父进程的关系, 方便 管理
        2. 例如: 杀死指定进程, 创建子进程..
    格式:
        查看当前进程的pid:
            os模块(operating, 系统模块) 的 getpid()        get Process id
            multiprocessing#current_process()的pid属性

        查看当前进程的ppid:        parent process id(父进程id)
            os#getppid()
细节:
    main中创建的进程, 如果没有特殊指定, 它的父进程都是main进程,
    而main进程的父进程是 PyCharm程序的pid
"""

# 导包
import multiprocessing, time
import os


# 需求: 小明一边敲代码, 一边听音乐
# 1. 定义函数, 表示敲代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f'{name} 正在敲第 {i} 行代码...')
    print(f'p1进程的pid: {os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid为) : {os.getppid()}')


# 2. 定义函数, 表示听音乐
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f'{name} 正在听第 {i} 首歌...........')
    print(f'p2进程的pid: {os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid为) : {os.getppid()}')


# 3.创建主进程(主线程)
if __name__ == '__main__':
    # 4. 创建两个子进程, 分别关联上述的目标函数
    p1 = multiprocessing.Process(target=coding, args=('虚竹', 10))
    p2 = multiprocessing.Process(target=music, kwargs={'count': 20, 'name': '刘备'})

    # 5. 开启子进程
    p1.start()
    p2.start()

    # 6. 查看主进程的信息
    print(f'main进程的pid: {os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid为) : {os.getppid()}')
