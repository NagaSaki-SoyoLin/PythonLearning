from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()


# 定义路由(API接口) -> 该函数的返回值表示 API接口 返回的数据
@app.get("/")  # 接口的访问路径为 /, 请求方式为 GET
def root():
    return {"message": "Hello World"}


# 定义API接口
@app.get("/users")  # 接口的访问路径为 /users, 请求方式为 GET
def get_user():
    return [
        {"name": "张三", "age": 20},
        {"name": "李四", "age": 21},
        {"name": "王五", "age": 22}
    ]


# 启动服务器
if __name__ == '__main__':
    import uvicorn  # uvicorn: Python中的轻量级Web服务器

    uvicorn.run(app, host="127.0.0.1", port=8000)  # 127.0.0.1 是本机IP地址, 8000 是端口号
