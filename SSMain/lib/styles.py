# lib/styles.py

def get_css():
    return """
    <style>
        /* 引入 Google Fonts 衬线字体 + 艺术手写字体 */
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Playfair+Display:wght@500;700&family=Dancing+Script:wght@500;600;700&display=swap');

        /* =========================
           0) 隐藏 Streamlit 顶部白条/工具条/装饰
        ========================= */
        header[data-testid="stHeader"] { display: none !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        div[data-testid="stDecoration"] { display: none !important; }
        #MainMenu { visibility: hidden !important; }
        footer { visibility: hidden !important; }

        /* 顶栏隐藏后，把上边距稍微收紧 */
        .block-container {
            padding-top: 2.2rem !important;
        }

        /* =========================
           1) 全局配色与字体
        ========================= */
        .stApp {
            background-color: #FCFAF2; /* 底色 */
            color: #1C1C1C;           /* 字体色 */
            font-family: 'Cormorant Garamond', serif;
        }

        /* =========================
           2) 侧边栏样式
        ========================= */
        section[data-testid="stSidebar"] {
            background-color: #D7C4BB; /* 侧栏色 */
            box-shadow: 
                4px 0 18px rgba(28, 28, 28, 0.12),
                1px 0 0 rgba(255, 255, 255, 0.25) inset;
        }
        
        /* =========================
            X) 禁用侧边栏伸缩：隐藏折叠按钮
        ========================= */
        /* 新版 Streamlit 常见 */
        button[data-testid="collapsedControl"] { 
            display: none !important; 
        }

        /* 有些版本折叠按钮会用这个结构（兜底） */
        div[data-testid="stSidebarCollapsedControl"],
        div[data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }

        section[data-testid="stSidebar"] * {
            color: #1C1C1C !important;
            font-family: 'Playfair Display', serif;
        }

        /* =========================
           3) 标题样式
        ========================= */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1C1C1C !important;
        }

        /* =========================
           4) 卡片化容器特效 (用于各个模块)
        ========================= */
        .info-card {
            background-color: #FFFFFF;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(28, 28, 28, 0.08); /* 柔和阴影 */
            border: 1px solid rgba(215, 196, 187, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 20px;
        }

        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(28, 28, 28, 0.12);
        }

        /* =========================
           5) 按钮美化
        ========================= */
        .stButton > button {
            background-color: #1C1C1C;
            color: #FCFAF2;
            border-radius: 8px;
            border: none;
            font-family: 'Playfair Display', serif;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #555;
            transform: scale(1.02);
        }

        /* =========================================================
           6) Diary & Guestbook 的 CSS：放全局，避免切换时闪一下裸排版
        ========================================================= */

        /* === 日记时间轴样式 === */
        .timeline-container {
            position: relative;
            padding-left: 30px;
            margin-bottom: 30px;
            border-left: 2px solid #D7C4BB; /* 侧栏同色轴线 */
        }

        .timeline-entry {
            position: relative;
            margin-bottom: 25px;
            padding: 15px 20px;
            background: #FFFFFF;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.03);
            border: 1px solid rgba(215, 196, 187, 0.2);
            transition: transform 0.2s;
        }

        .timeline-entry:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }

        /* 时间轴圆点 */
        .timeline-entry::before {
            content: '';
            position: absolute;
            left: -36px;
            top: 20px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #1C1C1C;
            border: 2px solid #FCFAF2;
        }

        .entry-meta {
            font-family: 'Playfair Display', serif;
            font-size: 0.85em;
            color: #888;
            margin-bottom: 8px;
            letter-spacing: 0.05em;
        }

        .entry-content {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.1em;
            line-height: 1.6;
            white-space: pre-wrap; /* 保留换行 */
        }

        /* === 月份波浪线分隔符 === */
        .month-separator {
            text-align: center;
            margin: 20px 0 40px 0;
            color: #D7C4BB;
            font-family: 'Playfair Display', serif;
            font-size: 1.5em;
            font-style: italic;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }

        .wavy-line {
            height: 10px;
            flex-grow: 1;
            background-image: url("data:image/svg+xml,%3Csvg width='40' height='10' viewBox='0 0 40 10' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 5 Q 10 0 20 5 T 40 5' stroke='%23D7C4BB' fill='none' stroke-width='2'/%3E%3C/svg%3E");
            background-repeat: repeat-x;
            opacity: 0.7;
        }

        /* =========================================================
           ✅ 7) Guestbook 右侧整块方格纸背景
           改动：去掉圆角（border-radius: 0）
        ========================================================= */
        .guestbook-grid-anchor{
            position: relative;
            z-index: 0;
            height: 0; /* 本体不占空间 */
        }

        .guestbook-grid-anchor::before{
            content: "";
            position: absolute;
            top: -12px;
            left: -12px;
            right: -12px;

            /* 覆盖 guestbook 全部内容：不够就调大 */
            height: 2400px;

            background-color: #FFFFFF;
            border: 1px solid #1C1C1C;
            border-radius: 0px; /* ✅ 去掉圆角 */
            box-shadow: 5px 5px 0px rgba(28,28,28,0.1);

            background-image:
                linear-gradient(#D7C4BB 1px, transparent 1px),
                linear-gradient(90deg, #D7C4BB 1px, transparent 1px);
            background-size: 20px 20px;
            background-position: -1px -1px;

            z-index: -1;
            pointer-events: none; /* 不挡点击/输入 */
        }

        /* 让原来的容器变成透明壳，避免双重边框/背景 */
        .guestbook-container{
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
            background-image: none !important;
        }

        /* === 留言板消息展示：去掉实底和边框，字大一点 === */
        .guest-msg {
            background: transparent !important; /* ✅ 去实底 */
            border: none !important;            /* ✅ 去边框 */
            padding: 6px 2px;                   /* 更轻一点 */
            margin-bottom: 12px;
            font-family: 'Cormorant Garamond', serif;
        }

        /* ✅ 时间：艺术字体 */
        .guest-time {
            font-family: 'Dancing Script', cursive;
            font-size: 0.80em;
            color: #666;
            margin-bottom: 4px;
            letter-spacing: 0.02em;
        }

        /* ✅ 留言正文：字体大一点点 */
        .guest-text {
            font-size: 1.50em;        /* 字体更大 */
            line-height: 1.75;
            color: #0C0C0C;           /* 更黑，更稳 */
            font-weight: 500;         /* 比默认稍重，但不粗 */
            white-space: pre-wrap;
        }

        /* 输入框更协调一点 */
        .guest-input textarea {
            background: rgba(255,255,255,0.8) !important;
            border: 1px solid #1C1C1C !important;
        }

        /* === 调整选择框样式 === */
        div[data-testid="stSelectbox"] > div > div {
            background-color: #fff;
            border: 1px solid #D7C4BB;
            color: #1C1C1C;
            font-family: 'Playfair Display', serif;
        }
    </style>
    """
