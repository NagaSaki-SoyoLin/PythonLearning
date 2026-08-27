# Python 学习路线

从零开始系统学习 Python，覆盖核心语法到实际应用，记录完整的 Python 学习过程。本仓库按学习章节组织代码，每章包含对应的知识点练习与综合案例。

视频参考: bilibili 黑马程序员 [Python入门](https://www.bilibili.com/list/ml3755439255?oid=115610906266258&bvid=BV1sHU9BmEne) [Python进阶](https://www.bilibili.com/list/37974444/?oid=115407063091401&bvid=BV1U2WmzfEqp)

## 学习路线

```
Python 启航 → 核心语法 → AI 应用 → 网络爬虫 → 数据分析
    → 面向对象高级 → Web 应用 → 闭包与装饰器 → 网络编程与多任务 → 生成器与正则
```

## 项目结构

```
py_project01/
├── 第1章/                  # Python 启航
├── 第2章/                  # 核心语法
├── 第3章/                  # AI 应用
├── 第4章/                  # 网络机器人（爬虫）
├── 第5章/                  # 数据分析
├── 第6章/                  # 面向对象高级
├── 第7章/                  # Web 应用
├── 第8章/                  # 闭包和装饰器
├── 第9章/                  # 网络编程和多进程/线程
└── 第10章/                 # 生成器与正则表达式
```

## 章节内容

### 第 1 章 · Python 启航

- 第一个程序：控制台输出，认识注释

### 第 2 章 · 核心语法

- 字面量与变量、数据类型、输入输出、运算符
- `if` 条件判断、`match` 模式匹配、`while` / `for` 循环
- 数据容器：`list`、`str`、`tuple`、`set`、`dict`
- 函数、lambda、递归、类型注解
- 模块与包、面向对象基础、异常处理
- 综合案例：购物车管理系统、教务管理系统

### 第 3 章 · AI 应用

- 调用 DeepSeek 大模型 API（OpenAI SDK）
- 文件操作、`json` 模块、`streamlit` 入门
- 综合案例：**AI 智能伴侣**（多轮对话、流式输出、性格设定、会话保存与恢复）

### 第 4 章 · 网络机器人（爬虫）

- `requests` 请求、`lxml` + XPath 网页解析、`csv` 存储、正则入门
- 综合案例：**TMDB-TOP300 电影榜单爬虫**（模拟浏览器请求、AJAX 分页、正则清洗数据）

### 第 5 章 · 数据分析

- Jupyter Notebook 使用
- **Pandas**：DataFrame 与 Series、数据读取写入、数据清洗、排序分组
- **Matplotlib**：核心图表绘制
- 综合案例：**TMDB 电影榜单分析**（年份、语言、类型、评分四联图）

### 第 6 章 · 面向对象高级

- 封装、继承、方法重写、多继承、多态、鸭子类型、抽象类
- 综合案例：**图书管理系统**（普通/VIP 会员借阅 + JSON 数据持久化）

### 第 7 章 · Web 应用

- **FastAPI** 入门：路由、请求响应、静态文件、日志
- 综合案例：**汉字谜盒**（基于 DeepSeek 的 AI 字谜互动游戏，含前端页面与会话管理）

### 第 8 章 · 闭包和装饰器

- 闭包、`nonlocal` 关键字
- 装饰器：各种参数组合、多装饰器、带参数装饰器
- 面试题：深浅拷贝

### 第 9 章 · 网络编程与多任务

- Socket 网络编程（TCP）：编解码、服务器端/客户端
- 综合案例：一句话通信、**文件上传**
- 多进程：创建、传参、进程编号、数据隔离、守护进程
- 线程入门：创建、传参

### 第 10 章 · 生成器与正则表达式

- 多线程深入：执行随机性、守护线程、数据共享、互斥锁
- 迭代器与生成器：自定义迭代器、推导式、`yield`（歌词分批生成案例）
- `property` 属性两种写法
- 正则表达式：字符匹配、数量限定、分组、替换（邮箱/QQ/HTML 标签校验案例）

## 环境

- Python 3.14
- 虚拟环境：`.venv/`
- 常用依赖：`requests`、`lxml`、`pandas`、`matplotlib`、`streamlit`、`fastapi`、`uvicorn`、`openai`

## 快速开始

```bash
git clone https://github.com/NagaSaki-SoyoLin/py_project01.git
cd py_project01
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 安装依赖（按需）
pip install requests lxml pandas matplotlib streamlit fastapi uvicorn openai jupyter
```

## 运行示例

```bash
# 第 3 章 AI 智能伴侣（Streamlit）
streamlit run 第3章/06.ai_partner_4.py

# 第 7 章 汉字谜盒（FastAPI）
uvicorn 第7章.main:app --reload
```

> 注意：调用 DeepSeek API 需配置环境变量 `DEEPSEEK_API_KEY`。

---

## 许可

- 仅供学习参考，欢迎 Star 和 PR。
