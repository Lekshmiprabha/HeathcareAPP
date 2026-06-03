import streamlit as st
import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Blood Report Analyser",
    page_icon="🩸",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Background */
.stApp {
    background: #0f1117;
    color: #e8e8e8;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #161b26 !important;
    border-right: 1px solid #2a2f3e;
}

/* Title */
h1 {
    font-family: 'DM Serif Display', serif !important;
    color: #f5f0e8 !important;
    letter-spacing: -0.5px;
}

h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: #f5f0e8 !important;
}

/* Cards */
.metric-card {
    background: #161b26;
    border: 1px solid #2a2f3e;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 8px 0;
    transition: border-color 0.2s;
}
.metric-card:hover { border-color: #e05c5c; }

.status-high   { color: #e05c5c; font-weight: 600; }
.status-low    { color: #f0a500; font-weight: 600; }
.status-normal { color: #4caf7d; font-weight: 600; }

.risk-high   { background: #3a1a1a; border-left: 4px solid #e05c5c; padding: 12px 16px; border-radius: 8px; }
.risk-medium { background: #2e2510; border-left: 4px solid #f0a500; padding: 12px 16px; border-radius: 8px; }
.risk-low    { background: #0f2a1a; border-left: 4px solid #4caf7d; padding: 12px 16px; border-radius: 8px; }

/* Buttons */
.stButton > button {
    background: #e05c5c !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    padding: 10px 24px !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* Text area */
.stTextArea textarea {
    background: #161b26 !important;
    color: #e8e8e8 !important;
    border: 1px solid #2a2f3e !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', monospace !important;
    font-size: 13px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #161b26;
    border-radius: 8px;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    color: #888 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTabs [aria-selected="true"] {
    background: #e05c5c !important;
    color: white !important;
    border-radius: 6px !important;
}

/* Divider */
hr { border-color: #2a2f3e !important; }

/* File uploader */
.stFileUploader {
    background: #161b26 !important;
    border: 1px dashed #2a2f3e !important;
    border-radius: 8px !important;
}

/* Success/error */
.stSuccess { background: #0f2a1a !important; }
.stError   { background: #3a1a1a !important; }
</style>
""", unsafe_allow_html=True)

# ── Load env & LLM ────────────────────────────────────────────────────────────
load_dotenv(dotenv_path=r"C:\Users\leksh\Documents\AI_projects\.venv\.env")

@st.cache_resource
def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    )

# ── Prompts ───────────────────────────────────────────────────────────────────
EXTRACT_PROMPT = """
You are a medical data extraction analyst.
Extract all blood test parameters from the report below.
Return ONLY a valid JSON object — no extra text, no markdown, no backticks.

Format:
{{
  "patient_name": "",
  "age": 0,
  "gender": "",
  "date": "",
  "reviewing_physician": "",
  "parameters": [
    {{
      "category": "",
      "name": "",
      "value": "",
      "unit": "",
      "normal_range": "",
      "status": "High|Low|Normal",
      "risk_level": "High|Medium|Low"
    }}
  ],
  "overall_risk": "High|Medium|Low",
  "urgent_parameters": [],
  "summary": ""
}}

Blood Report:
{report}
"""

DIET_PROMPT = """
You are an expert Indian dietician and nutritionist.
Based on the blood report analysis below, suggest a detailed Indian diet plan.

Include:
- Foods TO EAT with reasons (use common Indian foods)
- Foods TO AVOID with reasons
- Full day meal plan: Breakfast, Mid-morning, Lunch, Evening snack, Dinner
- Lifestyle tips (exercise, sleep, stress)

Keep it practical, specific, and focused on Indian cuisine.
Return as plain readable text with clear sections.

Analysis:
{analysis}
"""

# ── Helper: parse JSON safely ─────────────────────────────────────────────────
def parse_json(text: str):
    try:
        clean = text.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except Exception:
        return None

# ── Helper: status badge ──────────────────────────────────────────────────────
def status_badge(status: str) -> str:
    s = status.strip().lower()
    if s == "high":
        return '<span class="status-high">▲ High</span>'
    elif s == "low":
        return '<span class="status-low">▼ Low</span>'
    return '<span class="status-normal">✓ Normal</span>'

def risk_class(risk: str) -> str:
    r = risk.strip().lower()
    if r == "high":   return "risk-high"
    if r == "medium": return "risk-medium"
    return "risk-low"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🩸 Blood Report\nAnalyser")
    st.markdown("---")
    st.markdown("**How to use**")
    st.markdown("""
1. Paste or upload your blood report
2. Click **Analyse**
3. View parameter breakdown
4. Get Indian diet recommendations
""")
    st.markdown("---")
    st.markdown("**Model**")
    st.code("llama-3.3-70b-versatile", language=None)
    st.markdown("**Temperature**")
    st.code("0 (deterministic)", language=None)
    st.markdown("---")
    st.caption("Built with LangChain + Groq + Streamlit")

# ── Main UI ───────────────────────────────────────────────────────────────────
st.markdown("# 🩸 Blood Report Analyser")
st.markdown("*AI-powered medical data extraction and Indian diet recommendations*")
st.markdown("---")

# Input section
col1, col2 = st.columns([3, 1])
with col1:
    input_method = st.radio(
        "Input method",
        ["Paste text", "Upload .txt file"],
        horizontal=True,
        label_visibility="collapsed"
    )

blood_report = ""

if input_method == "Paste text":
    blood_report = st.text_area(
        "Paste your blood report here",
        height=250,
        placeholder="Patient: John Doe, Age 45...\nHemoglobin: 15.1 g/dL (Normal: 13.5–17.5)\n...",
    )
else:
    uploaded = st.file_uploader("Upload blood report (.txt)", type=["txt"])
    if uploaded:
        blood_report = uploaded.read().decode("utf-8")
        st.success(f"✅ Loaded: {uploaded.name}")
        with st.expander("Preview file"):
            st.text(blood_report[:500] + ("..." if len(blood_report) > 500 else ""))

st.markdown("")
analyse_btn = st.button("🔬 Analyse Blood Report", use_container_width=False)

# ── Analysis ──────────────────────────────────────────────────────────────────
if analyse_btn:
    if not blood_report.strip():
        st.error("Please paste or upload a blood report first.")
    else:
        llm = get_llm()

        # Step 1 — Extract parameters
        with st.spinner("Extracting parameters from report..."):
            extract_response = llm.invoke([
                SystemMessage(content="You are a medical analyst. Return only valid JSON, no extra text."),
                HumanMessage(content=EXTRACT_PROMPT.format(report=blood_report))
            ])
            data = parse_json(extract_response.content)

        if not data:
            st.error("Could not parse the report. Please check the format and try again.")
            st.code(extract_response.content)
        else:
            st.session_state["data"] = data
            st.session_state["blood_report"] = blood_report

            # Step 2 — Diet recommendation
            with st.spinner("Generating Indian diet recommendations..."):
                diet_response = llm.invoke([
                    SystemMessage(content="You are an expert Indian dietician. Be specific and practical."),
                    HumanMessage(content=DIET_PROMPT.format(analysis=extract_response.content))
                ])
                st.session_state["diet"] = diet_response.content

# ── Display results ───────────────────────────────────────────────────────────
if "data" in st.session_state:
    data = st.session_state["data"]
    diet = st.session_state.get("diet", "")

    st.markdown("---")

    # Patient info strip
    info_cols = st.columns(5)
    fields = [
        ("👤 Patient",   data.get("patient_name", "—")),
        ("🎂 Age",        str(data.get("age", "—"))),
        ("⚧ Gender",     data.get("gender", "—")),
        ("📅 Date",       data.get("date", "—")),
        ("🩺 Physician",  data.get("reviewing_physician", "—")),
    ]
    for col, (label, value) in zip(info_cols, fields):
        with col:
            st.metric(label, value)

    st.markdown("")

    # Overall risk banner
    overall_risk = data.get("overall_risk", "Low")
    rc = risk_class(overall_risk)
    urgent = data.get("urgent_parameters", [])
    urgent_text = ", ".join(urgent) if urgent else "None"
    st.markdown(f"""
    <div class="{rc}">
        <strong>Overall Risk: {overall_risk}</strong> &nbsp;|&nbsp;
        ⚠️ Urgent parameters: {urgent_text}<br>
        <small>{data.get("summary", "")}</small>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Parameter Analysis", "🥗 Diet Recommendations", "📄 Raw JSON"])

    # ── Tab 1: Parameters ────────────────────────────────────────────────────
    with tab1:
        params = data.get("parameters", [])

        if params:
            # Group by category
            categories = {}
            for p in params:
                cat = p.get("category", "Other")
                categories.setdefault(cat, []).append(p)

            for cat, items in categories.items():
                st.markdown(f"### {cat}")
                cols = st.columns(2)
                for i, p in enumerate(items):
                    with cols[i % 2]:
                        badge  = status_badge(p.get("status", "Normal"))
                        risk   = p.get("risk_level", "Low")
                        rclass = risk_class(risk)
                        st.markdown(f"""
                        <div class="metric-card">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <strong>{p.get('name','')}</strong>
                                {badge}
                            </div>
                            <div style="font-size:1.4em; font-weight:600; margin:6px 0;">
                                {p.get('value','')} <small style="font-size:0.55em; color:#888;">{p.get('unit','')}</small>
                            </div>
                            <div style="color:#888; font-size:0.82em;">
                                Normal: {p.get('normal_range','')} &nbsp;|&nbsp; Risk: <strong>{risk}</strong>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.info("No parameters found.")

    # ── Tab 2: Diet ──────────────────────────────────────────────────────────
    with tab2:
        if diet:
            st.markdown(diet)
        else:
            st.info("Diet recommendations not generated yet.")

    # ── Tab 3: Raw JSON ──────────────────────────────────────────────────────
    with tab3:
        st.json(data)
        st.download_button(
            label="⬇️ Download JSON",
            data=json.dumps(data, indent=2),
            file_name="blood_report_analysis.json",
            mime="application/json"
        )