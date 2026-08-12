import re

s1 = "18809090000是我的手机号, 188开头的, 以00结尾的; 我的另一个手机号是15500008888, 两个QQ号分别是1259989092和13809091293821, 邮箱为python666@163.com, 请给我发邮件"

# 正则表达式 -> . 匹配任意字符
print(re.findall(r"188.*", s1))  # * 匹配任何个
print(re.findall(r"188.?", s1))  # ? 匹配0个或1个(最多出现一次)
print(re.findall(r"188.+", s1))  # + 匹配1个或多个(至少出现一次)

print(re.findall(r"188\d{8}", s1))  # {8} 匹配8个
print(re.findall(r"155\d{6,10}", s1))  # {6,10} 匹配6-10个
print(re.findall(r"155\d{6,}", s1))  # {6,} 匹配6个或更多个

print(re.findall(r"1[38]\d{8}", s1))  # [38] 匹配3或者8
print(re.findall(r"1[^38]\d{8}", s1))  # [^38] 匹配除了3和8的任意字符
print(re.findall(r"1[3-9]\d{8}", s1))  # [3-9] 匹配3-9的任意字符(范围)
print(re.findall(r"^1[3-9]\d{9}", s1))  # ^ 匹配字符串s1的开头
print(re.findall(r"^1[3-9]\d{9}$", s1))  # $ 匹配字符串s1的结尾

print(re.findall(r"\w+@\w+\.\w+", s1))  # \w 匹配任意字母、数字、下划线、以及其他语言文字 -> 默认行为
print(re.findall(r"\w+@\w+\.\w+", s1, re.ASCII))  # re.ASCII \w 只能匹配ASCII字符

# 注意
s2 = "现在的时间是2026-02-06 10:05:25,今天的天气还可以,气温是28度"
print(re.findall(r"\d{4}-\d{2}-\d{2}", s2))  # \d 匹配任意数字, \D 匹配任意非数字
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s2))  # () 分组
