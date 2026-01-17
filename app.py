"""
El Vals de la Novia - Premium Wedding Dashboard
Dashboard de estrategia de Instagram con estetica wedding-premium.
"""

import streamlit as st
from pathlib import Path

# Import theme and styles
from src.styles.theme import inject_css

# Import state management
from src.utils.state import init_session_state, save_state

# Import pages
from src.pages.dashboard import render_dashboard
from src.pages.checklist import render_checklist
from src.pages.strategy import render_strategy
from src.pages.competitors import render_competitors

# =============================================================================
# PAGE CONFIG
# =============================================================================

st.set_page_config(
    page_title="El Vals de la Novia",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================================================================
# PATHS
# =============================================================================

DOCS_DIR = Path(__file__).parent / "docs" / "plans"

# =============================================================================
# INJECT CSS
# =============================================================================

inject_css(st)

# =============================================================================
# MOBILE BOTTOM NAVIGATION CSS
# =============================================================================

st.markdown("""
<style>
    /* ===== ADDITIONAL CHECKBOX STYLING ===== */
    .stCheckbox > label {
        padding: 14px 12px;
        font-size: 15px;
        line-height: 1.5;
        display: flex;
        align-items: center;
        border-bottom: 1px solid #F0E6E8;
        transition: all 0.2s ease;
        cursor: pointer;
        border-radius: 8px;
        margin: 2px 0;
    }

    .stCheckbox > label:hover {
        background-color: #FFFBF7;
        border-color: #F5E6D3;
    }

    .stCheckbox > label > div[data-testid="stCheckbox"] {
        margin-right: 12px;
    }

    /* Checkbox input styling */
    .stCheckbox input[type="checkbox"] {
        width: 24px;
        height: 24px;
        border-radius: 6px;
        border: 2px solid #E9D5FF;
        cursor: pointer;
    }

    .stCheckbox input[type="checkbox"]:checked {
        background: linear-gradient(135deg, #FF6B9D 0%, #C084FC 100%);
        border-color: transparent;
    }

    /* Mobile touch targets */
    @media (max-width: 768px) {
        .stCheckbox > label {
            padding: 16px 12px;
            min-height: 52px;
        }
    }

    /* ===== BOTTOM NAVIGATION FOR MOBILE ===== */
    .mobile-bottom-nav {
        display: none;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-top: 1px solid #F0E6E8;
        padding: 8px 0;
        padding-bottom: calc(8px + env(safe-area-inset-bottom, 0));
        z-index: 1000;
    }

    .mobile-bottom-nav .nav-items {
        display: flex;
        justify-content: space-around;
        max-width: 500px;
        margin: 0 auto;
    }

    .mobile-bottom-nav .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        padding: 8px 16px;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        color: #8B7E74;
    }

    .mobile-bottom-nav .nav-item:hover {
        background: #FFFBF7;
    }

    .mobile-bottom-nav .nav-item.active {
        color: #FF6B9D;
    }

    .mobile-bottom-nav .nav-item .icon {
        font-size: 22px;
    }

    .mobile-bottom-nav .nav-item .label {
        font-size: 10px;
        font-weight: 500;
    }

    @media (max-width: 768px) {
        .mobile-bottom-nav {
            display: block;
        }

        /* Hide top tabs on mobile */
        .stTabs [data-baseweb="tab-list"] {
            flex-wrap: nowrap;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }

        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            display: none;
        }

        .stTabs [data-baseweb="tab"] {
            flex-shrink: 0;
            padding: 10px 16px;
            font-size: 13px;
        }
    }

    /* ===== EXPANDER STYLING ===== */
    .streamlit-expanderHeader {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        font-weight: 500;
        color: #3D3D3D;
        background: #FFFBF7;
        border-radius: 12px;
    }

    .streamlit-expanderContent {
        border: 1px solid #F0E6E8;
        border-top: none;
        border-radius: 0 0 12px 12px;
    }

    /* ===== DIVIDER STYLING ===== */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #F0E6E8, transparent);
        margin: 24px 0;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HEADER
# =============================================================================

st.markdown("""
<div style="
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
">
    <span style="font-size: 2.5rem;"></span>
    <div>
        <h1 style="
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            font-weight: 600;
            color: #3D3D3D;
            margin: 0;
            line-height: 1.2;
        ">El Vals de la Novia</h1>
        <p style="
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            color: #8B7E74;
            margin: 4px 0 0 0;
        ">Dashboard de Estrategia de Instagram</p>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# INITIALIZE STATE
# =============================================================================

state = init_session_state(st)

# =============================================================================
# MAIN NAVIGATION
# =============================================================================

tab1, tab2, tab3, tab4 = st.tabs([
    " Dashboard",
    " Plan Semanal",
    " Estrategia",
    " Competidores",
])

# =============================================================================
# TAB CONTENT
# =============================================================================

with tab1:
    render_dashboard(DOCS_DIR, state)

with tab2:
    updated_state = render_checklist(DOCS_DIR, state)
    if updated_state != state:
        st.session_state.checkbox_state = updated_state

with tab3:
    render_strategy(DOCS_DIR)

with tab4:
    render_competitors(DOCS_DIR)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    <p style="
        font-size: 0.8rem;
        color: #8B7E74;
    ">Ultima actualizacion de documentos: 17 de enero de 2026</p>
    """, unsafe_allow_html=True)

with col2:
    with st.expander(" Opciones"):
        if st.button(" Reiniciar progreso", type="secondary", use_container_width=True):
            st.session_state.checkbox_state = {}
            save_state({})
            st.rerun()

# =============================================================================
# MOBILE BOTTOM NAVIGATION (HTML)
# =============================================================================

st.markdown("""
<div class="mobile-bottom-nav">
    <div class="nav-items">
        <div class="nav-item active">
            <span class="icon"></span>
            <span class="label">Dashboard</span>
        </div>
        <div class="nav-item">
            <span class="icon"></span>
            <span class="label">Checklist</span>
        </div>
        <div class="nav-item">
            <span class="icon"></span>
            <span class="label">Estrategia</span>
        </div>
        <div class="nav-item">
            <span class="icon"></span>
            <span class="label">Competidores</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
