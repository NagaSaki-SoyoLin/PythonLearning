r"""
案例: 演示正则表达式之 校验邮箱.

正则规则:
    |           代表 或者的意思
    ()          代表 分组, 从左往右数, 第几个左小括号(, 就表示第几组
    \num        代表 引用第几组的内容.

    扩展:
        (?P<分组名>)   设置分组
        (?P=分组名)    使用分组
"""
# 导包
import re

# 1. 定义邮箱
email = "abcd@163.com"

# 2. 校验邮箱是否合法
result = re.match(r'^[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$', email)

# 3. 打印结果
if result:
    print(f'合法邮箱为: {result.group()}')
    print(f'合法邮箱为: {result.group(0)}')  # 获取第0组的信息, 效果同上, 即: 整个匹配到的结果
    print(f'合法邮箱为: {result.group(1)}')  # 获取第1组的信息,  即: 163
else:
    print("邮箱不合法!")
