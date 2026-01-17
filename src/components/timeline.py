"""
Timeline component for visualizing phases and months.
Horizontal scrollable timeline with status indicators.
"""

import streamlit as st
from typing import Optional


def render_timeline(
    items: list[dict],
    current_index: int = 0,
) -> None:
    """
    Render a horizontal timeline with phases using native Streamlit columns.

    Args:
        items: List of timeline item dicts with keys:
            - label: str (e.g., "Mes 1")
            - sublabel: Optional[str] (e.g., "Rehabilitacion")
            - status: str ("pending", "active", "completed")
        current_index: Index of the current/active item.
    """
    if not items:
        return

    # Use Streamlit columns for the timeline
    cols = st.columns(len(items))

    for i, (col, item) in enumerate(zip(cols, items)):
        with col:
            label = item.get("label", f"Item {i + 1}")
            sublabel = item.get("sublabel", "")
            status = item.get("status", "pending")

            # Override status based on current_index if not explicitly set
            if status == "pending":
                if i < current_index:
                    status = "completed"
                elif i == current_index:
                    status = "active"

            # Determine colors based on status
            if status == "completed":
                dot_bg = "#86EFAC"
                icon = "✓"
                border_style = "none"
            elif status == "active":
                dot_bg = "#FF6B9D"
                icon = str(i + 1)
                border_style = "none"
            else:
                dot_bg = "#F5E6D3"
                icon = str(i + 1)
                border_style = "2px solid #E0D5D0"

            # Render using simple st.markdown with minimal HTML
            st.markdown(
                f'<div style="text-align:center;">'
                f'<div style="width:32px;height:32px;border-radius:50%;background:{dot_bg};{border_style};'
                f'display:inline-flex;align-items:center;justify-content:center;color:white;font-weight:600;font-size:0.75rem;">{icon}</div>'
                f'<p style="font-size:0.7rem;margin:4px 0 0 0;color:#8B7E74;">{label}</p>'
                f'<p style="font-size:0.6rem;margin:0;color:#A8A29E;">{sublabel}</p>'
                f'</div>',
                unsafe_allow_html=True
            )


def render_phase_cards(
    phases: list[dict],
    current_phase: int = 0,
) -> None:
    """
    Render phase overview cards.

    Args:
        phases: List of phase dicts with keys:
            - name: str (e.g., "Rehabilitacion")
            - description: str
            - duration: str (e.g., "Meses 1-3")
            - status: str ("pending", "active", "completed")
            - kpis: Optional[list[dict]] with target metrics
        current_phase: Index of the current phase.
    """
    if not phases:
        return

    cols = st.columns(len(phases))

    for i, (col, phase) in enumerate(zip(cols, phases)):
        with col:
            name = phase.get("name", f"Fase {i + 1}")
            description = phase.get("description", "")
            duration = phase.get("duration", "")
            status = phase.get("status", "pending")

            if status == "pending" and i < current_phase:
                status = "completed"
            elif status == "pending" and i == current_phase:
                status = "active"

            # Status styling
            status_colors = {
                "pending": ("#8B7E74", "#F5E6D3"),
                "active": ("#FF6B9D", "#FFE4EE"),
                "completed": ("#22C55E", "#DCFCE7"),
            }
            text_color, bg_color = status_colors.get(status, status_colors["pending"])

            status_labels = {
                "pending": "Pendiente",
                "active": "En curso",
                "completed": "Completada",
            }
            status_label = status_labels.get(status, "Pendiente")

            st.markdown(f'''
            <div style="background: white; border-radius: 16px; padding: 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); border: 1px solid #F0E6E8; height: 100%; position: relative;">
                <span style="position: absolute; top: 16px; right: 16px; background: {bg_color}; color: {text_color}; padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; font-weight: 600;">{status_label}</span>
                <p style="font-family: Playfair Display, serif; font-size: 1.25rem; font-weight: 600; color: #3D3D3D; margin: 0 0 4px 0;">{name}</p>
                <p style="font-size: 0.875rem; color: #8B7E74; margin: 0 0 12px 0;">{duration}</p>
                <p style="font-size: 0.9rem; color: #3D3D3D; line-height: 1.5; margin: 0;">{description}</p>
            </div>
            ''', unsafe_allow_html=True)


def render_month_indicator(
    current_month: int = 1,
    total_months: int = 12,
) -> None:
    """
    Render a compact month progress indicator.

    Args:
        current_month: Current month number (1-based).
        total_months: Total number of months.
    """
    months_html = ""

    for i in range(1, total_months + 1):
        if i < current_month:
            bg = "linear-gradient(135deg,#86EFAC 0%,#22C55E 100%)"
            color = "white"
        elif i == current_month:
            bg = "linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%)"
            color = "white"
        else:
            bg = "#F5E6D3"
            color = "#8B7E74"

        months_html += f'<div style="width:32px;height:32px;border-radius:50%;background:{bg};color:{color};display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:600;">{i}</div>'

    st.markdown(
        f'<div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;padding:16px;">{months_html}</div>',
        unsafe_allow_html=True
    )
