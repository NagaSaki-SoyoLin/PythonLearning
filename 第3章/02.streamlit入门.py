import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    layout="wide",  # 设置页面的布局
    initial_sidebar_state="expanded",  # 控制的是侧边栏的状态
    menu_items={

        # 'Get Help': 'https://www.itcast.cn',
        # 'Report a bug': "https://www.itcast.cn",
        # 'About': "# 这是一个Streamlit的入门页面~"

    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
text = """
布偶猫,被誉为“猫中仙女”,以其优雅的外表和温顺的性格成为最受欢迎的宠物猫之一。

它们体型较大,成年后可达10-20斤,拥有深邃的蓝色眼眸和柔顺的中长毛,毛色多为双色、手套色
或重点色,宛如戴着一副可爱的面具。最迷人的是其松弛柔软的体态,当你抱起它时,它会像布偶一
样全身放松,信赖地偎依在主人怀中,“布偶”之名便由此而来。

性格是布偶猫最大的魅力。它们极度温顺、安静且粘人,被称为“小狗猫”,喜欢跟随主人走动,享受
陪伴。它们通常脾气极好,忍耐力强,能与儿童和其他宠物友好相处,是理想的家庭伴侣。其轻柔的
叫声和爱撒娇的天性,能带给主人无尽的温暖与治愈。

养护方面,需要定期梳理其丰厚毛发以防止打结,并提供足够的关注与互动。拥有一只布偶猫,就如
同拥有了一位温柔优雅、终生依恋的毛茸茸家人。
"""
st.write(text)

# 图片
# st.image("./resources/cat.jpg")
st.image("resources/cat.jpg")

# 音频
st.audio("resources/news.mp3")

# 视频
st.video("resources/news.mp4")

# Logo
st.logo("resources/logo.png")

# 表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)

# 输入框
# 普通输入框
name = st.text_input("请输入您的姓名: ")
st.write(f"您输入的姓名为: {name}")

# 密码输入框
password = st.text_input("请输入您的密码: ", type="password")
st.write(f"您输入的密码为: {password}")

# 单选按钮
gender = st.radio("请选择您的性别: ", ["男", "女", "保密"], index=2)
st.write(f"您选择的性别为: {gender}")
