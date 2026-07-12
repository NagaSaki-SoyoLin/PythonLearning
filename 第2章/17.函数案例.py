# 案例1:定义一个函数: 根据传入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)
def triangle_area(b, h):
    """
    根据传入的底和高计算三角形面积
    :param b: 底长
    :param h: 高
    :return: 三角形面积
    """
    return round(b * h / 2, 1)


print("底长为30, 高为20的三角形面积: ", triangle_area(30, 20))


# 案例2:定义一个函数: 计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num


print(count_aeiou("Hello Python Hello World OK"))


# 案例3:定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分, 最低分, 平均分(保留1位小数), 并返回
def calc_score(score_list):
    """
    计算成绩列表中成绩的最高分, 最低分, 平均分
    :param score_list: 成绩列表
    :return: 最高分, 最低分, 平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s


s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)
print("最高分: ", max_score)
print("最低分: ", min_score)
print("平均分: ", avg_score)
