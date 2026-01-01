import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

INFO = {
    "name": "Profile",
    "icon": "👤"
}


@st.cache_data(show_spinner=False)
def get_base64_image(image_path_str: str) -> str:
    image_path = Path(image_path_str)
    if not image_path.exists():
        return ""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def render():
    if "f5_count" not in st.session_state:
        st.session_state.f5_count = 0

    st.title("About Me")
    st.markdown("KiriSumi大人在現世人間。")

    current_dir = Path(__file__).parent
    avatar_path = current_dir / "avatar.png"
    avatar_base64 = get_base64_image(str(avatar_path))

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        img_html = ""
        if avatar_base64:
            img_html = (
                f'<img src="data:image/png;base64,{avatar_base64}" '
                'style="width: 120px; height: 120px; border-radius: 50%; '
                'border: 3px solid #D7C4BB; margin-bottom: 15px; object-fit: cover;">'
            )

        card_html = f"""
        <div class="info-card" style="text-align: center;">
            {img_html}
            <h3 style="margin:0;">ShiratoriSaku</h3>
            <p style="color: #666; font-style: italic;">An orange cat</p>
            <hr style="margin: 15px 0; border: 0; border-top: 1px solid #eee;">
            <p>📍 Taipei, Taiwan</p>
            <p>📧 Mirielle6c@gmail.com</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

        if st.button("对我来说至关重要的F5", use_container_width=True):
            st.session_state.f5_count += 1

        if st.session_state.f5_count >= 5:
            st.session_state.f5_count = 0
            # Saku酱的彩蛋
            target_url = "https://docs.google.com/forms/d/e/1FAIpQLSdpReGX5HsSYJ_wuUjp_CtzdOhuML9U8wTjI6JtvWO22KSl0w/viewform?usp=sharing&ouid=110003774276712139106"
            js = f"<script>window.open('{target_url}', '_blank').focus();</script>"
            components.html(js, height=0)

    with col2:
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

    st.markdown("### Recent thoughts")
    st.info("2025.12.25 - lonely christmas...")