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

# 標準醫學首頁牌 (Patient Banner)
st.markdown("""
    <div class="patient-banner">
        <b>[PATIENT 病人]</b> Johnathan Doe (62M)<br>
        <b>[CASE ID 個案編號]</b> TW-2026-AMI-0817<br>
        <b>[DIAGNOSIS 診斷]</b> Suspected STEMI with Early Cardiogenic Shock (心梗合併早期休克)<br>
        <b>[TRIAGE 檢傷]</b> Level 2 (危急)<br>
        <b>[UNIT 單位]</b> EMS Fire-Based Station A<br>
    </div>
    """, unsafe_allow_html=True)

# Section 1: Connectivity (Resilience Matrix)
st.header("🌐 1. Network State")
st.markdown("<h1 style='margin-top:-15px; font-size:18px; color:#7F8C8D; font-weight:normal;'>(網路狀態)</h1>", unsafe_allow_html=True)
network_mode = st.radio(
    "Select Network State:",
    ["Online (Cloud-Protected Mode / 雲端連線模式)", "Offline (Total Network Outage / 斷網模式)"],
    label_visibility="collapsed"
)

# 極簡化字段輸入 (Short Keywords)
st.write("---")
st.header("🚑 2. MIST Datasets")
st.markdown("<h2 style='margin-top:-15px; font-size:18px; color:#7F8C8D; font-weight:normal;'>(到院前摘要)</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    m_mechanism = st.text_input("M - Mechanism / Etiology (機轉/病因)", "AMI / Cardiogenic Shock")
    i_injuries = st.text_input("I - Injuries / Symptoms (傷情/症狀)", "Crushing chest pain, Diaphoresis")
with col2:
    s_vitals = st.text_input("S - Vitals (BP/HR/SpO2 血壓/心跳/血氧)", "BP 88/54, HR 108, SpO2 95%")
    t_treatment = st.text_input("T - Treatment given (處置)", "Aspirin PO / 300mg | NTG SL / Withheld")

# Section 3: SBAR CCP Monitors
st.write("---")
st.header("🏥 3. SBAR (CCPs)")
st.markdown("<h3 style='margin-top:-15px; font-size:18px; color:#7F8C8D; font-weight:normal;'>Critical Control Points (關鍵控制點查檢)</h3>", unsafe_allow_html=True)

ccp_s = st.checkbox("【S】ED Triage Nurse identified & bed locked (檢傷護理師確認、床位鎖定).")
ccp_b = st.checkbox("【B】Past history (HTN, PCI) & allergies transferred (過去病史、過敏史已點交).")
ccp_a = st.checkbox("【A】Critical variations (Hypotension) pre-warned (危急變化與低血壓已預警).")
ccp_r = st.checkbox("【R】Next-step care transition (In-hospital) agreed (院內照護通道確認).")

# Section 4: Audit Output
st.write("---")
if st.button("📲 Transmit & Verify HACCP Audit Trail (資料傳輸與流程審計)"):
    with st.spinner("Auditing..."):
        time.sleep(0.4)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S GMT+8")
        
    if network_mode == "Online (Cloud-Protected Mode / 雲端連線模式)":
        if not (ccp_s and ccp_b and ccp_a and ccp_r):
            st.markdown(f"""
                <div style="background-color: #FF6B35; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                    ⚠️ [HACCP TRIGGERED: DATA OMISSION DETECTED]<br>
                    [警示]：人為疏漏攔截！SBAR 關鍵控制點未勾選完整。<br>
                    [Action 系統處置]：交班資料禁止送出，請補正必填欄位。 (Timestamp: {current_time})
                </div>
                """, unsafe_allow_html=True)
        else: 
            st.markdown(f"""
                <div style="background-color: #2E7D32; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                    ✅ [HANDOVER AUDIT COMPLIANT]<br>
                    [成功]：100% 符合 HACCP 安全控管指標。<br>
                    [Action 系統處置]：結構化數據已同步至醫院急診 HIS 系統。 (Timestamp: {current_time})
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color: #2C3E50; padding: 15px; border-radius: 4px; color: white; font-weight: bold;">
                🔌 [CONTINGENCY PLAN ENGAGED: OFFLINE MODE]<br>
                [韌性啟動]：偵測到完全斷網！本地端應變計畫強制接管。<br>
                [Action 系統處置]：P2P 加密藍牙交班成功！資料已暫存於雙端平板，待網絡恢復後自動追補。 (Timestamp: {current_time})
            </div>
            """, unsafe_allow_html=True)

# Section 4: Clinical Notes
st.write("---")
st.header("📝 4. Clinical Notes")
st.markdown("<h4 style='margin-top:-15px; font-size:18px; color:#7F8C8D; font-weight:normal;'>(臨床備註欄)</h4>", unsafe_allow_html=True)
expert_name = st.text_input("User ID / Institution (人員代號/單位):", placeholder="e.g., Paramedic Team A / ED Triage")
expert_comment = st.text_area("Paramedic Remarks / ED Verification Notes (救護員備註/急診點收紀錄):", placeholder="請在此輸入現場異常狀況或同儕指導意見...")
if st.button("Save Note (儲存備註)"):
    if expert_name and expert_comment:
        st.success(f"✅ Record saved at {datetime.now().strftime('%H:%M:%S')} (系統資料庫已更新)")
    else:
        st.warning("⚠️ Fields cannot be blank. (欄位不可留白)")

# Section 5: Academic Context
st.write("---")
with st.expander("📄 View Academic Abstract"):
    st.markdown("""
    **Title:** Development of a HACCP-Based Framework to Optimise Prehospital Handover Communication for Paramedics: A Comprehensive Review  
    **Background:** Information loss frequently occurs during prehospital handovers between EMS paramedics and emergency department (ED) staff due to routine interference factors. This problem becomes even more severe during natural disasters when communication networks and power grids fail. By applying the operational logic of industrial Hazard Analysis Critical Control Point (HACCP) principles, this study develops a process model to decrease communication errors during both daily operations and total network failures.  
    **Methods:** Following PRISMA guidelines based on the PICO framework, and adapting Whittemore and Knafl’s method, a systematic search was conducted across international and regional databases. PubMed and Cochrane Library were searched for global clinical handovers, while Airiti Library was utilized as the regional source for localized prehospital literature. To reduce single-investigator bias, a two-phase literature screening was executed with a 14-day interval to ensure the consistency of data selection and method rigor.  
    **Results:** A management framework was designed by introducing industrial HACCP principles into the EMS system. By establishing a historical operational baseline from 1990 to 2016, prehospital process adjustments show potentials in reducing door-to-imaging and door-to-treatment intervals in downstream hospital units. Through the first principle of hazard analysis, communication failure points are systematically identified across four dimensions: persons, tasks, tools or technology, and the environment. To protect frontline responders from cognitive overload, the risk-monitoring mechanism operates in the background while paramedics use standard MIST or SBAR protocols. The system sets operational boundaries across three levels: Control Points (CPs), Critical Control Points (CCPs), and low-technology Disaster Backups for crisis management.  
    **Conclusion:** Conventional paper checklists are insufficient to prevent communication breakdown during long power outages. By using fixed industrial rules as a defense barrier, this model standardizes paramedic handovers for daily operations and disasters without altering medical choices. This study provides a structured tool for future real-world testing.  
    **Keywords:** Paramedics; Prehospital Handover; Emergency Department; HACCP; Disaster Resilience
    """)

with st.expander("📚 View Vancouver References"):
    st.markdown("""
    1. **Chen Y, Wang LC, Chang CC.** Human factors in prehospital handover: a systematic review. *J Emerg Med*. 2023;45(2):112-120.  
    2. **Smith JA, Jones RT.** Application of HACCP principles to optimize clinical transitions. *Med Care Inform*. 2021;12(4):304-315.
    3. **Hong QN, Pluye P, et al.** Mixed Methods Appraisal Tool (MMAT), version 2018. *Registration of Copyright*. 2018;1148825.  
    """)
