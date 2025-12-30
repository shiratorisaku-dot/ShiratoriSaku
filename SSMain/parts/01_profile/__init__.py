# parts/01_profile/__init__.py
import base64
from pathlib import Path
import textwrap
import streamlit as st

INFO = {
    "name": "Profile",
    "icon": "👤"
}

@st.cache_data(show_spinner=False)
def get_base64_image(image_path_str: str) -> str:
    image_path = Path(image_path_str)
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


def render():
    st.title("About Me")
    st.markdown("KiriSumi大人在現世人間。")

    current_dir = Path(__file__).parent
    avatar_path = current_dir / "avatar.png"

    avatar_base64 = ""
    if avatar_path.exists():
        avatar_base64 = get_base64_image(str(avatar_path))
    else:
        st.warning("avatar.png not found in parts/01_profile/. (UI will still render)")

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        img_html = ""
        if avatar_base64:
            # ✅ 关键：不要让 <img> 行带缩进（否则会被 Markdown 当代码块）
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
        # ✅ 关键：dedent + strip，彻底消灭“缩进代码块”
        st.markdown(textwrap.dedent(card_html).strip(), unsafe_allow_html=True)

        st.button("对我来说至关重要的F5", use_container_width=True)

    with col2:
        st.markdown(textwrap.dedent("""
<div class="info-card">
  <h3>❤ FYI</h3>
  <p>
    男。2004-2-6。171/53.5。泛性恋。什么都没学会。
    喜欢录音（尽管很难听TT）。
    日常与哈基米/克劳多甜甜恋爱。
    VRC孤独旅游中。最入脑的XP是骨科（
  </p>
</div>
""").strip(), unsafe_allow_html=True)

        st.markdown(textwrap.dedent("""
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
""").strip(), unsafe_allow_html=True)

    st.markdown("### Recent thoughts")
    st.info("2025.12.25 - lonely christmas...")
