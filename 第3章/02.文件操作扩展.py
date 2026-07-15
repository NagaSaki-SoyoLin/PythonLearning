# 读文件
"""
路径写法:
    相对路径: 从当前文件所在目录开始查找(推荐)
        .: 当前目录 ----> ./resources/望庐山瀑布.txt ./ 可以省略
        ..: 上一级目录 ---> .. /第2章/file/寻隐者不遇.txt

    绝对路径: 从文件系统根目录开始查找,文件位置的完整路径(注意: 反斜杠 在字符串中表示的是转义字符,\n \t)
        方式一: D:\\Python-Project\\py_project01\\第3章\\resources\\望庐山瀑布.txt
        方式二: D:/Python-Project/py_project01/第3章/resources/望庐山瀑布.txt
"""
with open("resources/望庐山瀑布.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 写文件
# a: append, 追加内容; w: write, 覆盖内容 -> 如果文件不存在, 则创建文件
with open("resources/静夜思.txt", "a", encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
