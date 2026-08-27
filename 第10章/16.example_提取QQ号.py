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
import re

# 需求: 数据格式为 qq:数字,  从中提qq文本 和 qq号

# 1.定义变量, 记录要校验的字符串
s = 'qq:123456'

# 2.正则校验
result = re.match(r'^(qq):(\d{6,11})$', s)

# 3.提取内容
if result:
    print(result.group())
    print(result.group(0))  # 效果同上
    print('-' * 23)

    print(result.group(1))
    print(result.group(2))
else:
    print('未匹配')
