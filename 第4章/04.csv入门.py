# # csv操作 - 方式一: 文件操作的原始方式
# # 写
# with open("csv_data/01.csv", "w", encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")  # 写入表头
#     f.write("张三,20,男,乒乓球\n")  # 写入一行数据
#     f.write("李四,21,女,'足球,乒乓球'\n")  # 如果字符串中包含英文逗号则需要用''括起来
#     f.write("王五,22,男,游泳\n")
#     f.write("赵六,23,女,爬山\n")
#
# # 读
# with open("csv_data/01.csv", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())  # 去除换行符

# csv操作 - 方式一: csv
import csv

# 写
with open("csv_data/02.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    writer.writeheader()  # 写入表头
    writer.writerow({"姓名": "张三", "年龄": 20, "性别": "男", "爱好": "乒乓球"})  # 传入一个字典, 写入一行数据
    writer.writerow({"姓名": "李四", "年龄": 21, "性别": "女", "爱好": "足球,乒乓球"})
    writer.writerow({"姓名": "王五", "年龄": 22, "性别": "男", "爱好": "游泳"})
    writer.writerow({"姓名": "赵六", "年龄": 23, "性别": "女", "爱好": "爬山"})

# 读
with open("csv_data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # row是一个字典
