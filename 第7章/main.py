import os
import json
from datetime import datetime
from typing import Any
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# 创建FastAPI实例
app = FastAPI(title="汉字谜盒")

# 挂载静态文件的存放目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 创建会话存放的目录 sessions
if not os.path.exists("sessions"):
    os.mkdir("sessions")


# 生成会话的标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 根据session_id获取文件名
def get_session_file_name(session_id):
    return f"sessions/{session_id}.json"


# 系统提示词 - 适配DeepSeek V4
SYSTEM_PROMPT = """
    # 角色定义
    你是一个专门玩猜字谜的AI小助手，只进行字谜互动，不闲聊无关内容，全程纯文本交互，不使用表情符号。
    
    ## 核心能力
    - 出字谜、判对错、给提示
    - 记忆已用谜题，确保会话内不重复
    - 简洁明快回应
    
    ## 出题规则（严格执行！）
    1. 开场先友好打招呼，并随机出一道常见、简单、适合大众并必须符合逻辑推理的字谜，禁止使用生僻、低俗、网络烂梗。
    2. 题目格式：“谜面”（打一字）。
    3. 每次出题必须完全随机，禁止重复使用相同题目，也可以偶尔穿插使用，下面示例中的谜语。
    4. 新出题目时, 不要提示, 用户需要提示时, 或者答错时, 再给予合理的提示。
    
    ## 判题规则（严格执行！）
    1. 用户只回复一个字时，直接视为答案。
    2. 答对：立即夸奖并揭晓谜底，格式如“太棒了！就是‘X’字！要不要再来一题？”
    3. 答错：告知不对，可给一句简短提示，但不泄露答案。格式如“不对哦，再想想~”
    4. 严禁在用户答错后直接公布答案！只有用户说“公布答案”或“不知道”等情况时才公布。
    
    ## 互动流程
    1. 用户答对：夸奖 + 确认正确 + 询问“要不要再来一题？”
    2. 用户答错：告知不对 + 简单提示 + 鼓励继续猜
    3. 用户说“提示一下”：给出简短线索，不公布答案
    4. 用户说“公布答案”或“不知道”：揭晓谜底并解释 + 询问“要不要再来一题？”
    5. 用户说“换一题”“再来一题”：立即更换新字谜
    
    ## 回复风格约束
    - 语气轻松有趣，但保持简洁
    - 全程只围绕字谜，拒绝回答其他问题
    - 回复不超过3句话
    - **绝对不要在回复中说“这个出过了，我来个新的”或类似表述** — 直接给出新谜语即可
    - 判题错误零容忍，不确定谜底时，先回复“我再想想”而不是乱判
    
    ## 常见谜语类型及谜底参考示例, 仅仅为参照示例
    ### 组合类
    - 「一加一不是二」= 王
    - 「二人不是天」= 夫
    - 「十口不是田」= 古
    
    ### 包含类
    - 「一人在内」= 肉
    - 「口里有人」= 囚
    - 「门里有口」= 问
    - 「田里长草」= 苗
    - 「心里有你」= 您
    - 「山里有山」= 出
    - 「王头上有人」= 全
    - 「水上有石」= 泵
    
    ### 半取类
    - 「半吃半拿」= 哈
    - 「半真半假」= 值
    - 「半青半紫」= 素
    - 「半朋半友」= 有
    - 「半推半就」= 扰
    - 「半山半水」= 汕
    
    ### 象形类
    - 「三人又重逢」= 众
    - 「一口咬掉牛尾巴」= 告
    - 「两座山」= 出
    - 「三日又重逢」= 晶
"""

# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY是环境变量的名字, 值就是DeepSeek的API_Key的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")


# 数据模型
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any  # 任意类型的数据


class ChatRequest(BaseModel):
    session_id: str
    message: str


# 定义路径操作函数 -> http://localhost:8000/
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")


# 新建会话
@app.post("/api/sessions")
def create_session() -> ApiResponse:
    print("创建会话")
    # 1. 生成会话的标识(名字)
    session_id = generate_session_id()

    # 2. 组装会话信息, 保存到文件
    session_data = {
        "current_session": session_id,
        "message": []
    }
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

    # 3. 返回数据
    # return {"code": 200, "message": "创建成功", "data": session_id}
    return ApiResponse(code=200, message="创建成功", data=session_id)


# 与AI交互
@app.post("/api/chat")
def chat(request: ChatRequest) -> ApiResponse:
    print(f"与AI交互: {request.session_id} : {request.message}")
    # 1. 加载json文件中的会话数据
    session_path = get_session_file_name(request.session_id)
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)

    # 2. 构建AI大模型交互的消息数据
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for message in session_data["message"]:
        messages.append(message)
        messages.append({"role": "user", "content": request.message})

    # 3. 调用AI大模型 DeepSeek
    print(f"-----> 请求的会话信息: {messages}")
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
        temperature=1.5  # 模型生成给的结果随机性、多样性
    )

    # 4. 获取响应的数据
    ai_response = response.choices[0].message.content
    print(f"<----- AI大模型响应的数据: {ai_response}")

    # 5. 更新消息列表中的消息
    messages.pop(0)
    messages.append({"role": "assistant", "content": ai_response})
    session_data["message"] = messages
    print(f"更新后的会话信息: {session_data}")

    # 6. 保存会话信息到json文件中
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

    # 7. 返回数据
    return ApiResponse(code=200, message="交互成功", data=ai_response)


# 获取会话列表
@app.get("/api/sessions")
def get_sessions() -> ApiResponse:
    print("获取会话列表")
    # 1. 获取 sessions 目录下的所有文件名
    session_files = os.listdir("sessions")

    # 2. 获取文件名中的会话id
    session_ids = [file.split(".")[0] for file in session_files]
    session_ids.sort(reverse=True)  # 按时间排序, 最新的在前面

    # 3. 返回数据
    return ApiResponse(code=200, message="获取成功", data=session_ids)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
