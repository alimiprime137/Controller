# Controller
# 🦅 Mission Control: Personal Engineering & Research Dashboard

A customized, responsive web application built with **Python** and **Streamlit** to automate, monitor, and track my daily academic and computational research engineering milestones. 

Deploying this dashboard live allows me to manage my high-performance computing (HPC) workflows, exam preparation, and personal health metrics directly from any mobile device or desktop.

---

## 🛠️ Integrated Core Sub-Systems

The dashboard organizes my daily workflow by strict architectural priority:

1. **💻 Capstone Project (Molecular Dynamics):** Managing GROMACS simulation pipelines, topology modifications, `.mdp` files, and monitoring queue states on the **Param Utkarsh Supercomputing Cluster**.
2. **📖 Literature Radar:** Tracking technical research papers, methodology breakdowns, and supplementary materials for Graphene Quantum Dots (GQDs).
3. **📚 GATE Mission:** Structured daily practice using official virtual calculators and core subject formula revisions (Thermodynamics, Strength of Materials, Physical Metallurgy).
4. **🔬 DFT Sub-Mission:** Coordinating electronic structure optimizations and structural relaxations (`vc-relax`) using **Quantum ESPRESSO**.
5. **🧠 Free Time ML Workflows:** Low-stress, hands-on tracking of Machine Learning pipelines, dataset generation, and molecular docking automation.
6. **🚫🍬 Health & Bio-Integrity:** Monitoring daily lifestyle parameters, hydration tracking, and sugar-intake constraints.

---

## 🎨 Design & UI Architecture

- **Glassmorphic Interface:** Leverages customized CSS injections inside Streamlit to build semi-transparent, modern visual frosted glass panels.
- **Dynamic 24-Hour Nature Wallpapers:** Built-in Python logic loops through high-definition nature backgrounds, shifting automatically every 24 hours based on the system date.
- **Micro-Animations & Interactive Hovers:** Features smooth, interactive CSS transitions (`transform: translateX(6px)`) and left-accent glowing borders when hovering over specific metrics or targets.
- **One-Time Session Initialization:** Uses `st.session_state` memory control to run an introductory terminal splash screen countdown sequence ("Hello Akamal Alimi... Mission starting 3, 2, 1...") exclusively on the initial daily boot-up.

---

## ⚙️ Local Development Installation

To run this control hub locally on your machine, clone the repository and initialize the Python runtime:

```bash
# Clone the workspace
git clone [https://github.com/YOUR_GITHUB_USERNAME/mission-control-dashboard.git](https://github.com/YOUR_GITHUB_USERNAME/mission-control-dashboard.git)

# Enter the directory
cd mission-control-dashboard

# Install necessary application frameworks
pip install streamlit

# Launch the server
streamlit run app.py
