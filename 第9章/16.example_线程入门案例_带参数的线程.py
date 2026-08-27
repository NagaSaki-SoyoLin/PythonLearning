"""
案例: 线程入门案例, 一边听音乐, 一边写代码


线程的使用步骤:
    1. 导包
    2. 创建线程对象
    3. 启动线程


线程和进程的关系:
    1. 进程是CPU分配资源的基本单位, 线程是CPU调度资源的最小单位
    2. 线程是依附于进程的, 每个进程至少有1个线程(主线程栈)
    3. 进程间数据相互隔离, (同一个进程的)线程间数据可以共享
"""

# 导包
import threading, time


# 1. 定义函数, 表示: 敲代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f' {name} 正在敲第 {i} 遍代码...')


# 2. 定义函数, 表示: 听音乐
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f' {name} 正在听第 {i} 首音乐*********')


# 3. 测试
if __name__ == '__main__':
    # 4. 创建两个线程对象, 分别关联上述的两个目标函数
    t1 = threading.Thread(target=coding, args=('李想', 100))
    t2 = threading.Thread(target=music, kwargs={'count': 50, 'name': '周力'})

    # 5. 启动线程
    t1.start()
    t2.start()
