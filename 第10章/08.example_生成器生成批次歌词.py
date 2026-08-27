"""
案例: 基于传入的数值(每批次的歌词条数), 创建 生成器, 生成批次歌词
"""
import math


# 需求: 基于文件中 周杰伦的歌词, 创建生成器, 根据传入的每批次的歌词条数, 生成歌词批次
# 1. 定义函数, 接收 每批次的歌词条数, 返回生成器
def dataset_loader(batch_size):  # 假设是 8条/批次
    """
    自定义的 歌词 批量生成器
    :param batch_size:  每批次的歌词条数
    :return: 生成器, 每个元素都是一批次的数据, 例如: (8条, 8条, 8条...)
    """
    # 1.1 读取文件数据
    with open('./data/jaychou_lyrics.txt', 'r', encoding='utf-8') as src_f:
        # 1.2 一次读取所有行
        # lines = [line.strip() for line in src_f.readlines()]
        lines = src_f.readlines()

        # 1.3 计算批次总数, 假设: 5批
        total_batch = math.ceil(len(lines) / batch_size)

        # 1.4 for循环方式, 获取到每批次的数据, 放到生成器中, 并返回
        for idx in range(total_batch):  # idx的值: 0, 1, 2, 3, 4
            # 第1批歌词, 批次索引(idx=0), 歌词为: 第1条 ~ 第8条, 索引为: 0 ~ 7
            # 第2批歌词, 批次索引(idx=1), 歌词为: 第9条 ~ 第16条, 索引为: 8 ~ 15
            # 第3批歌词, 批次索引(idx=2), 歌词为: 第17条 ~ 第24条, 索引为: 16 ~ 23
            yield lines[idx * batch_size: idx * batch_size + batch_size]  # 第1批


# 2. 测试
dl = dataset_loader(8)
print(next(dl))  # 第1批
print(next(dl))  # 第2批

for batch_data in dl:
    print(batch_data)
