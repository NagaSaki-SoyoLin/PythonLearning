# match...case 模式匹配：工作日程安排
day = input("请输入星期几(1~7): ")

match day:
    case "1":
        print("周一: 工作会议日")
    case "2":
        print("周二: 学习培训日")
    case "3":
        print("周三: 项目开发日")
    case "4":
        print("周四: 代码审查日")
    case "5":
        print("周五: 总结规划日")
    case "6" | "7":  # | 表示或
        print("周末: 休息放松")
    case _:  # 匹配其他所有的情况
        print("输入有误!!!")

# 案例: 基于match...case 实现一个简易的计算器，可以实现+ - * /运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))
oper = input("请输入运算符(+ - * /): ")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:  # if条件成立，才匹配这个case
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")
