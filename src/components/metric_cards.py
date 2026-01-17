"""
Metric card components for the dashboard.
Premium wedding-themed design with gold accents.
"""

import streamlit as st
from typing import Optional


def render_metric_card(
    value: str,
    label: str,
    delta: Optional[str] = None,
    delta_positive: bool = True,
    icon: Optional[str] = None,
) -> None:
    """
    Render a premium metric card with gold accent border.

    Args:
        value: The main metric value to display.
        label: The label describing the metric.
        delta: Optional change indicator (e.g., "+12%").
        delta_positive: Whether the delta represents a positive change.
        icon: Optional emoji/icon to display.
    """
    delta_html = ""
    if delta:
        delta_bg = "#F0FDF4" if delta_positive else "#FEF2F2"
        delta_color = "#166534" if delta_positive else "#991B1B"
        arrow = "↑" if delta_positive else "↓"
        delta_html = f'<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;border-radius:9999px;background:{delta_bg};color:{delta_color};">{arrow} {delta}</span>'

    icon_html = f'<span style="font-size:1.5rem;margin-right:8px;">{icon}</span>' if icon else ""

    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:24px;border-left:4px solid #D4AF37;box-shadow:0 2px 12px rgba(0,0,0,0.04);">'
        f'<div style="display:flex;align-items:flex-start;justify-content:space-between;">'
        f'<div>'
        f'<p style="font-family:Playfair Display,serif;font-size:2rem;font-weight:600;color:#3D3D3D;line-height:1.2;margin:0;">{icon_html}{value}</p>'
        f'<p style="font-family:Montserrat,sans-serif;font-size:0.875rem;color:#8B7E74;margin:4px 0 0 0;">{label}</p>'
        f'</div>'
        f'{delta_html}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_metric_grid(metrics: list[dict]) -> None:
    """
    Render a grid of metric cards.

    Args:
        metrics: List of metric dictionaries with keys:
            - value: str
            - label: str
            - delta: Optional[str]
            - delta_positive: Optional[bool]
            - icon: Optional[str]
    """
    # Determine number of columns based on metrics count
    num_metrics = len(metrics)
    if num_metrics <= 2:
        cols = st.columns(num_metrics)
    elif num_metrics <= 4:
        cols = st.columns(min(num_metrics, 4))
    else:
        cols = st.columns(4)

    for i, metric in enumerate(metrics):
        with cols[i % len(cols)]:
            render_metric_card(
                value=metric.get("value", "0"),
                label=metric.get("label", ""),
                delta=metric.get("delta"),
                delta_positive=metric.get("delta_positive", True),
                icon=metric.get("icon"),
            )


def render_kpi_comparison(
    label: str,
    current: float,
    target: float,
    unit: str = "",
    show_bar: bool = True,
) -> None:
    """
    Render a KPI comparison with current vs target.

    Args:
        label: The KPI label.
        current: Current value.
        target: Target value.
        unit: Unit suffix (e.g., "%", "K").
        show_bar: Whether to show a progress bar.
    """
    progress = min((current / target * 100) if target > 0 else 0, 100)
    status_color = "#86EFAC" if current >= target else "#FBBF24" if progress >= 50 else "#FCA5A5"

    bar_html = ""
    if show_bar:
        bar_html = (
            f'<div style="background:#FFFBF7;border-radius:9999px;padding:2px;margin:8px 0;">'
            f'<div style="width:{progress}%;min-width:20px;height:8px;border-radius:9999px;'
            f'background:linear-gradient(90deg,{status_color} 0%,{status_color}CC 100%);"></div>'
            f'</div>'
        )

    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:16px;border:1px solid #F0E6E8;box-shadow:0 2px 12px rgba(0,0,0,0.04);">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">'
        f'<span style="font-weight:500;color:#3D3D3D;">{label}</span>'
        f'<span style="font-size:0.875rem;color:#8B7E74;">{current}{unit} / {target}{unit}</span>'
        f'</div>'
        f'{bar_html}'
        f'</div>',
        unsafe_allow_html=True
    )


def render_stat_pill(value: str, label: str, color: str = "lavender") -> str:
    """
    Return HTML for a small stat pill.

    Args:
        value: The stat value.
        label: The stat label.
        color: Color variant (lavender, blush, gold).

    Returns:
        str: HTML string for the pill.
    """
    colors = {
        "lavender": ("#C084FC", "#F3E8FF"),
        "blush": ("#FF6B9D", "#FFE4EE"),
        "gold": ("#D4AF37", "#FEF3C7"),
    }
    text_color, bg_color = colors.get(color, colors["lavender"])

    return f"""
    <span style="
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 4px 12px;
        border-radius: 9999px;
        background: {bg_color};
        color: {text_color};
        font-size: 0.75rem;
        font-weight: 600;
    ">
        <span>{value}</span>
        <span style="opacity: 0.8;">{label}</span>
    </span>
    """
