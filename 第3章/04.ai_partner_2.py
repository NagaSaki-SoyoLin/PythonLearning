import streamlit as st
import os
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",  # 设置页面的布局
    initial_sidebar_state="expanded",  # 控制的是侧边栏的状态
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")

# Logo
st.logo("resources/logo.png")

# 系统提示词
system_prompt = "你是一名非常可爱的AI助理, 你的名字叫小甜甜, 请你使用温柔可爱的语气回答用户的问题"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages:  # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY是环境变量的名字, 值就是DeepSeeK的API_Key的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入您要问的问题:")
if prompt:  # 字符串自动转换为布尔值, 非空字符串为True, 空字符串为False
    st.chat_message("user").write(prompt)
    print(f"-----> 调用AI大模型, 提示词: {prompt}")
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages  # 列表解包, 列表中的元素类型是字典类型
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "disabled"}}
    )

    # 输出大模型返回的结果 (非流式输出的解析方式)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # print(f"<----- 大模型返回的结果: {response.choices[0].message.content}")

    # 输出大模型返回的结果 (流式输出的解析方式)
    response_message = st.empty()  # 创建一个空的容器, 用于显示大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的结果
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    st.session_state.messages.append({"role": "assistant", "content": full_response})
