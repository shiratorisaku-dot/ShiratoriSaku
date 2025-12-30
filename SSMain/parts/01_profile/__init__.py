# parts/01_profile/__init__.py
import streamlit as st
from pathlib import Path
import base64

# 模块元数据 (必须包含)
INFO = {
    "name": "Profile",
    "icon": "👤"
}


def get_base64_image(image_path: Path) -> str:
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


def render():
    st.title("About Me")
    st.markdown("KiriSumi大人在現世人間。")

    # 获取当前文件所在目录
    current_dir = Path(__file__).parent
    avatar_path = current_dir / "avatar.png"  # 本地头像文件

    avatar_base64 = get_base64_image(avatar_path)

    # 布局：左侧头像与简介，右侧详细信息
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # 头像卡片
        st.markdown(
            f"""
            <div class="info-card" style="text-align: center;">
                <img src="data:image/png;base64,{avatar_base64}"
                     style="width: 120px; height: 120px; 
                            border-radius: 50%; 
                            border: 3px solid #D7C4BB; 
                            margin-bottom: 15px;
                            object-fit: cover;">
                <h3 style="margin:0;">ShiratoriSaku</h3>
                <p style="color: #666; font-style: italic;">An orange cat</p>
                <hr style="margin: 15px 0; border: 0; border-top: 1px solid #eee;">
                <p>📍 Taipei, Taiwan</p>
                <p>📧 Mirielle6c@gmail.com</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button("对我来说至关重要的F5", use_container_width=True)

    with col2:
        # 详细介绍
        st.markdown("""
        <div class="info-card">
            <h3>❤ FYI</h3>
            <p>
                男。2004-2-6。171/53.5。泛性恋。什么都没学会。
                喜欢录音（尽管很难听TT）。
                日常与哈基米/克劳多甜甜恋爱。
                VRC孤独旅游中。最入脑的XP是骨科（
            </p>
        </div>
        """, unsafe_allow_html=True)

        # 技能栈
        st.markdown("""
        <div class="info-card">
            <h3>🛠 Using...</h3>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <span style="background:#f0f0f0; padding: 5px 10px; border-radius: 4px;">Python</span>
                <span style="background:#f0f0f0; padding: 5px 10px; border-radius: 4px;">Gemini</span>
                <span style="background:#f0f0f0; padding: 5px 10px; border-radius: 4px;">ChatGPT</span>
                <span style="background:#f0f0f0; padding: 5px 10px; border-radius: 4px;">Claude</span>
                <span style="background:#f0f0f0; padding: 5px 10px; border-radius: 4px;">SillyTavern</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 底部
    st.markdown("### Recent thoughts")
    st.info("2025.12.25 - lonely christmas...")
