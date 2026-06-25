import streamlit as st
from chatbot.chatbot_engine import generate_response
from assets.styles import get_css
from utils.session_manager import initialize_session
from utils.ui_components import (
    render_background,
    render_header,
    render_chat_history,
    render_chips
)   
from services.response_service import (
    get_welcome_message
)
# ── Page config ────────────────────────────────────────────────
st.set_page_config(
    page_title="BLW Employee Assistant",
    page_icon="🚂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    get_css(),
    unsafe_allow_html=True
)
initialize_session()

render_background()
render_header()



# ══════════════════════════════════════════════════════════════
# Initial greeting
# ══════════════════════════════════════════════════════════════
if not st.session_state.messages:

    welcome = get_welcome_message()

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": welcome,
            "html": False
        }
    )

    

render_chat_history()

pending = render_chips()




# ══════════════════════════════════════════════════════════════
# Chat input
# ══════════════════════════════════════════════════════════════
user_input = st.chat_input("Type your message here…")
raw_input = pending or user_input
if raw_input:
    st.session_state.chips = []
    st.session_state.messages.append({"role": "user", "content": raw_input, "html": False})
    response_text, is_html, new_chips = generate_response(raw_input)
    st.session_state.messages.append({"role": "assistant", "content": response_text, "html": is_html})
    st.session_state.chips = new_chips
    st.rerun()
