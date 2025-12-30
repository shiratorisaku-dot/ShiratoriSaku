# app.py
import streamlit as st
import importlib
import os
from lib.styles import get_css

# 设置页面基础配置
st.set_page_config(
    page_title="My Modular Space",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 注入自定义CSS（全局）
st.markdown(get_css(), unsafe_allow_html=True)


def load_modules():
    """
    动态扫描 parts 文件夹下的所有子文件夹作为模块
    """
    modules = {}
    parts_dir = os.path.join(os.path.dirname(__file__), "parts")

    # 确保 parts 目录存在
    if not os.path.exists(parts_dir):
        os.makedirs(parts_dir)

    # 遍历文件夹
    subfolders = [f.name for f in os.scandir(parts_dir) if f.is_dir() and not f.name.startswith("__")]
    subfolders.sort()  # 按名称排序，所以可以用 01_, 02_ 控制顺序

    for folder_name in subfolders:
        try:
            # 动态导入模块
            module_path = f"parts.{folder_name}"
            module = importlib.import_module(module_path)

            # 获取模块信息（如果模块定义了 INFO 字典）
            module_info = getattr(module, "INFO", {"name": folder_name, "icon": "📦"})

            modules[module_info["name"]] = {
                "func": module.render,  # 核心渲染函数
                "icon": module_info["icon"]
            }
        except Exception as e:
            st.error(f"Error loading module {folder_name}: {e}")

    return modules


def main():
    # 1. 加载所有模块
    modules = load_modules()

    # 2. 侧边栏构建
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
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.caption("日月忽其不淹兮，春與秋其代序。")

    # 3. 渲染选中模块的主体内容
    if selection:
        modules[selection]["func"]()


if __name__ == "__main__":
    main()
