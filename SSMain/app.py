# app.py
import os
import importlib
import streamlit as st
from lib.styles import get_css

st.set_page_config(
    page_title="My Modular Space",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 注入全局 CSS（只注入一次）
st.markdown(get_css(), unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def load_modules(parts_dir: str):
    """
    动态扫描 parts 文件夹下子文件夹作为模块（缓存版本）
    - 缓存后切换模块更丝滑
    - 若你新增/删除 parts 子模块：Streamlit 热重载后会自动刷新缓存
    """
    modules = {}

    if not os.path.exists(parts_dir):
        os.makedirs(parts_dir, exist_ok=True)

    subfolders = [
        f.name for f in os.scandir(parts_dir)
        if f.is_dir() and not f.name.startswith("__")
    ]
    subfolders.sort()

    for folder_name in subfolders:
        try:
            module_path = f"parts.{folder_name}"
            module = importlib.import_module(module_path)

            module_info = getattr(module, "INFO", {"name": folder_name, "icon": "📦"})
            render_func = getattr(module, "render", None)

            if callable(render_func):
                modules[module_info["name"]] = {
                    "func": render_func,
                    "icon": module_info.get("icon", "📦"),
                }
            else:
                # 不影响整体，只提示
                st.warning(f"Module '{folder_name}' has no callable render().")
        except Exception as e:
            st.error(f"Error loading module {folder_name}: {e}")

    return modules


def main():
    parts_dir = os.path.join(os.path.dirname(__file__), "parts")
    modules = load_modules(parts_dir)

    with st.sidebar:
        st.title("Navigation")
        st.markdown("---")

        options = list(modules.keys())
        if not options:
            st.warning("No modules found in 'parts/' folder.")
            return

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
