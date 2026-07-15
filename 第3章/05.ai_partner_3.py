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
system_prompt = """
    你叫%s,现在是用户的真实伴侣,请完全代入伴侣角色。
    规则:
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短,像微信聊天一样
        5. 有需要的话可以用🩷🌸等emoji表情
        6. 用符合伴侣性格的方式对话
        7. 回复的内容,要充分体现伴侣的性格特征
    伴侣性格:
        - %s
    你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"

# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"

# 展示聊天信息
for message in st.session_state.messages:  # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY是环境变量的名字, 值就是DeepSeeK的API_Key的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 左侧侧边栏 - with: streamlit中的上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")
    # 昵称输入框 - placeholder: 提示文本, value: 默认值
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    # 性格输入框
    nature = st.text_input("性格", placeholder="请输入性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

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
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
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
