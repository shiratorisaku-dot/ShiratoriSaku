# parts/02_diary/__init__.py
import os
import re
from datetime import datetime
import pandas as pd
import streamlit as st

INFO = {
    "name": "Cyber Shelter",
    "icon": "📔"
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIARY_FILE = os.path.join(BASE_DIR, "diary.txt")
GUESTBOOK_FILE = os.path.join(BASE_DIR, "guestbook.csv")


# ===== Diary =====
_DIARY_HEADER_RE = re.compile(r'(\S+) (\d{4}-\d{2}-\d{2})\((.)\)(\d{2}:\d{2}:\d{2})')


@st.cache_data(show_spinner=False)
def parse_diary_file(filepath: str):
    """
    解析 diary.txt
    - 缓存：切换页面/筛月份更快
    - datetime 用真正的 datetime 排序更可靠
    """
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    matches = list(_DIARY_HEADER_RE.finditer(content))
    if not matches:
        return []

    entries = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end].strip()

        name = match.group(1)
        date_str = match.group(2)
        day = match.group(3)
        time_str = match.group(4)

        dt = None
        try:
            dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
        except Exception:
            dt = None

        entries.append({
            "name": name,
            "date": date_str,
            "day": day,
            "time": time_str,
            "dt": dt,
            "content": body
        })

    # dt 为空的放后面
    entries.sort(key=lambda x: x["dt"] or datetime.min, reverse=True)
    return entries


# ===== Guestbook =====
@st.cache_data(show_spinner=False)
def load_guestbook(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        return pd.DataFrame(columns=["Time", "Message"])
    try:
        df = pd.read_csv(path)
        # 兜底列缺失
        if "Time" not in df.columns:
            df["Time"] = ""
        if "Message" not in df.columns:
            df["Message"] = ""
        return df[["Time", "Message"]]
    except Exception:
        return pd.DataFrame(columns=["Time", "Message"])


def save_message(path: str, msg: str):
    msg = (msg or "").strip()
    if not msg:
        return

    df = load_guestbook(path)
    new_entry = pd.DataFrame({
        "Time": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "Message": [msg]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(path, index=False)

    # 写入后让缓存失效（否则你可能会看到旧数据）
    load_guestbook.clear()


def render():
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
            # 月份列表（按最新到最旧）
            all_months = sorted({e["date"][:7] for e in entries}, reverse=True)

            header_col, filter_col = st.columns([7, 3])
            with header_col:
                st.subheader("Diary")

            with filter_col:
                def format_month(m: str) -> str:
                    return datetime.strptime(m, "%Y-%m").strftime("%B %Y")

                selected_month_str = st.selectbox(
                    "Filter by Month",
                    options=all_months,
                    format_func=format_month,
                    label_visibility="collapsed",
                )

            filtered_entries = [e for e in entries if e["date"].startswith(selected_month_str)]

            # ✅ DOM 更轻：timeline-container 只包一次（外观不变）
            st.markdown('<div class="timeline-container">', unsafe_allow_html=True)

            current_month = None
            for entry in filtered_entries:
                entry_month = entry["date"][:7]

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

                # ✅ 恢复：每条都包一层 timeline-container（轴线画在这里）
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

            st.markdown("</div>", unsafe_allow_html=True)

    # --- 右侧：匿名留言板 ---
    with col2:
        st.markdown('<div class="guestbook-grid-anchor"></div>', unsafe_allow_html=True)

        st.subheader("Guestbook")
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
                save_message(GUESTBOOK_FILE, user_msg)
                st.rerun()

        st.markdown(
            '<hr style="border-top: 1px dashed #1C1C1C; margin: 15px 0;">',
            unsafe_allow_html=True
        )

        df_msgs = load_guestbook(GUESTBOOK_FILE)
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

        st.markdown("</div>", unsafe_allow_html=True)
