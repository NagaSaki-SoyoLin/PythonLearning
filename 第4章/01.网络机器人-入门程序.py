import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求
response = requests.get(target_url)

# 输出数据到控制台
print(type(response))
print(response.text)
