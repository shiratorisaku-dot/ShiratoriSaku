def get_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Playfair+Display:wght@500;700&family=Dancing+Script:wght@500;600;700&display=swap');

        header[data-testid="stHeader"],
        div[data-testid="stToolbar"],
        div[data-testid="stDecoration"],
        footer {
            display: none !important;
            visibility: hidden !important;
        }

        .block-container {
            padding-top: 2.2rem !important;
        }

        .stApp {
            background-color: #FCFAF2;
            color: #1C1C1C;
            font-family: 'Cormorant Garamond', serif;
        }

        h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            display: none !important;
            pointer-events: none;
        }

        h1, h2, h3 {
            pointer-events: none; 
            font-family: 'Playfair Display', serif !important;
            color: #1C1C1C !important;
        }

        section[data-testid="stSidebar"] {
            background-color: #D7C4BB;
            box-shadow: 4px 0 18px rgba(28, 28, 28, 0.12), 1px 0 0 rgba(255, 255, 255, 0.25) inset;
        }

        button[data-testid="collapsedControl"],
        div[data-testid="stSidebarCollapsedControl"],
        div[data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }

        div[data-testid="stRadio"] > div[role="radiogroup"] {
            gap: 1.2rem !important;
            margin-top: 1rem;
        }

        div[data-testid="stRadio"] label > div:first-child {
            display: none !important;
        }

        div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {
            font-family: 'Playfair Display', serif;
            font-size: 1.25rem !important;
            color: rgba(28, 28, 28, 0.6) !important;
            transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.2s ease;
            transform-origin: left center;
            padding-left: 5px;
            margin: 0 !important;
            line-height: 1.5;
        }

        div[data-testid="stRadio"] label:has(input:checked) div[data-testid="stMarkdownContainer"] p {
            transform: scale(1.3) translateX(8px); 
            font-weight: 600 !important;
            color: #1C1C1C !important;
            text-shadow: 2px 2px 0px rgba(255, 255, 255, 0.3);
        }

        div[data-testid="stRadio"] label:hover div[data-testid="stMarkdownContainer"] p {
            color: #1C1C1C !important;
            transform: translateX(4px); 
        }

        div[data-testid="stRadio"] label:has(input:checked):hover div[data-testid="stMarkdownContainer"] p {
             transform: scale(1.3) translateX(8px);
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
        }

        .guest-text {
            font-size: 1.50em;
            line-height: 1.75;
            color: #0C0C0C;
            font-weight: 500;
            white-space: pre-wrap;
        }

        div[data-testid="stSelectbox"] > div > div, 
        .guest-input textarea,
        .stTextArea textarea {
            background-color: #fff !important;
            border: 1px solid #D7C4BB !important;
            color: #1C1C1C !important;
            font-family: 'Playfair Display', serif !important;
        }
    </style>
    """