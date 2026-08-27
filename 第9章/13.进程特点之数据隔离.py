"""
案例: 演示进程的特点

进程的特点:
    1. 进程之间数据是相互隔离的
        因为子进程相当于是父进程的"副本", 会将父进程的"main外资源"拷贝一份, 即: 各是各的
    2. 默认情况下, 主进程会等待子进程执行结束再结束
"""
import multiprocessing
import time

# 需求: 定义1个公共的容器 my_list = [], 一个进程往里边写数据, 另一个进程从里边读数据, 看是否能读取到

# 1. 定义1个公共的容器 my_list = []
my_list = []


# 2. 定义函数, 往容器中添加数据
def write_data():
    for i in range(1, 6):
        my_list.append(i)
        print(f'添加数据: {i}')

    # 走到这里, 说明添加完毕, 打印即可
    print(f'write_data函数: {my_list}')  # [1, 2, 3, 4, 5]


# 3. 定义函数, 从容器中读取数据
def read_data():
    time.sleep(3)
    print(f'read_data函数: {my_list}')  # []


print('我是main外资源, 看我执行了几次')

# 4. 测试
if __name__ == '__main__':
    # 5. 创建两个子进程, 分别关联上述的两个函数
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)

    # 6. 启动进程
    p1.start()
    p2.start()
    # print('我是main内资源, 看我执行了几次')
