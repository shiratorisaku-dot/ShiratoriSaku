# parts/02_diary/__init__.py
import streamlit as st
import os
import re
import pandas as pd
from datetime import datetime

# === 模块元数据 ===
INFO = {
    "name": "Cyber Shelter",
    "icon": "📔"
}

# === 配置文件路径 ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIARY_FILE = os.path.join(BASE_DIR, "diary.txt")
GUESTBOOK_FILE = os.path.join(BASE_DIR, "guestbook.csv")


def local_css():
    # Diary 的 CSS 已迁移到全局 lib/styles.py
    return


def parse_diary_file(filepath):
    """解析 diary.txt 文件"""
    if not os.path.exists(filepath):
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'(\S+) (\d{4}-\d{2}-\d{2})\((.)\)(\d{2}:\d{2}:\d{2})')

    entries = []
    matches = list(pattern.finditer(content))

    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)

        header_info = {
            "name": match.group(1),
            "date": match.group(2),
            "day": match.group(3),
            "time": match.group(4),
            "datetime": f"{match.group(2)} {match.group(4)}"
        }

        body = content[start:end].strip()
        entries.append({**header_info, "content": body})

    entries.sort(key=lambda x: x['datetime'], reverse=True)
    return entries


def load_guestbook():
    """读取留言板 CSV"""
    if not os.path.exists(GUESTBOOK_FILE):
        return pd.DataFrame(columns=["Time", "Message"])
    try:
        return pd.read_csv(GUESTBOOK_FILE)
    except Exception:
        return pd.DataFrame(columns=["Time", "Message"])


def save_message(msg):
    """保存留言"""
    if not msg.strip():
        return
    df = load_guestbook()
    new_entry = pd.DataFrame({
        "Time": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "Message": [msg]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(GUESTBOOK_FILE, index=False)


def render():
    local_css()

    st.title("一生一緒です")
    st.markdown("ShiratoriSaku的碎碎念。")
    st.write("")

    col1, col2 = st.columns([2.5, 1], gap="large")

    # --- 左侧：日记时间轴 ---
    with col1:
        entries = parse_diary_file(DIARY_FILE)

        if not entries:
            st.subheader("Diary")
            st.warning(f"No diary entries found. Please create '{DIARY_FILE}'.")
        else:
            all_months = sorted(list(set([e['date'][:7] for e in entries])), reverse=True)

            header_col, filter_col = st.columns([7, 3])

            with header_col:
                st.subheader("Diary")

            with filter_col:
                def format_month(m):
                    return datetime.strptime(m, "%Y-%m").strftime("%B %Y")

                selected_month_str = st.selectbox(
                    "Filter by Month",
                    options=all_months,
                    format_func=format_month,
                    label_visibility="collapsed"
                )

            filtered_entries = [e for e in entries if e['date'].startswith(selected_month_str)]

            current_month = None
            for entry in filtered_entries:
                entry_month = entry['date'][:7]

                if entry_month != current_month:
                    dt_obj = datetime.strptime(entry_month, "%Y-%m")
                    month_display = dt_obj.strftime("%B %Y")

                    st.markdown(f"""
                        <div class="month-separator">
                            <div class="wavy-line"></div>
                            <span>{month_display}</span>
                            <div class="wavy-line"></div>
                        </div>
                    """, unsafe_allow_html=True)
                    current_month = entry_month

                st.markdown(f"""
                <div class="timeline-container">
                    <div class="timeline-entry">
                        <div class="entry-meta">
                            {entry['date']} ({entry['day']}) {entry['time']} • {entry['name']}
                        </div>
                        <div class="entry-content">{entry['content']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # --- 右侧：匿名留言板 ---
    with col2:
        # ✅ 锚点：用于画“超长方格纸背景”
        st.markdown('<div class="guestbook-grid-anchor"></div>', unsafe_allow_html=True)

        st.subheader("Guestbook")

        # 透明壳（样式里已设为透明，不会影响格子纸）
        st.markdown('<div class="guestbook-container">', unsafe_allow_html=True)

        with st.form("guest_form", clear_on_submit=True):
            user_msg = st.text_area(
                "Leave a note...",
                height=100,
                label_visibility="collapsed",
                placeholder="Type here..."
            )
            submitted = st.form_submit_button("Post")
            if submitted:
                save_message(user_msg)
                st.rerun()

        st.markdown(
            '<hr style="border-top: 1px dashed #1C1C1C; margin: 15px 0;">',
            unsafe_allow_html=True
        )

        df_msgs = load_guestbook()
        if not df_msgs.empty:
            for _, row in df_msgs.iloc[::-1].head(8).iterrows():
                st.markdown(f"""
                <div class="guest-msg">
                    <div class="guest-time">{row['Time']}</div>
                    <div class="guest-text">{row['Message']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(
                "<p style='text-align:center; font-style:italic; font-size:0.8em;'>No messages yet.</p>",
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)
