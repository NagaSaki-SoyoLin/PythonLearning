"""
案例: 演示多线程共享全局变量, 可能出现的问题

多线程共享全局变量, 出现问题的问题:
    累加次数不够
产生原因:
    线程1还没有来记得执行完(一个完整的动作)前, 被线程2抢走了资源, 就可能出问题
解决方案:
    加锁思想, 即: 互斥锁

细节:
    使用互斥锁的时候, 要在合适的时机释放所, 否则可能出现 死锁 或者 锁不住的情况


进程和线程的区别:
    1. 线程依赖进程, 进程是CPU分配资源的基本单位, 线程是CPU调度资源的基本单位
    2. 进程更消耗资源, 不能共享全局变量, 相对更稳定
    3. 线程更轻量级, 可以共享全局变量, 相对更灵活
"""

# 需求: 定义两个函数, 分别对全局变量累加100W次, 创建两个线程, 关联这两个函数, 执行看效果
# 导包
import threading

# 1.定义全局变量
global_num = 0

# 创建线程锁
mutex = threading.Lock()


# mutex2 = threading.Lock()

# 2.定义目标函数1, 对全局变量累加100W次
def target_fun1():
    mutex.acquire()  # 加锁
    # 2.1 声明为全局变量
    global global_num
    # 2.2 遍历100W次, 对全局变量进行累加
    for i in range(1000000):
        # 2.3 具体的累加动作
        global_num += 1
    # 2.4 累加完毕后, 打印结果
    print(f'target_fun1函数结果: {global_num}')
    mutex.release()  # 释放锁


# 3.定义目标函数2, 对全局变量累加100W次
def target_fun2():
    mutex.acquire()  # 加锁
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_fun2函数结果: {global_num}')
    mutex.release()  # 释放锁


# 4.测试
if __name__ == '__main__':
    # 4.1 创建两个线程, 分别关联上述的两个目标函数
    t1 = threading.Thread(target=target_fun1)
    t2 = threading.Thread(target=target_fun2)

    # 4.2 开启线程
    t1.start()
    t2.start()
