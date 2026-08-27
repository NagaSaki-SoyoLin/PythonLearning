"""
案例: 演示带参数的多进程

进程传参有两种方式:
    方式1: args方式, 接受所有的 位置参数
    方式2: kwargs方式, 接受所有的 关键字参数
"""
# 导包
import multiprocessing, time


# 需求: 小明一边敲代码, 一边听音乐
# 1. 定义函数, 表示敲代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f'{name} 正在敲第 {i} 行代码...')


# 2. 定义函数, 表示听音乐
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f'{name} 正在听第 {i} 首歌...........')


# 3.创建主进程(主线程)
if __name__ == '__main__':
    # 4. 创建两个子进程, 分别关联上述的目标函数
    p1 = multiprocessing.Process(target=coding, args=('虚竹', 10))
    p2 = multiprocessing.Process(target=music, kwargs={'count': 20, 'name': '刘备'})

    # 5. 开启子进程
    p1.start()
    p2.start()
