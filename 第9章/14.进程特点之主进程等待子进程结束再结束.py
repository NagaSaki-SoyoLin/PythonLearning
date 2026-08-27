"""
案例: 演示进程特点之 默认情况下, 主进程会等待子进程执行结束再结束

进程的特点:
    1. 进程之间数据是相互隔离的
        因为子进程相当于是父进程的"副本", 会将父进程的"main外资源"拷贝一份, 即: 各是各的
    2. 默认情况下, 主进程会等待子进程执行结束再结束
       如果要设置主进程结束, 子进程同步结束, 方式如下:
        思路1: 设置子进程为 守护进程
        思路2: 强制关闭子进程.   可能会导致子进程变成僵尸进程, 交由Python 解释器自动回收(底层有 init初始化进程来管理维护)

"""
import multiprocessing
import time


# 导包


# 1.定义函数, 表示: 子进程的目标函数
def work():
    for i in range(10):
        print('正在努力工作中...')
        time.sleep(0.2)


# 2.测试
if __name__ == '__main__':
    # 3. 创建子进程, 关联目标函数
    # 细节: 进程的默认命名规则是: Process-编号, 编号是从1开始的
    # p1 = multiprocessing.Process(target=work, name='刘亦菲')
    # print(f'p1进程的名字: {p1.name}')

    p1 = multiprocessing.Process(target=work)
    # 思路1: 设置p1为: 守护进程
    p1.daemon = True  # 设置p1为: 守护进程.

    # 4.启动进程
    p1.start()

    # 5.主进程(main)休眠1秒后, 结束
    time.sleep(1)

    # 思路2: 强制关闭子进程
    # p1.terminate()
    print('main进程结束了.')
