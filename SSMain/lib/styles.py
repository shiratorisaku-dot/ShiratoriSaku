def get_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Playfair+Display:wght@500;700&family=Dancing+Script:wght@500;600;700&display=swap');

        /* 隐藏 Streamlit 默认头部装饰，但保留侧栏触发区 */
        header[data-testid="stHeader"] {
            background: transparent;
        }

        /* 隐藏顶部红线装饰 */
        div[data-testid="stDecoration"] {
            display: none !important;
        }

        /* 隐藏右上角汉堡菜单和 Footer */
        div[data-testid="stToolbar"],
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
        }

        /* 【修改点 1】删除了之前隐藏 collapsedControl 的代码块 */
        /* 确保左上角的侧栏展开按钮（汉堡菜单/箭头）可见 */
        button[data-testid="collapsedControl"] {
            display: block !important;
            color: #1C1C1C !important;
        }

        /* 【修改点 2】隐藏标题旁边的锚点链接图标 (🔗) */
        h1 > a, h2 > a, h3 > a, h4 > a, h5 > a, h6 > a {
            display: none !important;
            pointer-events: none; 
        }
        /* 针对 Streamlit 新版结构的额外覆盖 */
        [data-testid="stMarkdownContainer"] h1 a, 
        [data-testid="stMarkdownContainer"] h2 a,
        [data-testid="stMarkdownContainer"] h3 a {
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

        section[data-testid="stSidebar"] {
            background-color: #D7C4BB;
            box-shadow: 4px 0 18px rgba(28, 28, 28, 0.12), 1px 0 0 rgba(255, 255, 255, 0.25) inset;
        }

        section[data-testid="stSidebar"] * {
            color: #1C1C1C !important;
            font-family: 'Playfair Display', serif;
        }

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