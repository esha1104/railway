import streamlit as st

def initialize_session():

    defaults = {
        "messages": [],
        "phase": "awaiting_id",
        "user_name": None,
        "attempts": 0,
        "last_emp": None,
        "requested_service": None,
        "chips": []
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value