import streamlit as st
import time
from datetime import datetime

# 1. Premium Academic UI Styling (Lancet Minimalist Style)
st.set_page_config(page_title="P09 - HACCP EMS", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #F4F4F6; } /* Warm Light Gray */
    h1, h2, h3 { color: #2C3E50; font-family: sans-serif; font-weight: 700; }
    /* Patient Banner - Standard Medical HIS Spec */
    .patient-banner { background-color: #FFFFFF; padding: 12px; border-radius: 4px; border-left: 4px solid #007A87; margin-bottom: 15px; color: #2C3E50; font-size: 14px; line-height: 1.5; }
    div.stButton > button:first-child { background-color: #007A87; color: white; font-weight: bold; border-radius: 4px; width: 100%; height: 45px; font-size: 16px; }
    div.stButton > button:first-child:hover { background-color: #FF6B35; border-color: #FF6B35; }
    </style>
    """, unsafe_allow_html=True)

# Main Navigation Anchor
st.title("📱 P09: EMS HACCP Handover App")
st.caption("SEIPS 2.0 Engine | SBAR-MIST Protocol | 29 MMAT Core Articles")

# 标准医学首页牌 (Patient Banner)
st.markdown("""
    <div class="patient-banner">
        <b>[PATIENT]</b> Johnathan Doe (62M) | <b>[CASE ID]</b> TW-2026-AMI-0817<br>
        <b>[TRIAGE]</b> Level 1 (Resuscitation) | <b>[UNIT]</b> Fire-Based EMS Station A<br>
        <b>[DIAGNOSIS]</b> Suspected STEMI with Early Cardiogenic Shock
    </div>
    """, unsafe_allow_html=True)

# Section 1: Connectivity (Resilience Matrix)
st.header("🌐 1. Connectivity Status")
network_mode = st.radio(
    "Select Network State:",
    ["Online (Cloud-Protected Mode)", "Offline (Total Network Outage)"],
    label_visibility="collapsed"
)

# 极简化字段输入 (Short Keywords)
st.write("---")
st.header("🚑 2. MIST Datasets")
col1, col2 = st.columns(2)
with col1:
    m_mechanism = st.text_input("M - Mechanism / Etiology", "AMI / Cardiogenic Shock")
    i_injuries = st.text_input("I - Injuries / Symptoms", "Crushing chest pain, Diaphoresis")
with col2:
    s_vitals = st.text_input("S - Vitals (BP/HR/SpO2)", "BP 88/54, HR 108, SpO2 93% on NRM")
    t_treatment = st.text_input("T - Treatment given", "IV 18G, Aspirin 300mg PO, NTG withheld")

# Section 3: SBAR CCP Monitors
st.write("---")
st.header("🏥 3. SBAR Critical Control Points (CCPs)")
ccp_s = st.checkbox("【S】ED Triage Nurse identified & resuscitation bed locked.")
ccp_b = st.checkbox("【B】Past history (HTN, PCI) & allergies transferred.")
ccp_a = st.checkbox("【A】Critical variations (Time-series Hypotension) pre-warned.")
ccp_r = st.checkbox("【R】Next-step care transition (Cath-Lab activation) agreed.")

# Section 4: Audit Output (🌟 依您的建議完美修改為 📲 傳輸圖標)
st.write("---")
if st.button("📲 Transmit & Verify HACCP Audit Trail"):
    with st.spinner("Auditing..."):
        time.sleep(0.4)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
    if network_mode == "Online (Cloud-Protected Mode)":
        if not (ccp_s and ccp_b and ccp_a and ccp_r):
            st.markdown(f"""
                <div style="background-color: #FF6B35; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                    ⚠️ [HACCP TRIGGERED: DATA OMISSION DETECTED]<br>
                    [Timestamp]: {current_time}<br>
                    [Action]: Handover blocked. SBAR CCP fields incomplete.
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background-color: #2E7D32; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                    ✅ [HANDOVER AUDIT COMPLIANT]<br>
                    [Online Submit Time Stamp]: {current_time}<br>
                    [Action]: Datasets synced to Hospital Information System (HIS).
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color: #2C3E50; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                🔌 [CONTINGENCY PLAN ENGAGED: OFFLINE MODE]<br>
                [Offline Received Time Stamp]: {current_time}<br>
                [Action]: P2P encrypted Bluetooth handover complete. Data cached locally.
            </div>
            """, unsafe_allow_html=True)

# Section 5: Academic Context
st.write("---")
with st.expander("📄 View Academic Abstract"):
    st.markdown("**Title:** Development of a HACCP-Based Framework to Optimise Prehospital Handover Communication for Paramedics: A Comprehensive Review...")

with st.expander("📚 View Vancouver References (n=29)"):
    st.markdown("1. Chen Y... 2. Smith JA...")import streamlit as st
import time
from datetime import datetime

# 1. Premium Academic UI Styling (Lancet Minimalist Style)
st.set_page_config(page_title="P09 - HACCP EMS", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #F4F4F6; } /* Warm Light Gray */
    h1, h2, h3 { color: #2C3E50; font-family: sans-serif; font-weight: 700; }
    /* Patient Banner - Standard Medical HIS Spec */
    .patient-banner { background-color: #FFFFFF; padding: 12px; border-radius: 4px; border-left: 4px solid #007A87; margin-bottom: 15px; color: #2C3E50; font-size: 14px; line-height: 1.5; }
    div.stButton > button:first-child { background-color: #007A87; color: white; font-weight: bold; border-radius: 4px; width: 100%; height: 45px; font-size: 16px; }
    div.stButton > button:first-child:hover { background-color: #FF6B35; border-color: #FF6B35; }
    </style>
    """, unsafe_allow_html=True)

# Main Navigation Anchor
st.title("📱 P09: EMS HACCP Handover App")
st.caption("SEIPS 2.0 Engine | SBAR-MIST Protocol | 29 MMAT Core Articles")

# 标准医学首页牌 (Patient Banner)
st.markdown("""
    <div class="patient-banner">
        <b>[PATIENT]</b> Johnathan Doe (62M) | <b>[CASE ID]</b> TW-2026-AMI-0817<br>
        <b>[TRIAGE]</b> Level 1 (Resuscitation) | <b>[UNIT]</b> Fire-Based EMS Station A<br>
        <b>[DIAGNOSIS]</b> Suspected STEMI with Early Cardiogenic Shock
    </div>
    """, unsafe_allow_html=True)

# Section 1: Connectivity (Resilience Matrix)
st.header("🌐 1. Connectivity Status")
network_mode = st.radio(
    "Select Network State:",
    ["Online (Cloud-Protected Mode)", "Offline (Total Network Outage)"],
    label_visibility="collapsed"
)

# 极简化字段输入 (Short Keywords)
st.write("---")
st.header("🚑 2. MIST Datasets")
col1, col2 = st.columns(2)
with col1:
    m_mechanism = st.text_input("M - Mechanism / Etiology", "AMI / Cardiogenic Shock")
    i_injuries = st.text_input("I - Injuries / Symptoms", "Crushing chest pain, Diaphoresis")
with col2:
    s_vitals = st.text_input("S - Vitals (BP/HR/SpO2)", "BP 88/54, HR 108, SpO2 93% on NRM")
    t_treatment = st.text_input("T - Treatment given", "IV 18G, Aspirin 300mg PO, NTG withheld")

# Section 3: SBAR CCP Monitors
st.write("---")
st.header("🏥 3. SBAR Critical Control Points (CCPs)")
ccp_s = st.checkbox("【S】ED Triage Nurse identified & resuscitation bed locked.")
ccp_b = st.checkbox("【B】Past history (HTN, PCI) & allergies transferred.")
ccp_a = st.checkbox("【A】Critical variations (Time-series Hypotension) pre-warned.")
ccp_r = st.checkbox("【R】Next-step care transition (Cath-Lab activation) agreed.")

# Section 4: Audit Output (🌟 依您的建議完美修改為 📲 傳輸圖標)
st.write("---")
if st.button("📲 Transmit & Verify HACCP Audit Trail"):
    with st.spinner("Auditing..."):
        time.sleep(0.4)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
    if network_mode == "Online (Cloud-Protected Mode)":
        if not (ccp_s and ccp_b and ccp_a and ccp_r):
            st.markdown(f"""
                <div style="background-color: #FF6B35; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                    ⚠️ [HACCP TRIGGERED: DATA OMISSION DETECTED]<br>
                    [Timestamp]: {current_time}<br>
                    [Action]: Handover blocked. SBAR CCP fields incomplete.
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background-color: #2E7D32; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                    ✅ [HANDOVER AUDIT COMPLIANT]<br>
                    [Online Submit Time Stamp]: {current_time}<br>
                    [Action]: Datasets synced to Hospital Information System (HIS).
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color: #2C3E50; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                🔌 [CONTINGENCY PLAN ENGAGED: OFFLINE MODE]<br>
                [Offline Received Time Stamp]: {current_time}<br>
                [Action]: P2P encrypted Bluetooth handover complete. Data cached locally.
            </div>
            """, unsafe_allow_html=True)

# Section 5: Academic Context
st.write("---")
with st.expander("📄 View Academic Abstract"):
    st.markdown("**Title:** Development of a HACCP-Based Framework to Optimise Prehospital Handover Communication for Paramedics: A Comprehensive Review...")

with st.expander("📚 View Vancouver References (n=29)"):
    st.markdown("1. Chen Y... 2. Smith JA...")
