def get_css():
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body { height: 100%; }
    .stApp {
        font-family: 'Inter', sans-serif !important;
        background: #f4efe4 !important;
    }
    #MainMenu, footer, .stDeployButton { display: none !important; }
    header[data-testid="stHeader"] {
        background: rgba(244,239,228,0.97) !important;
    }
    /* Main container — above fixed background */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 720px !important;
        position: relative;
        z-index: 10;
        isolation: isolate;
    }
    section[data-testid="stMain"] {
        position: relative;
        z-index: 10;
    }
    /* ── Background scene ── */
    .bg-scene {
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    /* India map — faded, centred */
    .india-wrap {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: min(62vw, 440px);
        opacity= 0.015;
        filter:
        grayscale(100%)
        brightness(180%)
        contrast(60%);
        
        
    }
    /* Electric loco */
    .loco-wrap {
        position: absolute;
        top: 51%;
        transform: translateY(-50%);
        animation: trainRide 55s linear infinite;
        opacity: 0.08;
    }
    @keyframes trainRide {
        0%   { left: -340px; }
        100% { left: 110vw;  }
    }
    /* ── Header ── */
    .blw-header {
        text-align: center;
        padding: 18px 0 10px;
        position: relative;
        z-index: 2;
    }
    .blw-logo-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin-bottom: 4px;
    }
    .blw-title {
        font-size: 23px;
        font-weight: 700;
        color: #1b4332;
        letter-spacing: -0.3px;
    }
    .blw-title span { font-weight: 400; color: #52796f; font-size: 18px; }
    .blw-tagline { font-size: 12px; color: #74a57f; letter-spacing: 0.4px; margin-top: 3px; }
    .blw-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #b7e4c7, transparent);
        margin: 14px auto 18px;
        width: 80%;
    }
    /* ── Chat messages ── */
    [data-testid="stChatMessageContent"] {
    background: rgba(255,255,255,0.97) !important;
    backdrop-filter: blur(4px);
    border: 1px solid #d0e8d4 !important;
    border-radius: 14px !important;
    font-size: 14px !important;
    font-family: 'Inter', sans-serif !important;
    color: #1c3829 !important;
    box-shadow: 0 1px 6px rgba(45,106,79,0.07) !important;
    line-height: 1.65 !important;

    max-width: 100% !important;
    width: auto !important;
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"])
    [data-testid="stChatMessageContent"] {
    background: #2d6a4f !important;
    border: 1px solid #2d6a4f !important;
    }

    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"])
    [data-testid="stChatMessageContent"] * {
    color: white !important;
    }
    
    [data-testid="stChatMessageAvatarAssistant"] { background: #d8f3dc !important; }
    [data-testid="stChatMessageAvatarUser"]      { background: #2d6a4f !important; }
    [data-testid="stChatMessageContent"] p { margin-bottom: 6px !important; }
    [data-testid="stChatMessageContent"] p:last-child { margin-bottom: 0 !important; }
    [data-testid="stChatMessageContent"] code {
        background: #f0fdf4 !important;
        color: #1b4332 !important;
        border-radius: 4px !important;
        padding: 1px 6px !important;
        font-size: 12.5px !important;
    }
    /* ── Chat input ── */
    [data-testid="stChatInput"] {
        border-radius: 28px !important;
        border: 1.5px solid #b7e4c7 !important;
        background: #ffffff !important;
    }
    [data-testid="stChatInput"]:focus-within {
        border-color: #2d6a4f !important;
        box-shadow: 0 0 0 3px rgba(45,106,79,0.12) !important;
    }
    [data-testid="stChatInput"] textarea {
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        color: #1c3829 !important;
        background: transparent !important;
        border: none !important;
        -webkit-text-fill-color: #1c3829 !important;
        min-height: 22px !important;
        max-height: 22px !important;
        caret-color: #1b4332 !important;
    }
    [data-testid="stChatInput"] textarea,
    [data-testid="stChatInput"] input {
        color: #1c3829 !important;
        -webkit-text-fill-color: #1c3829 !important;
    }
    [data-testid="stChatInput"] button {
        background: #2d6a4f !important;
        border-radius: 50% !important;
    }

    
    .dashboard-card {
        background: white;
        border: 1px solid #d0e8d4;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 12px;
        box-shadow: 0 1px 6px rgba(45,106,79,0.07);
    }



/* Placeholder */
[data-testid="stChatInput"] textarea::placeholder {
    color: #6b7280 !important;
}
    /* ── Payslip card ── */
    .payslip {
        border: 1px solid #c8e6d0;
        border-radius: 14px;
        overflow: hidden;
        font-family: 'Inter', sans-serif;
        font-size: 13.5px;
        box-shadow: 0 3px 16px rgba(45,106,79,0.10);
        margin: 6px 0;
    }
    .ps-top {
        background: linear-gradient(135deg, #2d6a4f 0%, #40916c 100%);
        color: #fff;
        padding: 16px 20px;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 12px;
    }
    .ps-name { font-size: 16px; font-weight: 700; }
    .ps-sub  { font-size: 11.5px; opacity: 0.72; margin-top: 4px; }
    .ps-badge {
        background: rgba(255,255,255,0.15);
        border: 1px solid rgba(255,255,255,0.22);
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 11px;
        font-weight: 600;
        white-space: nowrap;
        flex-shrink: 0;
    }
    .ps-body { padding: 16px 20px; background: #fff; }
    .ps-sect-lbl {
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1.1px;
        color: #74a57f;
        text-transform: uppercase;
        padding-bottom: 6px;
        border-bottom: 1px solid #e8f5ec;
        margin-bottom: 4px;
    }
    .pst { width: 100%; border-collapse: collapse; }
    .pst td { padding: 7px 6px; color: #374151; }
    .pst tr:hover td { background: #f7fdf9; border-radius: 6px; }
    .pst .earn { text-align: right; font-weight: 600; color: #1a56a0; }
    .pst .ded  { text-align: right; font-weight: 600; color: #dc2626; }
    .pst .tot-row { border-top: 1px solid #e8f5ec; }
    .pst .tot-row td { padding-top: 9px; font-size: 14px; }
    .net-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, #f0fdf4, #e8f8ee);
        border: 1.5px solid #86efac;
        border-radius: 10px;
        padding: 13px 16px;
        margin-top: 14px;
    }
    .net-lbl { font-size: 13.5px; font-weight: 600; color: #166534; }
    .net-amt { font-size: 20px; font-weight: 800; color: #15803d; letter-spacing: -0.5px; }
    .ps-foot {
        background: #f9fdf9;
        border-top: 1px solid #e0f0e4;
        padding: 10px 20px;
        font-size: 11.5px;
        color: #6b7280;
    }
    /* ── Suggestion chips ── */
    .stButton > button {
        background: #ffffff !important;
        border: 1.5px solid #b7e4c7 !important;
        border-radius: 22px !important;
        color: #2d6a4f !important;
        font-size: 12.5px !important;
        font-weight: 500 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 5px 16px !important;
        transition: all 0.15s !important;
        box-shadow: none !important;
    }
    .stButton > button:hover {
        background: #2d6a4f !important;
        color: #ffffff !important;
        border-color: #2d6a4f !important;
        transform: translateY(-1px);
        box-shadow: 0 3px 10px rgba(45,106,79,0.2) !important;
    }
    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #b7e4c7; border-radius: 10px; }
    /* ── Tables inside chat ── */
    [data-testid="stChatMessageContent"] table {
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
        margin-top: 4px;
    }
    [data-testid="stChatMessageContent"] th,
    [data-testid="stChatMessageContent"] td {
        padding: 7px 10px;
        border-bottom: 1px solid #e8f5ec;
        text-align: left;
    }
    [data-testid="stChatMessageContent"] th {
        background: #f0fdf4;
        font-weight: 600;
        color: #1b4332;
    }
    </style>
    """
