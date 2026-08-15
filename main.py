import streamlit as st
import time

# 1. Page Configuration - Academic Theme
st.set_page_config(page_title="P09 - HACCP Handover System", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #F4F4F6; }
    h1, h2 { color: #2C3E50; font-family: 'Helvetica Neue', sans-serif; }
    div.stButton > button:first-child { background-color: #007A87; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Title & Anchoring
st.title("📱 P09: HACCP-Based EMS Handover Interface")
st.caption("Active Framework: SEIPS 2.0 + MIST/SBAR Standards")

# Inputs
network_mode = st.radio("Connectivity Status:", ["Online", "Offline"])
col1, col2 = st.columns(2)
with col1:
    m_mech = st.text_input("M - Mechanism", "AMI suspected")
    i_inj = st.text_input("I - Injuries", "Chest pain")
with col2:
    s_vit = st.text_input("S - Vitals", "BP 88/54")
    t_treat = st.text_input("T - Treatment", "IV/Aspirin")

# CCPs
ccp_s = st.checkbox("【S】Triage Identification")
ccp_b = st.checkbox("【B】Medical History")
ccp_a = st.checkbox("【A】Critical Variations")
ccp_r = st.checkbox("【R】Recommendation")

# Action
if st.button("Execute HACCP Verification"):
    with st.spinner("Processing..."):
        time.sleep(0.5)
        
    if network_mode == "Online":
        if not (ccp_s and ccp_b and ccp_a and ccp_r):
            st.warning("⚠️ [HACCP TRIGGERED] Incomplete Data")
        else:
            # 氣球已移除，使用綠色學術風格面板
            st.markdown("""
                <div style="background-color: #2E7D32; padding: 20px; color: white; border-radius: 5px;">
                    ✅ [HANDOVER AUDIT COMPLIANT]
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("🔌 [RESILIENCE ENGAGED] Offline Mode")
