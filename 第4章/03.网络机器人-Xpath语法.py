from lxml import html

# 读取html文件
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_text = f.read()

    # 解析html的文本, 将其转换为一个html文档对象
    document = html.fromstring(html_text)

    # 解析表头 - xpath语法
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)
