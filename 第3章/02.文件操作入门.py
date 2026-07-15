# 读文件
# 1. 打开文件
f = open("resources/望庐山瀑布.txt", "r", encoding="utf-8")

# 2. 读取文件内容
# content = f.read() # 读取全部内容
# print(content)

content_list = f.readlines()  # 读取所有行, 返回列表
for line in content_list:
    print(line.strip())  # strip() 去除换行符

# 3. 关闭文件
f.close()

# 写文件
# 1. 打开文件
f = open("resources/静夜思.txt", "w", encoding="utf-8")

# 2. 写入文件内容
f.write("静夜思(李白)\n\n")
f.write("床前明月光，\n")
f.write("疑是地上霜。\n")
f.write("举头望明月，\n")
f.write("低头思故乡。\n")

# 3. 关闭文件
f.close()

# ------------------------------ 释放资源 方式一 ------------------------------
# 写文件
# 1. 打开文件
f = open("resources/静夜思.txt", "w", encoding="utf-8")

try:
    # 2. 写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")

finally:
    # 3. 关闭文件
    f.close()

# ------------------------------ 释放资源 方式二(最佳实践) ------------------------------
# 写文件
# 1. 打开文件
with open("resources/静夜思.txt", "w", encoding="utf-8") as f:
    # 2. 写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
