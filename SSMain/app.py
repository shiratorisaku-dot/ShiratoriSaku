import os
import importlib
import streamlit as st
from lib.styles import get_css

st.set_page_config(
    page_title="My Modular Space",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(get_css(), unsafe_allow_html=True)
st.markdown("""
    <div class="snow-container">
        <div class="snow small"></div>
        <div class="snow medium"></div>
        <div class="snow large"></div>
    </div>
""", unsafe_allow_html=True)

PARTS_DIR = os.path.join(os.path.dirname(__file__), "parts")

@st.cache_resource(show_spinner=False)
def load_modules():
    modules = {}
    for folder in sorted(os.listdir(PARTS_DIR)):
        if folder.startswith("_"):
            continue
        module_path = f"parts.{folder}"
        try:
            mod = importlib.import_module(module_path)
            info = getattr(mod, "INFO", None)
            render_func = getattr(mod, "render", None)
            if info and render_func:
                modules[info["name"]] = {
                    "icon": info.get("icon", ""),
                    "func": render_func
                }
        except Exception:
            continue
    return modules

def main():
    modules = load_modules()
    options = list(modules.keys())

    with st.sidebar:
        st.markdown("## Navigation")
        selection = st.radio(
            "Go to",
            options,
            format_func=lambda x: f"{modules[x]['icon']}  {x}",
            label_visibility="collapsed",
        )
        st.markdown("---")
        st.caption("日月忽其不淹兮，春與秋其代序。")

    if selection:
        modules[selection]["func"]()

if __name__ == "__main__":
    main()
