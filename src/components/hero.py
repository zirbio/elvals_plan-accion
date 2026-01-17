"""
Hero section component for the dashboard.
Large gradient banner with key metrics.
"""

import streamlit as st
from typing import Optional


def render_hero(
    title: str = "Engagement Rate",
    current_value: str = "0.24%",
    target_value: str = "1.5%",
    subtitle: Optional[str] = None,
) -> None:
    """
    Render the hero section with animated values.

    Args:
        title: Small title above the values.
        current_value: Current metric value (large, left).
        target_value: Target metric value (right after arrow).
        subtitle: Optional subtitle below the values.
    """
    subtitle_html = ""
    if subtitle:
        subtitle_html = f'<div style="font-family:Montserrat,sans-serif;font-size:1.125rem;color:#3D3D3D;margin-top:8px;">{subtitle}</div>'

    st.markdown(
        f'<div style="background:linear-gradient(135deg,#FF6B9D15 0%,#C084FC15 100%);border-radius:24px;padding:48px;margin-bottom:32px;text-align:center;position:relative;overflow:hidden;">'
        f'<div style="font-family:Montserrat,sans-serif;font-size:1rem;font-weight:400;color:#8B7E74;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.1em;">{title}</div>'
        f'<div style="display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:8px;">'
        f'<span style="font-family:Playfair Display,serif;font-size:4rem;font-weight:700;background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;">{current_value}</span>'
        f'<span style="display:inline-flex;align-items:center;gap:8px;font-size:1.5rem;margin:0 16px;color:#D4AF37;">&#8594;</span>'
        f'<span style="font-family:Playfair Display,serif;font-size:4rem;font-weight:700;background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;">{target_value}</span>'
        f'</div>'
        f'{subtitle_html}'
        f'</div>',
        unsafe_allow_html=True
    )


def render_mini_hero(
    value: str,
    label: str,
    icon: Optional[str] = None,
) -> None:
    """
    Render a smaller hero-style highlight.

    Args:
        value: The main value to display.
        label: Label below the value.
        icon: Optional emoji icon.
    """
    icon_html = f'<span style="font-size:2rem;margin-bottom:8px;">{icon}</span>' if icon else ""

    st.markdown(
        f'<div style="background:linear-gradient(135deg,#FF6B9D15 0%,#C084FC15 100%);border-radius:16px;padding:24px;text-align:center;">'
        f'{icon_html}'
        f'<div style="font-family:Playfair Display,serif;font-size:2.5rem;font-weight:700;background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">{value}</div>'
        f'<div style="font-family:Montserrat,sans-serif;font-size:0.875rem;color:#8B7E74;margin-top:4px;">{label}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_focus_section(tasks: list[dict], max_items: int = 5) -> None:
    """
    Render the "Hoy Tu Enfoque" section with top tasks.

    Args:
        tasks: List of task dicts with keys: text, time, day.
        max_items: Maximum number of tasks to show.
    """
    st.markdown(
        '<div style="background:white;border-radius:16px;padding:24px;border:1px solid #F0E6E8;margin-top:24px;">'
        '<h3 style="font-family:Playfair Display,serif;font-size:1.25rem;color:#3D3D3D;margin-bottom:16px;display:flex;align-items:center;gap:8px;">'
        '<span style="font-size:1.5rem;"></span>'
        'Hoy Tu Enfoque'
        '</h3>',
        unsafe_allow_html=True
    )

    for i, task in enumerate(tasks[:max_items]):
        text = task.get("text", "")
        time = task.get("time", "")

        time_badge = f'<span style="font-size:0.75rem;font-weight:500;color:#8B7E74;background:#FFFBF7;padding:4px 10px;border-radius:9999px;">{time}</span>' if time else ""

        border_style = "1px solid #F0E6E8" if i < min(len(tasks), max_items) - 1 else "none"

        st.markdown(
            f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:{border_style};">'
            f'<span style="width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);color:white;display:flex;align-items:center;justify-content:center;font-size:0.875rem;font-weight:600;flex-shrink:0;">{i + 1}</span>'
            f'<span style="flex:1;color:#3D3D3D;font-size:0.9375rem;">{text}</span>'
            f'{time_badge}'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)
