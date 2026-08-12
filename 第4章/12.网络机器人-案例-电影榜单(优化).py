import re
import requests
import csv
from lxml import html

# 常量
MOVIE_LIST_FILE = "csv_data/movie_list2.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"  # 高分电影榜单的url(第1页)
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"  # 高分电影榜单的url(第2页之后)

# 请求头, 模拟浏览器访问
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# POST 请求专用的 AJAX 头
AJAX_HEADERS = {
    **HEADERS,
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}


# 保存电影数据,保存为 CSV 文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演",
                                            "编剧", "宣传语", "简介"])
        writer.writeheader()  # 写入表头
        writer.writerows(all_movies)  # 写入数据


# 获取电影年份
def get_movie_year(movie_years):
    movie_year = movie_years[0].strip() if movie_years else ''
    return movie_year.replace("(", "").replace(")", "")


# 获取电影上映时间
def get_movie_publish_date(movie_dates):
    movie_date = movie_dates[0].strip() if movie_dates else ''  # 1975-04-10 (US)
    return re.search(r"(\d{4}-\d{2}-\d{2})", movie_date).group()  # 1975-04-10


# 获取电影时长(统一转换为分钟, 如 2h 30m 转换为 150)
def get_movie_cost_time(movie_cost_times):
    movie_cost_time = movie_cost_times[0].strip() if movie_cost_times else ''  # 2h 30m / 40 m / 2h
    h_res = re.search(r"(\d+)h", movie_cost_time)
    m_res = re.search(r"(\d+)m", movie_cost_time)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h * 60 + m

# 获取电影详情
def get_movie_info(movie_info_url):
    # 1. 发送请求, 获取电影详情数据
    print(f"  正在获取电影详情: {movie_info_url}")
    movie_response = requests.get(movie_info_url, headers=HEADERS, timeout=60)

    # 2. 检查响应状态
    if movie_response.status_code != 200:
        print(f"  [错误] 请求失败, 状态码: {movie_response.status_code}, URL: {movie_info_url}")
        return None

    # 3. 解析数据, 获取电影详情
    movie_doc = html.fromstring(movie_response.text)

    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_dates = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    movie_cost_times = movie_doc.xpath(
        "//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_languages = movie_doc.xpath(
        "//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_authors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    movie_descriptions = movie_doc.xpath("//*[@id='original_header' ]/div[2]/section/div[3]/div/p/text()")

    # 4. 返回电影详情 - 字典
    movie_info = {
        "电影名": movie_names[0].strip() if movie_names else '',
        "年份": get_movie_year(movie_years),
        "上映时间": get_movie_publish_date(movie_dates),
        "类型": ",".join(movie_tags) if movie_tags else '',
        "时长": get_movie_cost_time(movie_cost_times),
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_languages[0].strip() if movie_languages else '',
        "导演": ",".join(movie_directors) if movie_directors else '',
        "编剧": ",".join(movie_authors) if movie_authors else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "简介": movie_descriptions[0].strip() if movie_descriptions else ''
    }
    return movie_info


# 主函数, 定义核心逻辑
def main():
    all_movies = []  # 存储所有电影的列表

    # 循环获取电影列表(第1页到第5页)
    for page_num in range(1, 6):
        # 1.发送请求, 获取高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, headers=HEADERS, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     data=f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-07-31&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                     headers=AJAX_HEADERS,
                                     timeout=60)

        print(f"发送请求, 访问第{page_num}页的数据, 获取TMDB电影榜单数据... (状态码: {response.status_code})")

        # 2.检查响应状态
        if response.status_code != 200:
            print(f"[错误] 第{page_num}页请求失败, 状态码: {response.status_code}")
            continue

        # 3.解析数据, 获取电影列表
        # TMDB 新版页面电影卡片使用 data-object-id 属性标识
        document = html.fromstring(response.text)
        movie_list = document.xpath("//div[@data-object-id]")

        print(f"第{page_num}页找到 {len(movie_list)} 部电影")

        # 4.遍历电影列表, 获取电影详情
        for movie in movie_list:
            movie_urls = movie.xpath(".//a[contains(@href, '/movie/')]/@href")
            if movie_urls:
                # 取第一个非空的 /movie/ 链接 (跳过空白链接)
                movie_path = next((url for url in movie_urls if url and '/movie/' in url and url != '/movie/'), '')
                if movie_path:
                    movie_info_url = TMDB_BASE_URL + movie_path
                    # 发送请求, 获取电影详情数据
                    movie_info = get_movie_info(movie_info_url)
                    if movie_info:
                        all_movies.append(movie_info)

    # 5.保存数据, 保存为 CSV 文件
    print(f"获取到所有电影详情共 {len(all_movies)} 部, 保存电影数据到CSV文件...")
    if all_movies:
        save_all_movies(all_movies)
    else:
        print("[警告] 没有获取到任何电影数据, 跳过保存。")


if __name__ == '__main__':
    main()
