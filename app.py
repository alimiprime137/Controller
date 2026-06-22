import streamlit as st
import datetime
import time

# 1. Page Configuration for SaaS Dashboard Layout
st.set_page_config(
    page_title="Akamal's Mission Control",
    page_icon="⚡",
    layout="wide", # Expands layout to screen edges like Vercel templates
    initial_sidebar_state="collapsed"
)

# 2. Dynamic 24-Hour Nature Background Logic
nature_wallpapers = [
    "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=1920", # Deep Forest
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1920", # Woodland
    "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?q=80&w=1920", # Footbridge
    "https://images.unsplash.com/photo-1472214222541-d510753a4707?q=80&w=1920", # Emerald Valley
    "https://images.unsplash.com/photo-1501854140801-50d01698950b?q=80&w=1920", # Mountain Peaks
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=1920", # Alpine Highland
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=1920"  # Misty Valley
]
day_index = datetime.date.today().weekday()
current_bg = nature_wallpapers[day_index]

# 3. High-End SaaS UI Custom CSS (Vercel Breeze Aesthetic)
st.markdown(f"""
    <style>
    /* Premium Dark Mode Glass Cover */
    .stApp {{
        background-image: linear-gradient(to bottom, rgba(10, 15, 30, 0.75), rgba(10, 11, 20, 0.92)), url('{current_bg}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Vercel Typography & Global Font Override */
    h1, h2, h3, p, label, span, .stMarkdown p {{
        color: #F3F4F6 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
    }}
    
    /* Grid Title Tweaks */
    .section-title {{
        font-size: 1.15rem;
        font-weight: 600;
        color: #9CA3AF !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 12px;
        border-left: 3px solid #3B82F6;
        padding-left: 8px;
    }}
    
    /* High-Performance Vercel Breeze Checkbox Cards */
    div[data-testid="stCheckbox"] {{
        background: rgba(17, 24, 39, 0.65) !important;
        padding: 14px 18px !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.07) !important;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
        margin-bottom: 12px !important;
        backdrop-filter: blur(12px);
    }}
    
    /* Neon Glow Hover Micro-Animation */
    div[data-testid="stCheckbox"]:hover {{
        background: rgba(31, 41, 55, 0.8) !important;
        border-color: #3B82F6 !important; /* Premium Cyan/Blue Border on hover */
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.25);
        transform: translateY(-2px);
    }}
    
    /* Clean Styling for Countdown Screen */
    .countdown-text {{
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        margin-top: 18%;
        letter-spacing: -0.03em;
        background: linear-gradient(to right, #FFFFFF, #9CA3AF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. One-Time Flash Initialization Sequence
if 'countdown_complete' not in st.session_state:
    st.session_state.countdown_complete = False

if not st.session_state.countdown_complete:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<p class="countdown-text">Hello Akamal Alimi</p>', unsafe_allow_html=True)
        time.sleep(1.3)
        st.markdown('<p class="countdown-text">Mission starting in 3...</p>', unsafe_allow_html=True)
        time.sleep(0.9)
        st.markdown('<p class="countdown-text">Mission starting in 2...</p>', unsafe_allow_html=True)
        time.sleep(0.9)
        st.markdown('<p class="countdown-text">Mission starting in 1...</p>', unsafe_allow_html=True)
        time.sleep(0.9)
        st.markdown('<p class="countdown-text" style="background: linear-gradient(to right, #10B981, #3B82F6); -webkit-background-clip: text;">🚀 INITIALIZED</p>', unsafe_allow_html=True)
        time.sleep(0.7)
    st.session_state.countdown_complete = True
    placeholder.empty()
    st.rerun()

# 5. SaaS Dashboard Header Architecture
col_header, col_date = st.columns([2, 1])
with col_header:
    st.title("⚡ AKAMAL'S MISSION CONTROL")
with col_date:
    today_str = datetime.date.today().strftime("%A, %b %d, %Y")
    st.markdown(f"<p style='text-align: right; font-size: 1.1rem; color: #3B82F6 !important; font-weight: 600; padding-top: 25px;'>{today_str}</p>", unsafe_allow_html=True)

st.write("---")

# Metrics Calculation Matrix
total_tasks = 9
completed_tasks = 0

# 6. Grid Columns Layout (Splitting the screen into 2 Main functional tracks)
left_column, right_column = st.columns(2, gap="large")

with left_column:
    st.markdown('<div class="section-title">💻 1. MOLECULAR DYNAMICS (GROMACS)</div>', unsafe_allow_html=True)
    md_1 = st.checkbox("Check Param Utkarsh cluster queue, submit/monitor jobs, or review error logs", key="md1")
    md_2 = st.checkbox("Work on GROMACS pipelines (edit .mdp files, fix topology, or analyze trajectories)", key="md2")
    md_3 = st.checkbox("Read 1 research paper or methodology section specifically focusing on GQD / MD setups", key="md3")
    
    st.write("") # Spacer
    
    st.markdown('<div class="section-title">🔬 2. DFT SUB-MISSION</div>', unsafe_allow_html=True)
    dft_1 = st.checkbox("Run a convergence test or a variable-cell relaxation (Quantum ESPRESSO)", key="dft1")

with right_column:
    st.markdown('<div class="section-title">📚 3. GATE MISSION</div>', unsafe_allow_html=True)
    gate_1 = st.checkbox("Solve 10 past PYQs using only the Virtual Calculator", key="gt1")
    gate_2 = st.checkbox("Revise 1 Core Subject Formula Block (Thermodynamics/SOM/Physical Met)", key="gt2")
    gate_3 = st.checkbox("Spend 20 mins on Engineering Math or General Aptitude", key="gt3")
    
    st.write("") # Spacer
    
    st.markdown('<div class="section-title">🧠 4. FREE TIME & HABITS</div>', unsafe_allow_html=True)
    ml_1 = st.checkbox("Spend 20-30 mins learning ML concepts or writing data pipelines (Zero Stress)", key="ml1")
    sugar_health = st.checkbox("Strictly Less Sugar / Zero Added Sugar + Hydration check", key="health")

# Scoring Arithmetic
if md_1: completed_tasks += 1
if md_2: completed_tasks += 1
if md_3: completed_tasks += 1
if dft_1: completed_tasks += 1
if gate_1: completed_tasks += 1
if gate_2: completed_tasks += 1
if gate_3: completed_tasks += 1
if ml_1: completed_tasks += 1
if sugar_health: completed_tasks += 1

st.write("---")

# 7. Real-Time Telemetry / Progress Bar Section
st.markdown('<div class="section-title">📊 ANALYTICS TELEMETRY</div>', unsafe_allow_html=True)
progress_percentage = int((completed_tasks / total_tasks) * 100)
st.progress(completed_tasks / total_tasks)
st.write(f"**Current Efficiency Rating:** {completed_tasks}/{total_tasks} Objectives Secured ({progress_percentage}%)")

if progress_percentage == 100:
    st.balloons()
    st.success("Flawless execution cycle completed. Systems stable.")
elif progress_percentage >= 70:
    st.info("System health green. Core goals completely locked down.")
