"""
案例: 演示多线程特点之 守护线程

多线程特点:
    1. 线程执行具有随机性, 原因是因为CPU在做着高效的切换
    2. 默认情况下, 主线程会等待子线程结束再结束
    3. (同一个进程的)线程间 数据共享。
    4. 多线程操作共享数据， 可能会出现安全问题， 可以用 互斥锁解决。

"""
# 导包
import threading, time


# 1.定义目标函数
def work():
    for i in range(10):
        time.sleep(0.2)
        print('工作中...')


# 2. 测试
if __name__ == '__main__':
    # 2.1 创建(子)线程对象
    # (守护线程)写法1: daemon属性
    # t = threading.Thread(target=work, daemon=True)

    # (守护线程)写法2: setDaemon()函数, 已过时(暂时还支持, 以后的新版本中可能会被移除掉)
    # t = threading.Thread(target=work)
    # t.setDaemon(True)

    # (守护线程)写法3: daemon属性
    t = threading.Thread(target=work)
    t.daemon = True

    # 2.2 启动线程
    t.start()

    # 2.3 设置主线程休眠时间1秒
    time.sleep(1)
    # 2.4 设置主线程的结束标记
    print('主线程结束了!')
