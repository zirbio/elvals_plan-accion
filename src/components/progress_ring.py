"""
Circular progress ring component.
SVG-based with gradient fill and animations.
"""

import streamlit as st
from typing import Optional


def render_progress_ring(
    percentage: float,
    size: int = 120,
    stroke_width: int = 10,
    label: Optional[str] = None,
    show_percentage: bool = True,
) -> None:
    """
    Render a circular progress ring with gradient.

    Args:
        percentage: Progress percentage (0-100).
        size: Diameter of the ring in pixels.
        stroke_width: Width of the ring stroke.
        label: Optional label below the percentage.
        show_percentage: Whether to show the percentage number.
    """
    # Clamp percentage
    percentage = max(0, min(100, percentage))

    # Calculate SVG parameters
    radius = (size - stroke_width) / 2
    center = size / 2
    circumference = 2 * 3.14159 * radius
    stroke_dashoffset = circumference * (1 - percentage / 100)

    # Gradient definition
    gradient_id = f"ring-gradient-{id(percentage)}"

    center_content = ""
    if show_percentage:
        center_content = f"""
        <text
            x="{center}"
            y="{center}"
            text-anchor="middle"
            dominant-baseline="central"
            style="
                font-family: 'Playfair Display', serif;
                font-size: {size * 0.25}px;
                font-weight: 600;
                fill: #3D3D3D;
            "
        >{int(percentage)}%</text>
        """

    label_html = ""
    if label:
        label_html = f'<p style="font-family:Montserrat,sans-serif;font-size:0.875rem;color:#8B7E74;margin:8px 0 0 0;text-align:center;">{label}</p>'

    st.markdown(
        f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;">'
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="transform:rotate(-90deg);">'
        f'<defs><linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">'
        f'<stop offset="0%" style="stop-color:#FF6B9D;" />'
        f'<stop offset="100%" style="stop-color:#C084FC;" />'
        f'</linearGradient></defs>'
        f'<circle cx="{center}" cy="{center}" r="{radius}" fill="none" stroke="#F5E6D3" stroke-width="{stroke_width}" />'
        f'<circle cx="{center}" cy="{center}" r="{radius}" fill="none" stroke="url(#{gradient_id})" stroke-width="{stroke_width}" stroke-linecap="round" stroke-dasharray="{circumference}" stroke-dashoffset="{stroke_dashoffset}" />'
        f'<g style="transform:rotate(90deg);transform-origin:center;">{center_content}</g>'
        f'</svg>'
        f'{label_html}'
        f'</div>',
        unsafe_allow_html=True
    )


def render_mini_progress_ring(
    percentage: float,
    size: int = 48,
    stroke_width: int = 4,
) -> str:
    """
    Return HTML for a mini progress ring (inline use).

    Args:
        percentage: Progress percentage (0-100).
        size: Diameter in pixels.
        stroke_width: Width of stroke.

    Returns:
        str: HTML string for the mini ring.
    """
    percentage = max(0, min(100, percentage))
    radius = (size - stroke_width) / 2
    center = size / 2
    circumference = 2 * 3.14159 * radius
    stroke_dashoffset = circumference * (1 - percentage / 100)
    gradient_id = f"mini-ring-{id(percentage)}"

    return f"""
    <svg
        width="{size}"
        height="{size}"
        viewBox="0 0 {size} {size}"
        style="transform: rotate(-90deg); display: inline-block; vertical-align: middle;"
    >
        <defs>
            <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color: #FF6B9D;" />
                <stop offset="100%" style="stop-color: #C084FC;" />
            </linearGradient>
        </defs>
        <circle
            cx="{center}" cy="{center}" r="{radius}"
            fill="none" stroke="#F5E6D3" stroke-width="{stroke_width}"
        />
        <circle
            cx="{center}" cy="{center}" r="{radius}"
            fill="none" stroke="url(#{gradient_id})"
            stroke-width="{stroke_width}" stroke-linecap="round"
            stroke-dasharray="{circumference}"
            stroke-dashoffset="{stroke_dashoffset}"
        />
    </svg>
    """


def render_progress_bar(
    completed: int,
    total: int,
    show_text: bool = True,
) -> None:
    """
    Render a horizontal progress bar.

    Args:
        completed: Number of completed items.
        total: Total number of items.
        show_text: Whether to show the progress text.
    """
    if total == 0:
        return

    percentage = int((completed / total) * 100)
    text = f"{percentage}% ({completed}/{total})" if show_text else ""

    st.markdown(f'''
    <div style="background-color: #FFFBF7; border-radius: 9999px; padding: 4px; margin: 12px 0 24px 0;">
        <div style="background: linear-gradient(135deg, #FF6B9D 0%, #C084FC 100%); border-radius: 9999px; height: 28px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 13px; font-family: Montserrat, sans-serif; min-width: 60px; width: {max(percentage, 8)}%;">{text}</div>
    </div>
    ''', unsafe_allow_html=True)
