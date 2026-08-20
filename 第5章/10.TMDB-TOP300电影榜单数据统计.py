# -*- coding: utf-8 -*-
"""
项目名称：TMDB-TOP300电影榜单数据统计
文件说明：统计 TOP300 电影榜单的年度数量变化、语言分布、类型分布、评分占比
          （对应 09.TMDB-TOP300电影榜单分析.ipynb 的内容，进行了函数封装）
运行环境：Python 3 + pandas + matplotlib
作者：
日期：
"""

from typing import Dict

import pandas as pd
from pandas import Series
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

# 展示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示异常
plt.rcParams['axes.unicode_minus'] = False

# 数据文件路径
DATA_PATH = './data/movies.csv'
# 统计结果图片保存路径
OUTPUT_PATH = 'data/TMDB-TOP300电影榜单数据统计.png'


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """加载电影榜单数据

    :param path: 数据文件路径
    :return: 包含指定列的电影数据 DataFrame
    """
    # int64: 整型数字(不支持空值)
    # Int64: 整型数字(支持空值)
    # float64: 浮点型数字(支持空值)
    data = pd.read_csv(path, usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
                       dtype={'年份': 'Int64'})
    return data


def plot_yearly_count(axes: Axes, data: pd.DataFrame) -> None:
    """需求一: 统计TOP300的电影中, 每年的电影数量变化(折线图)

    :param axes: 子图坐标轴对象
    :param data: 电影数据 DataFrame
    """
    # 1.1 缺失值、异常值处理
    # 年份缺失时, 取上映时间的前4位作为年份
    data['年份'] = data['年份'].fillna(data['上映时间'].str[:4])

    # 1.2 分组统计
    year_count = data.groupby('年份')['电影名'].count()

    # 1.3 组装数据
    # x轴数据
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = [i for i in range(min_year, max_year + 1)]

    # y轴数据
    y = [int(year_count.get(i, 0)) for i in x]

    # 1.4 绘制折线图
    axes.plot(x, y, color='green')  # 折线图
    axes.set_title('每年电影数量变化折线图', fontsize=18)  # 添加子图标题
    axes.set_xlabel('年份', fontsize=12)  # 添加X轴标签
    axes.set_ylabel('电影数量', fontsize=12)  # 添加Y轴标签

    axes.set_xticks(x[::8])  # 设置X轴刻度间隔
    y_ticks = [i for i in range(0, 31, 3)]
    axes.set_yticks(y_ticks)  # 设置Y轴刻度间隔
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格线


def plot_language_count(axes: Axes, data: pd.DataFrame) -> None:
    """需求二: 统计对比不同语言的电影数量(柱状图)

    :param axes: 子图坐标轴对象
    :param data: 电影数据 DataFrame
    """
    # 2.1 获取不同语言对应的电影数量
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)

    x_language = language_count.index.tolist()
    y_language = language_count.values.tolist()

    # 2.2 绘制柱状图
    axes.bar(x_language, y_language, color='green', width=0.7)  # 柱状图
    axes.set_title('不同语言电影数量柱状图', fontsize=18)  # 添加子图标题
    axes.set_xlabel('语言', fontsize=12)  # 添加X轴标签
    axes.set_ylabel('电影数量', fontsize=12)  # 添加Y轴标签
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格线
    axes.tick_params(axis='x', rotation=30)  # 设置X轴刻度旋转30度


def plot_type_count(axes: Axes, data: pd.DataFrame) -> None:
    """需求三: 统计对比不同类型电影数量(柱状图)

    :param axes: 子图坐标轴对象
    :param data: 电影数据 DataFrame
    """
    # 3.1 获取不同类型对应的电影数量
    type_count: Dict[str, int] = {}  # {类型: 数量}
    for types in data['类型'].str.split(','):  # 类型是列表
        for type in types:  # 类型是字符串
            if type in type_count:
                type_count[type] += 1
            else:
                type_count[type] = 1

    x_types = list(type_count.keys())  # 类型列表
    y_nums = list(type_count.values())  # 数量列表

    # 3.2 绘制柱状图
    axes.bar(x_types, y_nums, color='green', width=0.7)  # 柱状图
    axes.set_title('不同类型电影数量柱状图', fontsize=18)  # 添加子图标题
    axes.set_xlabel('类型', fontsize=12)  # 添加X轴标签
    axes.set_ylabel('电影数量', fontsize=12)  # 添加Y轴标签
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格线
    axes.tick_params(axis='x', rotation=30)  # 设置X轴刻度旋转30度


def plot_score_ratio(axes: Axes, data: pd.DataFrame) -> None:
    """需求四: 统计不同评分电影数量占比(饼状图)

    :param axes: 子图坐标轴对象
    :param data: 电影数据 DataFrame
    """
    # 4.1 获取不同评分对应的电影数量
    scores_count = data.groupby('评分')['评分'].count()

    # 合并小数据(比例 < 2%)为其他
    total = scores_count.sum()
    large_scores: Series = scores_count[scores_count >= total * 0.02]  # 大数据, 比例 >= 2%
    small_scores: Series = scores_count[scores_count < total * 0.02]  # 小数据, 比例 < 2%

    if small_scores.shape[0] > 0:
        large_scores['其他'] = small_scores.sum()

    scores = large_scores.index.tolist()  # 评分列表
    nums = large_scores.values.tolist()  # 数量列表

    # 4.2 绘制饼状图
    axes.pie(nums, labels=scores, autopct='%1.1f%%', startangle=0, radius=1.1)  # 饼状图 -> startangle: 起始角度
    axes.set_title('不同评分电影数量占比饼状图', fontsize=18)  # 添加子图标题
    axes.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.1))  # 添加图例


def main() -> None:
    """主函数: 创建画布子图, 依次绘制四个统计图表, 保存并展示结果"""
    # 创建子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('TMDB-TOP300电影榜单数据统计', fontsize=24, x=0.5, y=0.97)  # 添加画布标题 -> x,y 表示标题相对于画布的位置
    # 调整子图间距 -> hspace: 垂直间距, wspace: 水平间距
    # hspace 调大避免子图标题/旋转的X轴标签互相重叠, top 为画布标题预留空间
    fig.subplots_adjust(hspace=0.5, wspace=0.3, top=0.92)

    # 获取子图
    axes1: Axes = axes[0][0]
    axes2: Axes = axes[0][1]
    axes3: Axes = axes[1][0]
    axes4: Axes = axes[1][1]

    # 加载数据
    data = load_data()

    # 依次绘制四个统计图表
    plot_yearly_count(axes1, data)  # 需求一: 每年电影数量变化(折线图)
    plot_language_count(axes2, data)  # 需求二: 不同语言电影数量(柱状图)
    plot_type_count(axes3, data)  # 需求三: 不同类型电影数量(柱状图)
    plot_score_ratio(axes4, data)  # 需求四: 不同评分电影数量占比(饼状图)

    # 5. 保存图片
    plt.savefig(OUTPUT_PATH)

    # 6. 显示图片
    plt.show()


if __name__ == '__main__':
    main()
