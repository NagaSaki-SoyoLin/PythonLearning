"""
案例: 演示多线程特点之 数据共享

多线程特点:
    1. 线程执行具有随机性, 原因是因为CPU在做着高效的切换
    2. 默认情况下, 主线程会等待子线程结束再结束
    3. (同一个进程的)线程间 数据共享。
    4. 多线程操作共享数据， 可能会出现安全问题， 可以用 互斥锁解决。

"""

# 需求: 定义全局变量my_list = [], 定义两个目标函数分别实现添加, 查看数据. 最后创建两个线程, 分别执行对应的任务, 观察结果

# 导包
import threading, time

# 1.定义全局变量
my_list = []


# 2. 定义目标函数, 添加数据
def write_data():
    for i in range(1, 6):
        my_list.append(i)
        print("写入数据: ", i)
    print(f'write_data函数: {my_list}')


# 3. 定义目标函数, 查看数据
def read_data():
    # 休眠, 即: 等待write_data()执行结束在结束
    time.sleep(2)
    print(f'read_data函数: {my_list}')


# 4. 测试
if __name__ == '__main__':
    # 4.1 创建线程对象, 并且启动线程
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)

    # 4.2 启动线程
    t1.start()
    t2.start()
