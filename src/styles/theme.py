"""
Theme configuration for El Vals de la Novia dashboard.
Wedding-premium aesthetic with mobile-first design.
"""

# =============================================================================
# COLOR PALETTE - Wedding Themed
# =============================================================================

COLORS = {
    # Primary colors
    "blush": "#FF6B9D",
    "lavender": "#C084FC",

    # Background colors
    "cream": "#FFFBF7",
    "ivory": "#FDF8F3",
    "white": "#FFFFFF",

    # Accent colors
    "gold": "#D4AF37",
    "champagne": "#F5E6D3",

    # Text colors
    "charcoal": "#3D3D3D",
    "warm_gray": "#8B7E74",
    "light_gray": "#A8A29E",

    # Semantic colors
    "success": "#86EFAC",
    "success_bg": "#F0FDF4",
    "error": "#FCA5A5",
    "error_bg": "#FEF2F2",

    # Card/Border colors
    "border_light": "#F0E6E8",
    "border_lavender": "#E9D5FF",
}

# Gradients
GRADIENTS = {
    "primary": f"linear-gradient(135deg, {COLORS['blush']} 0%, {COLORS['lavender']} 100%)",
    "hero": f"linear-gradient(135deg, {COLORS['blush']}15 0%, {COLORS['lavender']}15 100%)",
    "card": f"linear-gradient(135deg, {COLORS['cream']} 0%, {COLORS['ivory']} 100%)",
    "gold_accent": f"linear-gradient(180deg, {COLORS['gold']} 0%, {COLORS['champagne']} 100%)",
}

# =============================================================================
# TYPOGRAPHY
# =============================================================================

FONTS = {
    "heading": "'Playfair Display', serif",
    "body": "'Montserrat', sans-serif",
}

# =============================================================================
# SPACING & SIZING
# =============================================================================

SPACING = {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px",
    "xxl": "48px",
}

BORDER_RADIUS = {
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "xl": "24px",
    "full": "9999px",
}

# =============================================================================
# CSS INJECTION
# =============================================================================

def get_google_fonts_css():
    """Returns the CSS for Google Fonts import."""
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap');
    </style>
    """

def get_base_css():
    """Returns the base CSS for the entire application."""
    return f"""
    <style>
        /* ===== ROOT VARIABLES ===== */
        :root {{
            --blush: {COLORS['blush']};
            --lavender: {COLORS['lavender']};
            --cream: {COLORS['cream']};
            --ivory: {COLORS['ivory']};
            --gold: {COLORS['gold']};
            --champagne: {COLORS['champagne']};
            --charcoal: {COLORS['charcoal']};
            --warm-gray: {COLORS['warm_gray']};
            --gradient-primary: {GRADIENTS['primary']};
        }}

        /* ===== GLOBAL STYLES ===== */
        .stApp {{
            font-family: {FONTS['body']};
            background-color: {COLORS['cream']};
        }}

        /* ===== TYPOGRAPHY ===== */
        h1, h2, h3, .heading {{
            font-family: {FONTS['heading']};
            color: {COLORS['charcoal']};
        }}

        h1 {{
            font-size: 2.5rem !important;
            font-weight: 600 !important;
            letter-spacing: -0.02em;
        }}

        h2 {{
            font-size: 1.75rem !important;
            font-weight: 500 !important;
        }}

        h3 {{
            font-size: 1.25rem !important;
            font-weight: 500 !important;
        }}

        p, span, label, .body-text {{
            font-family: {FONTS['body']};
            color: {COLORS['charcoal']};
        }}

        /* ===== LAYOUT ===== */
        .block-container {{
            padding: 2rem 2rem 8rem 2rem !important;
            max-width: 1200px !important;
        }}

        /* ===== HIDE STREAMLIT BRANDING ===== */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}

        /* ===== CUSTOM SCROLLBAR ===== */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: {COLORS['cream']};
        }}

        ::-webkit-scrollbar-thumb {{
            background: {COLORS['lavender']}50;
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: {COLORS['lavender']};
        }}

        /* ===== MOBILE RESPONSIVE ===== */
        @media (max-width: 768px) {{
            .block-container {{
                padding: 1rem 1rem 10rem 1rem !important;
            }}

            h1 {{
                font-size: 1.75rem !important;
            }}

            h2 {{
                font-size: 1.5rem !important;
            }}

            [data-testid="column"] {{
                width: 100% !important;
                flex: 1 1 100% !important;
            }}
        }}
    </style>
    """

def get_navigation_css():
    """Returns CSS for the navigation components."""
    return f"""
    <style>
        /* ===== TOP TABS (Desktop) ===== */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 0;
            background: {COLORS['white']};
            border-radius: {BORDER_RADIUS['lg']};
            padding: 4px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}

        .stTabs [data-baseweb="tab"] {{
            padding: 12px 24px;
            font-family: {FONTS['body']};
            font-weight: 500;
            font-size: 14px;
            color: {COLORS['warm_gray']};
            background: transparent;
            border-radius: {BORDER_RADIUS['md']};
            transition: all 0.3s ease;
        }}

        .stTabs [data-baseweb="tab"]:hover {{
            color: {COLORS['charcoal']};
            background: {COLORS['cream']};
        }}

        .stTabs [aria-selected="true"] {{
            background: {GRADIENTS['primary']} !important;
            color: white !important;
        }}

        .stTabs [data-baseweb="tab-highlight"] {{
            display: none;
        }}

        .stTabs [data-baseweb="tab-border"] {{
            display: none;
        }}

        /* ===== MOBILE RESPONSIVE TABS ===== */
        @media (max-width: 768px) {{
            /* Keep Streamlit tabs visible and scrollable on mobile */
            .stTabs [data-baseweb="tab-list"] {{
                flex-wrap: nowrap !important;
                overflow-x: auto !important;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: none;
                padding: 4px !important;
                gap: 4px !important;
            }}

            .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {{
                display: none;
            }}

            .stTabs [data-baseweb="tab"] {{
                flex-shrink: 0 !important;
                padding: 12px 16px !important;
                font-size: 13px !important;
                min-height: 44px;
            }}
        }}
    </style>
    """

def get_card_css():
    """Returns CSS for card components."""
    return f"""
    <style>
        /* ===== BASE CARD ===== */
        .premium-card {{
            background: {COLORS['white']};
            border-radius: {BORDER_RADIUS['lg']};
            padding: {SPACING['lg']};
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            border: 1px solid {COLORS['border_light']};
            transition: all 0.3s ease;
        }}

        .premium-card:hover {{
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-color: {COLORS['champagne']};
        }}

        /* ===== METRIC CARD ===== */
        .metric-card {{
            background: {COLORS['white']};
            border-radius: {BORDER_RADIUS['lg']};
            padding: {SPACING['lg']};
            border-left: 4px solid {COLORS['gold']};
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
        }}

        .metric-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        }}

        .metric-value {{
            font-family: {FONTS['heading']};
            font-size: 2rem;
            font-weight: 600;
            color: {COLORS['charcoal']};
            line-height: 1.2;
        }}

        .metric-label {{
            font-family: {FONTS['body']};
            font-size: 0.875rem;
            color: {COLORS['warm_gray']};
            margin-top: 4px;
        }}

        .metric-delta {{
            font-size: 0.75rem;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: {BORDER_RADIUS['full']};
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .metric-delta.positive {{
            background: {COLORS['success_bg']};
            color: #166534;
        }}

        .metric-delta.negative {{
            background: {COLORS['error_bg']};
            color: #991B1B;
        }}

        /* ===== TASK CARD ===== */
        .task-card {{
            background: {COLORS['white']};
            border-radius: {BORDER_RADIUS['md']};
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            border: 1px solid {COLORS['border_light']};
            transition: all 0.2s ease;
            cursor: pointer;
        }}

        .task-card:hover {{
            border-color: {COLORS['champagne']};
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}

        .task-card.completed {{
            background: {COLORS['success_bg']};
            border-color: #BBF7D0;
        }}

        .task-card.completed .task-text {{
            text-decoration: line-through;
            color: {COLORS['warm_gray']};
        }}

        .task-checkbox {{
            width: 28px;
            height: 28px;
            border-radius: 8px;
            border: 2px solid {COLORS['border_lavender']};
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }}

        .task-checkbox.checked {{
            background: {GRADIENTS['primary']};
            border-color: transparent;
        }}

        .task-checkbox.checked::after {{
            content: "\\2713";
            color: white;
            font-size: 16px;
            font-weight: bold;
        }}

        .task-text {{
            flex: 1;
            font-size: 0.9375rem;
            color: {COLORS['charcoal']};
        }}

        .task-time {{
            font-size: 0.75rem;
            font-weight: 500;
            color: {COLORS['warm_gray']};
            background: {COLORS['cream']};
            padding: 4px 10px;
            border-radius: {BORDER_RADIUS['full']};
        }}

        /* ===== COMPETITOR CARD ===== */
        .competitor-card {{
            background: {COLORS['white']};
            border-radius: {BORDER_RADIUS['lg']};
            padding: {SPACING['lg']};
            border: 1px solid {COLORS['border_light']};
            transition: all 0.3s ease;
        }}

        .competitor-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        }}

        .competitor-avatar {{
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: {GRADIENTS['primary']};
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 1.25rem;
        }}

        .competitor-name {{
            font-family: {FONTS['heading']};
            font-size: 1.125rem;
            font-weight: 600;
            color: {COLORS['charcoal']};
        }}

        .competitor-handle {{
            font-size: 0.875rem;
            color: {COLORS['warm_gray']};
        }}

        .competitor-followers {{
            font-family: {FONTS['heading']};
            font-size: 1.5rem;
            font-weight: 600;
            color: {COLORS['blush']};
        }}

        .competitor-model {{
            font-size: 0.75rem;
            background: {COLORS['cream']};
            padding: 4px 12px;
            border-radius: {BORDER_RADIUS['full']};
            color: {COLORS['charcoal']};
        }}
    </style>
    """

def get_progress_css():
    """Returns CSS for progress components."""
    return f"""
    <style>
        /* ===== PROGRESS BAR ===== */
        .progress-container {{
            background-color: {COLORS['cream']};
            border-radius: {BORDER_RADIUS['full']};
            padding: 4px;
            margin: 12px 0 24px 0;
        }}

        .progress-bar {{
            background: {GRADIENTS['primary']};
            border-radius: {BORDER_RADIUS['full']};
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 13px;
            font-family: {FONTS['body']};
            transition: width 0.5s ease;
            min-width: 60px;
        }}

        /* ===== PROGRESS RING ===== */
        .progress-ring-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }}

        .progress-ring {{
            transform: rotate(-90deg);
        }}

        .progress-ring-bg {{
            fill: none;
            stroke: {COLORS['cream']};
            stroke-width: 8;
        }}

        .progress-ring-fill {{
            fill: none;
            stroke: url(#gradient);
            stroke-width: 8;
            stroke-linecap: round;
            transition: stroke-dashoffset 0.5s ease;
        }}

        .progress-ring-text {{
            font-family: {FONTS['heading']};
            font-size: 2rem;
            font-weight: 600;
            fill: {COLORS['charcoal']};
        }}
    </style>
    """

def get_hero_css():
    """Returns CSS for hero section."""
    return f"""
    <style>
        /* ===== HERO SECTION ===== */
        .hero-section {{
            background: {GRADIENTS['hero']};
            border-radius: {BORDER_RADIUS['xl']};
            padding: {SPACING['xxl']};
            margin-bottom: {SPACING['xl']};
            text-align: center;
            position: relative;
            overflow: hidden;
        }}

        .hero-section::before {{
            content: "";
            position: absolute;
            top: -50%;
            right: -50%;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, {COLORS['lavender']}10 0%, transparent 70%);
            pointer-events: none;
        }}

        .hero-title {{
            font-family: {FONTS['heading']};
            font-size: 1rem;
            font-weight: 400;
            color: {COLORS['warm_gray']};
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}

        .hero-value {{
            font-family: {FONTS['heading']};
            font-size: 4rem;
            font-weight: 700;
            background: {GRADIENTS['primary']};
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
        }}

        .hero-subtitle {{
            font-family: {FONTS['body']};
            font-size: 1.125rem;
            color: {COLORS['charcoal']};
            margin-top: 8px;
        }}

        .hero-arrow {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 1.5rem;
            margin: 0 16px;
            color: {COLORS['gold']};
        }}

        @media (max-width: 768px) {{
            .hero-section {{
                padding: {SPACING['lg']};
            }}

            .hero-value {{
                font-size: 2.5rem;
            }}
        }}
    </style>
    """

def get_day_section_css():
    """Returns CSS for day sections in checklist."""
    return f"""
    <style>
        /* ===== DAY SECTION ===== */
        .day-header {{
            background: {GRADIENTS['primary']};
            color: white;
            padding: 12px 20px;
            border-radius: {BORDER_RADIUS['md']};
            margin: 24px 0 12px 0;
            font-family: {FONTS['heading']};
            font-weight: 500;
            font-size: 1rem;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .day-header .icon {{
            font-size: 1.25rem;
        }}

        .day-tasks {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            padding-left: 8px;
        }}

        /* ===== WEEK SELECTOR ===== */
        .week-tabs {{
            display: flex;
            gap: 8px;
            margin-bottom: 24px;
            flex-wrap: wrap;
        }}

        .week-tab {{
            padding: 10px 20px;
            border-radius: {BORDER_RADIUS['full']};
            font-family: {FONTS['body']};
            font-weight: 500;
            font-size: 0.875rem;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 2px solid {COLORS['border_light']};
            background: {COLORS['white']};
            color: {COLORS['charcoal']};
        }}

        .week-tab:hover {{
            border-color: {COLORS['lavender']};
        }}

        .week-tab.active {{
            background: {GRADIENTS['primary']};
            border-color: transparent;
            color: white;
        }}
    </style>
    """

def get_timeline_css():
    """Returns CSS for timeline component."""
    return f"""
    <style>
        /* ===== TIMELINE ===== */
        .timeline-container {{
            display: flex;
            gap: 0;
            overflow-x: auto;
            padding: 20px 0;
            -webkit-overflow-scrolling: touch;
        }}

        .timeline-item {{
            flex: 0 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 100px;
            position: relative;
        }}

        .timeline-item::after {{
            content: "";
            position: absolute;
            top: 20px;
            left: 50%;
            width: 100%;
            height: 3px;
            background: {COLORS['border_light']};
            z-index: 0;
        }}

        .timeline-item:last-child::after {{
            display: none;
        }}

        .timeline-item.active::after {{
            background: {GRADIENTS['primary']};
        }}

        .timeline-dot {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: {COLORS['white']};
            border: 3px solid {COLORS['border_light']};
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1;
            transition: all 0.3s ease;
        }}

        .timeline-item.active .timeline-dot {{
            background: {GRADIENTS['primary']};
            border-color: transparent;
            color: white;
        }}

        .timeline-item.completed .timeline-dot {{
            background: {COLORS['success']};
            border-color: transparent;
            color: white;
        }}

        .timeline-label {{
            margin-top: 12px;
            font-size: 0.75rem;
            color: {COLORS['warm_gray']};
            text-align: center;
            font-weight: 500;
        }}

        .timeline-item.active .timeline-label {{
            color: {COLORS['charcoal']};
            font-weight: 600;
        }}
    </style>
    """

def get_all_css():
    """Returns all CSS combined."""
    return (
        get_google_fonts_css() +
        get_base_css() +
        get_navigation_css() +
        get_card_css() +
        get_progress_css() +
        get_hero_css() +
        get_day_section_css() +
        get_timeline_css()
    )

def inject_css(st):
    """Injects all CSS into the Streamlit app."""
    st.markdown(get_all_css(), unsafe_allow_html=True)
