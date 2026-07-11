# 异常处理
try:
    print("==============================")
    a = int(input("请输入被除数: "))
    b = int(input("请输入除数: "))
    print(f"商为: {a / b}")
    print("==============================")
except ZeroDivisionError as e:  # 捕获的是 ZeroDivisionError 类型的异常
    print("零不能作为除数, 异常信息:", e)
except Exception as e:  # 捕获所有的异常
    print("程序运行出错了, 请联系管理员, 错误信息:", e)
finally:  # 无论是否正常运行, finally 代码块中的代码都会运行
    print("资源释放 ~")


# 异常的传递
def fun1():
    print("fun1 ... running ...")
    fun2()


def fun2():
    print("fun2 ... running ...")
    fun3()


def fun3():
    print("fun3 ... running ...")
    return 1 / 0


if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了, 请联系管理员, 错误信息:", e)
