def get_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Playfair+Display:wght@500;700&family=Dancing+Script:wght@500;600;700&display=swap');

        /* ------------------------------------------------------- */
        /* 1. 头部与侧栏按钮控制 (核心修复部分) */
        /* ------------------------------------------------------- */
        
        /* 不要隐藏整个 Header，否则会连同按钮一起隐藏。
           改为背景透明，并允许点击穿透（这样不会挡住下面的内容） */
        header[data-testid="stHeader"] {
            background: transparent !important;
            pointer-events: none; /* 让鼠标点击穿透 Header 区域 */
        }

        /* 隐藏顶部彩虹装饰线 */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* 隐藏右上角的功能菜单 (Running man, Settings, etc) */
        div[data-testid="stToolbar"], 
        div[data-testid="stStatusWidget"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* 强制显示左上角的侧栏展开按钮，并恢复点击交互 */
        button[data-testid="collapsedControl"],
        div[data-testid="stSidebarCollapsedControl"] {
            display: block !important;
            pointer-events: auto !important; /* 恢复按钮点击 */
            z-index: 1000000 !important; /* 确保层级最高 */
            color: #1C1C1C !important; /* 强制颜色，防止在浅色背景下看不见 */
            background-color: transparent !important;
        }
        
        /* 修复按钮内的图标颜色 */
        button[data-testid="collapsedControl"] svg,
        div[data-testid="stSidebarCollapsedControl"] svg {
            fill: #1C1C1C !important;
            color: #1C1C1C !important;
        }

        /* ------------------------------------------------------- */
        /* 2. 隐藏标题链接锚点 (去除 🔗) */
        /* ------------------------------------------------------- */
        
        /* 隐藏所有标题旁的链接图标 */
        [data-testid="stMarkdownContainer"] h1 a, 
        [data-testid="stMarkdownContainer"] h2 a, 
        [data-testid="stMarkdownContainer"] h3 a,
        h1 > a, h2 > a, h3 > a {
            display: none !important;
            pointer-events: none;
            opacity: 0;
        }

        /* ------------------------------------------------------- */
        /* 3. 页面基础样式 */
        /* ------------------------------------------------------- */

        #MainMenu, footer {
            display: none !important;
        }

        .block-container {
            padding-top: 2.2rem !important;
        }

        .stApp {
            background-color: #FCFAF2;
            color: #1C1C1C;
            font-family: 'Cormorant Garamond', serif;
        }

        /* ------------------------------------------------------- */
        /* 4. 侧栏样式 */
        /* ------------------------------------------------------- */
        
        section[data-testid="stSidebar"] {
            background-color: #D7C4BB;
            box-shadow: 4px 0 18px rgba(28, 28, 28, 0.12), 1px 0 0 rgba(255, 255, 255, 0.25) inset;
        }

        /* 确保侧栏内的文字样式 */
        section[data-testid="stSidebar"] * {
            color: #1C1C1C !important;
            font-family: 'Playfair Display', serif;
        }

        /* 隐藏侧栏内部原本的关闭按钮（可选，防止双重按钮，视版本而定） */
        section[data-testid="stSidebar"] button[kind="header"] {
            /* 通常不需要隐藏，Streamlit 会自动处理 */
        }

        /* ------------------------------------------------------- */
        /* 5. 组件自定义样式 (卡片、时间轴、留言板) */
        /* ------------------------------------------------------- */

        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #1C1C1C !important;
        }

        .info-card {
            background-color: #FFFFFF;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(28, 28, 28, 0.08);
            border: 1px solid rgba(215, 196, 187, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 20px;
        }

        .info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(28, 28, 28, 0.12);
        }

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

        /* Timeline 样式 */
        .timeline-container {
            position: relative;
            padding-left: 30px;
            margin-bottom: 30px;
            border-left: 2px solid #D7C4BB;
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
            white-space: pre-wrap;
        }

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

        /* 留言板样式 */
        .guestbook-grid-anchor {
            position: relative;
            z-index: 0;
            height: 0;
        }

        .guestbook-grid-anchor::before {
            content: "";
            position: absolute;
            top: -12px;
            left: -12px;
            right: -12px;
            height: 2400px;
            background-color: #FFFFFF;
            border: 1px solid #1C1C1C;
            border-radius: 0px;
            box-shadow: 5px 5px 0px rgba(28,28,28,0.1);
            background-image: linear-gradient(#D7C4BB 1px, transparent 1px), linear-gradient(90deg, #D7C4BB 1px, transparent 1px);
            background-size: 20px 20px;
            background-position: -1px -1px;
            z-index: -1;
            pointer-events: none;
        }

        .guestbook-container {
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
            background-image: none !important;
        }

        .guest-msg {
            background: transparent !important;
            border: none !important;
            padding: 6px 2px;
            margin-bottom: 12px;
            font-family: 'Cormorant Garamond', serif;
        }

        .guest-time {
            font-family: 'Dancing Script', cursive;
            font-size: 0.80em;
            color: #666;
            margin-bottom: 4px;
            letter-spacing: 0.02em;
        }

        .guest-text {
            font-size: 1.50em;
            line-height: 1.75;
            color: #0C0C0C;
            font-weight: 500;
            white-space: pre-wrap;
        }

        .guest-input textarea {
            background: rgba(255,255,255,0.8) !important;
            border: 1px solid #1C1C1C !important;
        }

        div[data-testid="stSelectbox"] > div > div {
            background-color: #fff;
            border: 1px solid #D7C4BB;
            color: #1C1C1C;
            font-family: 'Playfair Display', serif;
        }
    </style>
    """
