"""
案例: 演示正则表达式之 校验单个字符

正则表达式介绍:
    概述:
        正确的, 符合特定规则的 字符串
        Regular Expression, 正则表达式, 简称: re
    细节:
        1. 学正则表达式, 就是学正则表达式的规则, 你用不背, 网上一搜一大堆
        2. 关于正则我对大家的要求是, 能用我们讲的规则, 看懂别人写的式子, 且会简单修改即可
        3. 正则不独属于Python, 像Java, JavaScript, PHP, Go等都支持
    步骤:
        1. 导包
            import re
        2. 正则匹配
            result = re.match('正则表达式', '要校验的字符串')       从前往后依次匹配,只要能匹配即可
            result = re.search('正则表达式', '要校验的字符串')      分段查找
        3. 获取匹配结果
            result.group()
    正则常用的规则:
        .       代表任意的 1个字符, 除了 \n
        \.      取消.的特殊含义, 就是1个普通的
        a       代表1个普通的字符 a
        [abc]   代表a,b,c中任意的1个字符
        [^abc]  代表除了a,b,c外, 任意的1个字符
        \d      代表数字, 等价于 [0-9]
        \D      代表非数字, 等价于 [^0-9]
        \s      代表空白字符, 等价于 [\t\n\r]
        \S      代表非空白字符
        \w      代表非特殊字符, 即: 数字, 字母, 下划线, 汉字, [a-zA-Z0-9_汉字]
        \W      代表特殊字符, 非字母,数字,下划线,汉字

        ^
        $

        *
        ?
        +
        {n}
        {n,}
        {n,m}

        |           代表 或者的意思
        ()
        \num

        扩展:
            (?P<分组名>)
            (?P=分组名)
"""

# 需求: 正则入门

# 1.导包
import re

# 2.正则校验, 参1: 正则规则, 参2: 要被校验的字符串
# result = re.match('.it', 'ait')     # 匹配成功
# result = re.match('.it', '你it')    # 匹配成功
# result = re.match('.it', '你好it')   # 失败

# result = re.match('\.it', '你it')   # 失败
# result = re.match('\.it', '.it')   # 匹配成功

result = re.match('[ahg]it', 'ait')  # 匹配成功
result = re.match('[ahg]it', 'hit')  # 匹配成功
result = re.match('[ahg]it', 'git')  # 匹配成功
result = re.match('[ahg]it', 'g it')  # 失败

result = re.match('[^ahg]it', 'ait')  # 失败
result = re.match('[^ahg]it', 'x it')  # 失败
result = re.match('[^ahg]it', 'xit')  # 匹配成功
result = re.match('[^ahg]it', 'xitabcxyz')  # 匹配成功, 从前往后匹配, 匹配到就返回.
result = re.match('[^ahg]it', 'abcxitabcxyz')  # 失败, 从前往后依次查找.
# result = re.search('[^ahg]it', 'abcxitabcxyz') # 失败, 从前往后依次查找


result = re.match('[3-7]it', '3it')  # 匹配成功
result = re.match('[3-7]it', '-it')  # 失败, [3-7]等价于[34567]

result = re.match('a\\dhm', 'a1hm')  # 匹配成功
result = re.match('a\\dhm', 'a10hm')  # 失败

result = re.match('a\\Dhm', 'a!hm')  # 匹配成功
result = re.match('a\\Dhm', 'abhm')  # 匹配成功

result = re.match('a\\shm', 'abhm')  # 失败
result = re.match('a\\shm', 'a\thm')  # 匹配成功
result = re.match('a\\shm', 'a\nhm')  # 匹配成功
result = re.match('a\\shm', 'a hm')  # 匹配成功

result = re.match('a\\whm', 'a\thm')  # 失败
result = re.match('a\\whm', 'a!hm')  # 失败
result = re.match('a\\whm', 'axhm')  # 匹配成功
result = re.match('a\\whm', 'a_hm')  # 匹配成功
result = re.match('a\\whm', 'a6hm')  # 匹配成功
result = re.match('a\\whm', 'aYhm')  # 匹配成功
result = re.match('a\\whm', 'a夯hm')  # 匹配成功

# 3.获取匹配结果
if result:
    print(result.group())
else:
    print('匹配失败')
