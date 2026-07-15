import json

# 写入json数据文件
user = {
    "name": "NagaSaki-SoyoLin",
    "age": 20,
    "gender": "男",
    "hobbies": ["reading", "coding"]
}

with open("resources/user.json", "w", encoding="utf-8") as f:
    # .dump() 方法将 Python 对象编码为 JSON 字符串
    # ensure_ascii: 默认为True, 确保所有的数据输出都是ascii编码(非ascii编码的字符会被转义); 设置为False, 非ascii编码的字符会原样输出
    # indent: 缩进, 默认为None, 不缩进; 设置为数字, 缩进的空格数; 设置为4, 缩进4个空格
    json.dump(user, f, ensure_ascii=False, indent=4)

# 读取json数据文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    # .load() 方法将 JSON 字符串解码为 Python 对象
    user = json.load(f)
    print(user)
    print(type(user))
