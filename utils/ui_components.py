import streamlit as st
from assets.india_map import get_india_svg

def render_background():
    _india_svg = get_india_svg()  
    _loco_svg = """
<svg width="320" height="95" viewBox="0 0 320 95" xmlns="http://www.w3.org/2000/svg">
  <!-- Overhead catenary wire -->
  <line x1="-60" y1="6" x2="380" y2="6"
        stroke="#2d6a4f" stroke-width="1.4" opacity="0.55" stroke-dasharray="18,6"/>
  <line x1="80"  y1="6" x2="80"  y2="10" stroke="#2d6a4f" stroke-width="1" opacity="0.4"/>
  <line x1="160" y1="6" x2="160" y2="10" stroke="#2d6a4f" stroke-width="1" opacity="0.4"/>
  <line x1="240" y1="6" x2="240" y2="10" stroke="#2d6a4f" stroke-width="1" opacity="0.4"/>
  <line x1="-60" y1="9" x2="380" y2="9"
        stroke="#2d6a4f" stroke-width="2.2" opacity="0.40"/>
  <!-- Pantograph (diamond bow collector) -->
  <rect x="102" y="24" width="6" height="6" rx="1" fill="#2d6a4f"/>
  <rect x="150" y="24" width="6" height="6" rx="1" fill="#2d6a4f"/>
  <line x1="105" y1="24" x2="129" y2="14" stroke="#2d6a4f" stroke-width="2"/>
  <line x1="153" y1="24" x2="129" y2="14" stroke="#2d6a4f" stroke-width="2"/>
  <line x1="120" y1="9"  x2="138" y2="9"  stroke="#2d6a4f" stroke-width="3"/>
  <line x1="120" y1="9"  x2="115" y2="14" stroke="#2d6a4f" stroke-width="1.8"/>
  <line x1="138" y1="9"  x2="143" y2="14" stroke="#2d6a4f" stroke-width="1.8"/>
  <line x1="115" y1="14" x2="143" y2="14" stroke="#2d6a4f" stroke-width="1.5"/>
  <line x1="115" y1="14" x2="105" y2="24" stroke="#2d6a4f" stroke-width="2"/>
  <line x1="143" y1="14" x2="153" y2="24" stroke="#2d6a4f" stroke-width="2"/>
  <!-- Roof -->
  <rect x="18" y="24" width="280" height="6" rx="2" fill="#245a40"/>
  <!-- Main body (WAP-7 style long rectangular loco) -->
  <rect x="18" y="28" width="280" height="44" rx="4" fill="#2d6a4f"/>
  <!-- Left cab -->
  <path d="M 18,28 L 18,72 L 68,72 L 68,28 Z" fill="#1e5040"/>
  <rect x="22" y="32" width="40" height="24" rx="3" fill="#f4efe4" opacity="0.82"/>
  <rect x="22" y="58" width="16" height="12" rx="2" fill="#f4efe4" opacity="0.60"/>
  <circle cx="20" cy="44" r="5" fill="#f4efe4" opacity="0.75"/>
  <circle cx="20" cy="57" r="3" fill="#f4efe4" opacity="0.55"/>
  <rect x="12" y="65" width="10" height="7" rx="1" fill="#1b3a28"/>
  <rect x="8"  y="67" width="14" height="5" rx="1" fill="#2d6a4f"/>
  <!-- Right cab -->
  <path d="M 250,28 L 250,72 L 298,72 L 298,28 Z" fill="#1e5040"/>
  <rect x="254" y="32" width="40" height="24" rx="3" fill="#f4efe4" opacity="0.82"/>
  <rect x="278" y="58" width="16" height="12" rx="2" fill="#f4efe4" opacity="0.60"/>
  <circle cx="297" cy="44" r="5" fill="#f4efe4" opacity="0.75"/>
  <circle cx="297" cy="57" r="3" fill="#f4efe4" opacity="0.55"/>
  <rect x="294" y="65" width="10" height="7" rx="1" fill="#1b3a28"/>
  <rect x="294" y="67" width="14" height="5" rx="1" fill="#2d6a4f"/>
  <!-- Equipment housings + louvres -->
  <rect x="74"  y="30" width="22" height="38" rx="2" fill="#1b4a38"/>
  <rect x="100" y="30" width="14" height="38" rx="2" fill="#1b4a38"/>
  <line x1="76" y1="36" x2="94" y2="36" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="76" y1="42" x2="94" y2="42" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="76" y1="48" x2="94" y2="48" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="76" y1="54" x2="94" y2="54" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="76" y1="60" x2="94" y2="60" stroke="#2d6a4f" stroke-width="1.2"/>
  <rect x="192" y="30" width="14" height="38" rx="2" fill="#1b4a38"/>
  <rect x="210" y="30" width="22" height="38" rx="2" fill="#1b4a38"/>
  <line x1="212" y1="36" x2="230" y2="36" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="212" y1="42" x2="230" y2="42" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="212" y1="48" x2="230" y2="48" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="212" y1="54" x2="230" y2="54" stroke="#2d6a4f" stroke-width="1.2"/>
  <line x1="212" y1="60" x2="230" y2="60" stroke="#2d6a4f" stroke-width="1.2"/>
  <!-- Centre ventilation grilles -->
  <rect x="120" y="32" width="75" height="10" rx="2" fill="#1b4a38"/>
  <rect x="120" y="46" width="75" height="10" rx="2" fill="#1b4a38"/>
  <rect x="120" y="58" width="75" height="10" rx="2" fill="#1b4a38"/>
  <!-- Underframe -->
  <rect x="14" y="70" width="288" height="5" rx="2" fill="#142d1f"/>
  <!-- Left bogie — 3 axles -->
  <rect x="22" y="74" width="80" height="7" rx="3" fill="#1b3a28"/>
  <circle cx="36" cy="83" r="9" fill="none" stroke="#2d6a4f" stroke-width="2.2"/>
  <circle cx="36" cy="83" r="3" fill="#2d6a4f"/>
  <line x1="36" y1="74" x2="36" y2="92" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 36 83" to="360 36 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="27" y1="83" x2="45" y2="83" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 36 83" to="360 36 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <circle cx="62" cy="83" r="9" fill="none" stroke="#2d6a4f" stroke-width="2.2"/>
  <circle cx="62" cy="83" r="3" fill="#2d6a4f"/>
  <line x1="62" y1="74" x2="62" y2="92" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 62 83" to="360 62 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="53" y1="83" x2="71" y2="83" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 62 83" to="360 62 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <circle cx="88" cy="83" r="9" fill="none" stroke="#2d6a4f" stroke-width="2.2"/>
  <circle cx="88" cy="83" r="3" fill="#2d6a4f"/>
  <line x1="88" y1="74" x2="88" y2="92" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 88 83" to="360 88 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="79" y1="83" x2="97" y2="83" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 88 83" to="360 88 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <!-- Right bogie — 3 axles -->
  <rect x="214" y="74" width="80" height="7" rx="3" fill="#1b3a28"/>
  <circle cx="228" cy="83" r="9" fill="none" stroke="#2d6a4f" stroke-width="2.2"/>
  <circle cx="228" cy="83" r="3" fill="#2d6a4f"/>
  <line x1="228" y1="74" x2="228" y2="92" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 228 83" to="360 228 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="219" y1="83" x2="237" y2="83" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 228 83" to="360 228 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <circle cx="254" cy="83" r="9" fill="none" stroke="#2d6a4f" stroke-width="2.2"/>
  <circle cx="254" cy="83" r="3" fill="#2d6a4f"/>
  <line x1="254" y1="74" x2="254" y2="92" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 254 83" to="360 254 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="245" y1="83" x2="263" y2="83" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 254 83" to="360 254 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <circle cx="280" cy="83" r="9" fill="none" stroke="#2d6a4f" stroke-width="2.2"/>
  <circle cx="280" cy="83" r="3" fill="#2d6a4f"/>
  <line x1="280" y1="74" x2="280" y2="92" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 280 83" to="360 280 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <line x1="271" y1="83" x2="289" y2="83" stroke="#2d6a4f" stroke-width="1.6">
    <animateTransform attributeName="transform" type="rotate"
      from="0 280 83" to="360 280 83" dur="2s" repeatCount="indefinite"/>
  </line>
  <!-- Rail -->
  <rect x="-60" y="91" width="440" height="3" rx="1.5" fill="#2d6a4f" opacity="0.45"/>
  <rect x="-60" y="88" width="440" height="1.5" rx="1" fill="#2d6a4f" opacity="0.25"/>
</svg>
"""
    _bg_html = (
        '<div class="bg-scene">'
        '<div class="india-wrap">' + _india_svg + '</div>'
        '<div class="loco-wrap">' + _loco_svg + '</div>'
        '</div>'
    )
    st.markdown(_bg_html, unsafe_allow_html=True)
 

def render_header():
    st.markdown("""
<div class="blw-header">
  <div class="blw-logo-row">
    <svg width="40" height="40" viewBox="0 0 40 40">
      <circle cx="20" cy="20" r="19" fill="#2d6a4f" fill-opacity="0.12"
              stroke="#2d6a4f" stroke-opacity="0.3" stroke-width="1.5"/>
      <text x="20" y="16" text-anchor="middle" fill="#1b4332"
            font-size="9.5" font-weight="700" font-family="Inter, sans-serif">BLW</text>
      <text x="20" y="25" text-anchor="middle" fill="#52796f"
            font-size="5" font-family="Inter, sans-serif">RAILWAYS</text>
      <path d="M8 32 Q20 26 32 32" stroke="#2d6a4f" stroke-width="1"
            fill="none" stroke-opacity="0.4"/>
    </svg>
    <div class="blw-title">BLW Assistant <span>/ Employee Portal</span></div>
  </div>
  <div class="blw-tagline">Banaras Locomotive Works · Salary · PF · HR Support</div>
  <div class="blw-divider"></div>
</div>
""", unsafe_allow_html=True)

def render_chat_history():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🚂" if msg["role"] == "assistant" else "👤"):
            if msg.get("html"):
                st.markdown(msg["content"], unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])

def render_chips():

    pending = None

    if st.session_state.chips:

        cols = st.columns(
            len(st.session_state.chips)
        )

        for i, chip_text in enumerate(
            st.session_state.chips
        ):

            with cols[i]:

                if st.button(
                    chip_text,
                    key=f"chip_{i}_{chip_text}"
                ):
                    pending = chip_text

    return pending