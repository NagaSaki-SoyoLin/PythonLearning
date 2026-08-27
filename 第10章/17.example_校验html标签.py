r"""
案例: 演示正则表达式之 校验邮箱.

正则规则:
    |           代表 或者的意思
    ()          代表 分组, 从左往右数, 第几个左小括号(, 就表示第几组
    \num        代表 引用第几组的内容.

    扩展:
        (?P<分组名>)   设置分组
        (?P=分组名)    使用分组


参考的html代码:
    <html>
        <head></head>       # 开始, 开放标签,    结束, 闭合标签.
        <body></body>
        <br />              # 自闭合标签.
    </html>
"""
import re

# 需求1: 校验html的单级标签
# 1.定义变量, 记录: html标签
# html_s = '<html>我是html页面</html>'        # 字母数: 1 ~ 4

# 2.匹配校验
# 写法1: 重新copy一份
# result = re.match('<[a-zA-Z]{1,4}>.*</[a-zA-Z]{1,4}>', html_s)

# 写法2: 引入分组的概念
# result = re.match(r'<([a-zA-Z]{1,4})>.*</\1>', html_s)

# 3.打印结果
# if result:
#     print(result.group())
# else:
#     print('未匹配!')


# 需求2: 校验html的单级标签
# 1.定义变量, 记录: html标签
html_s = '<html><h1>我是html页面</h1></html>'  # 字母数: 1 ~ 4,  标题标签1 ~ 6

# 2.匹配校验
# 写法1: 重新copy一份
# result = re.match(r'<[a-zA-Z]{1,4}><h[1-6]>.*</h[1-6]></[a-zA-Z]{1,4}>', html_s)

# 写法2: 引入分组的概念
# result = re.match(r'<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>', html_s)

# 写法3: 给分组起名
result = re.match(r'<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>', html_s)

# 3.打印结果
if result:
    print(result.group())
else:
    print('未匹配!')
