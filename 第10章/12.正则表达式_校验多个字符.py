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
    正则常用的规则:9
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

        *       代表前边的内容 出现至少0次, 至多无数次
        ?       代表前边的内容 出现至少0次, 至多1次
        +       代表前边的内容 出现至少1次, 至多无数次
        {n}     代表前边的内容 恰好出现n次, 多一次,少一次都不行
        {n,}    代表前边的内容 至少出现n次, 至多无数次
        {n,m}   代表前边的内容 至少出现n次, 至多出现m次, 包左包右

        |           代表 或者的意思
        ()
        \num

        扩展:
            (?P<分组名>)
            (?P=分组名)
"""

# 导包
import re

# 验证 *       代表前边的内容 出现至少0次, 至多无数次
result = re.match('.*hm.*', 'abchm123')  # 匹配成功
result = re.match('.*hm.*', 'hm123')  # 匹配成功
result = re.match('.*hm.*', 'abchm')  # 匹配成功

result = re.match('.+hm.*', 'abchm')  # 匹配成功
result = re.match('.+hm.*', 'hm123')  # 失败

result = re.match('.?hm.*', 'ahm123')  # 匹配成功
result = re.match('.?hm.*', 'hm123')  # 匹配成功
result = re.match('.?hm.*', 'abchm123')  # 失败

result = re.match(r'\d{3}hm\w{2,5}', '123hm123')  # 匹配成功
result = re.match(r'\d{3}hm\w{2,5}', '123hm12@')  # 匹配成功
result = re.match(r'\d{3}hm\w{2,5}', '123hmabcAB')  # 匹配成功
result = re.match(r'\d{3}hm\w{2,5}', '1234hm123')  # 失败
result = re.match(r'\d{3}hm\w{2,5}', '12hm123')  # 失败
result = re.match(r'\d{3}hm\w{2,5}', '123hm1@')  # 失败
result = re.match(r'\d{3}hm\w{2,5}', '123hmabcAB1')  # 失败

result = re.match(r'\d{3,}hm\w{2,5}', '12hmabcAB1')  # 失败
result = re.match(r'\d{3,}hm\w{2, 5}', '123hmabcAB1')  # 失败, 注意空格
result = re.match(r'\d{3,}hm\w{2,5}', '123hmabc')  # 匹配成功

# 验证 ?       代表前边的内容 出现至少0次, 至多1次
# 验证 +       代表前边的内容 出现至少1次, 至多无数次
# 验证 {n}     代表前边的内容 恰好出现n次, 多一次,少一次都不行
# 验证 {n,}    代表前边的内容 至少出现n次, 至多无数次
# 验证 {n,m}   代表前边的内容 至少出现n次, 至多出现m次, 包左包右

# 查看结果
print(result.group() if result else '未匹配')
