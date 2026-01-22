"""
Insight card components for the Insights page.
Premium wedding-themed design with comparison visuals.
"""

import streamlit as st
from typing import Optional


def render_comparison_metric(
    name: str,
    best: str | int,
    worst: str | int,
    ratio: str,
    icon: str = "",
) -> None:
    """
    Render a comparison metric card showing best vs worst.

    Args:
        name: Metric name.
        best: Best posts value.
        worst: Worst posts value.
        ratio: Ratio or difference display.
        icon: Emoji icon.
    """
    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:20px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;height:100%;">'
        f'<div style="text-align:center;margin-bottom:12px;">'
        f'<span style="font-size:1.5rem;">{icon}</span>'
        f'</div>'
        f'<div style="font-family:Montserrat,sans-serif;font-size:0.75rem;color:#8B7E74;text-align:center;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">{name}</div>'
        f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;">'
        f'<div style="text-align:center;flex:1;">'
        f'<div style="font-size:0.65rem;color:#16A34A;font-weight:500;">MEJOR</div>'
        f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#166534;">{best:,}</div>'
        f'</div>'
        f'<div style="font-size:0.875rem;color:#8B7E74;">vs</div>'
        f'<div style="text-align:center;flex:1;">'
        f'<div style="font-size:0.65rem;color:#DC2626;font-weight:500;">PEOR</div>'
        f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#991B1B;">{worst:,}</div>'
        f'</div>'
        f'</div>'
        f'<div style="text-align:center;margin-top:12px;padding-top:12px;border-top:1px solid #F0E6E8;">'
        f'<span style="background:linear-gradient(135deg,#D4AF37 0%,#F5D77D 100%);color:white;padding:4px 12px;border-radius:9999px;font-size:0.75rem;font-weight:600;">{ratio}</span>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_comparison_metric_text(
    name: str,
    best: str,
    worst: str,
    ratio: str,
    icon: str = "",
) -> None:
    """
    Render a comparison metric card with text values (for percentages).

    Args:
        name: Metric name.
        best: Best posts value as string.
        worst: Worst posts value as string.
        ratio: Ratio or difference display.
        icon: Emoji icon.
    """
    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:20px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;height:100%;">'
        f'<div style="text-align:center;margin-bottom:12px;">'
        f'<span style="font-size:1.5rem;">{icon}</span>'
        f'</div>'
        f'<div style="font-family:Montserrat,sans-serif;font-size:0.75rem;color:#8B7E74;text-align:center;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">{name}</div>'
        f'<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;">'
        f'<div style="text-align:center;flex:1;">'
        f'<div style="font-size:0.65rem;color:#16A34A;font-weight:500;">MEJOR</div>'
        f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#166534;">{best}</div>'
        f'</div>'
        f'<div style="font-size:0.875rem;color:#8B7E74;">vs</div>'
        f'<div style="text-align:center;flex:1;">'
        f'<div style="font-size:0.65rem;color:#DC2626;font-weight:500;">PEOR</div>'
        f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#991B1B;">{worst}</div>'
        f'</div>'
        f'</div>'
        f'<div style="text-align:center;margin-top:12px;padding-top:12px;border-top:1px solid #F0E6E8;">'
        f'<span style="background:linear-gradient(135deg,#D4AF37 0%,#F5D77D 100%);color:white;padding:4px 12px;border-radius:9999px;font-size:0.75rem;font-weight:600;">{ratio}</span>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_lever_card(
    title: str,
    impact: str,
    insight: str,
    action: str,
    icon: str = "",
) -> None:
    """
    Render a success lever card with insight and action.

    Args:
        title: Lever title.
        impact: Impact level (ALTO, MEDIO, BAJO).
        insight: Data-driven insight.
        action: Recommended action.
        icon: Emoji icon.
    """
    # Impact colors
    impact_colors = {
        "ALTO": ("#D4AF37", "#FEF3C7"),
        "MEDIO": ("#C084FC", "#F3E8FF"),
        "BAJO": ("#8B7E74", "#F5F5F4"),
    }
    text_color, bg_color = impact_colors.get(impact, impact_colors["MEDIO"])

    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;border-left:4px solid {text_color};height:100%;">'
        f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">'
        f'<div style="display:flex;align-items:center;gap:12px;">'
        f'<span style="font-size:1.75rem;">{icon}</span>'
        f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#3D3D3D;">{title}</div>'
        f'</div>'
        f'<span style="background:{bg_color};color:{text_color};padding:4px 10px;border-radius:9999px;font-size:0.65rem;font-weight:700;letter-spacing:0.5px;">{impact}</span>'
        f'</div>'
        f'<div style="background:#FFFBF7;border-radius:8px;padding:12px;margin-bottom:12px;">'
        f'<div style="font-size:0.7rem;color:#8B7E74;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:4px;">Insight</div>'
        f'<div style="font-size:0.875rem;color:#3D3D3D;line-height:1.5;">{insight}</div>'
        f'</div>'
        f'<div style="background:#F0FDF4;border-radius:8px;padding:12px;">'
        f'<div style="font-size:0.7rem;color:#166534;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:4px;">Accion</div>'
        f'<div style="font-size:0.875rem;color:#166534;line-height:1.5;font-weight:500;">{action}</div>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_do_dont_section(do_items: list[str], dont_items: list[str]) -> None:
    """
    Render a two-column DO vs DON'T section.

    Args:
        do_items: List of things to do.
        dont_items: List of things to avoid.
    """
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div style="background:#F0FDF4;border-radius:16px;padding:24px;border:2px solid #86EFAC;">'
            '<div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">'
            '<span style="font-size:1.5rem;"></span>'
            '<span style="font-family:Playfair Display,serif;font-size:1.25rem;font-weight:600;color:#166534;">HACER</span>'
            '</div>',
            unsafe_allow_html=True
        )
        for item in do_items:
            st.markdown(
                f'<div style="display:flex;align-items:flex-start;gap:8px;margin-bottom:10px;font-size:0.875rem;color:#166534;">'
                f'<span style="color:#16A34A;font-weight:bold;"></span>'
                f'<span>{item}</span>'
                f'</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(
            '<div style="background:#FEF2F2;border-radius:16px;padding:24px;border:2px solid #FCA5A5;">'
            '<div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">'
            '<span style="font-size:1.5rem;"></span>'
            '<span style="font-family:Playfair Display,serif;font-size:1.25rem;font-weight:600;color:#991B1B;">EVITAR</span>'
            '</div>',
            unsafe_allow_html=True
        )
        for item in dont_items:
            st.markdown(
                f'<div style="display:flex;align-items:flex-start;gap:8px;margin-bottom:10px;font-size:0.875rem;color:#991B1B;">'
                f'<span style="color:#DC2626;font-weight:bold;"></span>'
                f'<span>{item}</span>'
                f'</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)


def render_hashtag_clouds(
    good_hashtags: list[tuple[str, int]],
    bad_hashtags: list[tuple[str, int]],
) -> None:
    """
    Render hashtag clouds for effective vs ineffective hashtags.

    Args:
        good_hashtags: List of (hashtag, count) tuples for effective tags.
        bad_hashtags: List of (hashtag, count) tuples for ineffective tags.
    """
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:20px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:600;color:#166534;margin-bottom:16px;display:flex;align-items:center;gap:8px;">'
            '<span></span> Hashtags Efectivos'
            '</div>'
            '<div style="display:flex;flex-wrap:wrap;gap:8px;">',
            unsafe_allow_html=True
        )
        for tag, count in good_hashtags[:8]:
            size = min(0.75 + (count / 10) * 0.25, 1.0)
            st.markdown(
                f'<span style="background:#DCFCE7;color:#166534;padding:6px 12px;border-radius:9999px;font-size:{size}rem;font-weight:500;">#{tag}</span>',
                unsafe_allow_html=True
            )
        st.markdown('</div></div>', unsafe_allow_html=True)

    with col2:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:20px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:600;color:#991B1B;margin-bottom:16px;display:flex;align-items:center;gap:8px;">'
            '<span></span> Hashtags a Evitar'
            '</div>'
            '<div style="display:flex;flex-wrap:wrap;gap:8px;">',
            unsafe_allow_html=True
        )
        for tag, count in bad_hashtags[:8]:
            size = min(0.75 + (count / 10) * 0.25, 1.0)
            st.markdown(
                f'<span style="background:#FEE2E2;color:#991B1B;padding:6px 12px;border-radius:9999px;font-size:{size}rem;font-weight:500;">#{tag}</span>',
                unsafe_allow_html=True
            )
        st.markdown('</div></div>', unsafe_allow_html=True)


def render_posts_table(posts: list[dict], title: str, is_best: bool = True) -> None:
    """
    Render a table of posts with key metrics.

    Args:
        posts: List of post dictionaries.
        title: Table title.
        is_best: Whether these are best posts (for styling).
    """
    accent_color = "#166534" if is_best else "#991B1B"
    bg_color = "#F0FDF4" if is_best else "#FEF2F2"

    st.markdown(
        f'<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:600;color:{accent_color};margin-bottom:12px;">{title}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="background:white;border-radius:12px;overflow:hidden;border:1px solid #F0E6E8;">'
        f'<table style="width:100%;border-collapse:collapse;font-size:0.8rem;">'
        f'<thead>'
        f'<tr style="background:{bg_color};">'
        f'<th style="padding:10px 8px;text-align:left;color:#8B7E74;font-weight:500;">Fecha</th>'
        f'<th style="padding:10px 8px;text-align:right;color:#8B7E74;font-weight:500;">Views</th>'
        f'<th style="padding:10px 8px;text-align:right;color:#8B7E74;font-weight:500;">Likes</th>'
        f'<th style="padding:10px 8px;text-align:right;color:#8B7E74;font-weight:500;">Guard.</th>'
        f'<th style="padding:10px 8px;text-align:left;color:#8B7E74;font-weight:500;">Caption</th>'
        f'</tr>'
        f'</thead>'
        f'<tbody>',
        unsafe_allow_html=True
    )

    for i, post in enumerate(posts[:10]):
        row_bg = "#FFFBF7" if i % 2 == 0 else "white"
        caption_short = post.get("caption", "")[:60] + "..." if len(post.get("caption", "")) > 60 else post.get("caption", "")

        st.markdown(
            f'<tr style="background:{row_bg};border-bottom:1px solid #F0E6E8;">'
            f'<td style="padding:8px;font-size:0.75rem;">{post.get("fecha", "-")[:10]}</td>'
            f'<td style="padding:8px;text-align:right;font-weight:500;">{post.get("views", 0):,}</td>'
            f'<td style="padding:8px;text-align:right;">{post.get("likes", 0):,}</td>'
            f'<td style="padding:8px;text-align:right;">{post.get("saves", 0):,}</td>'
            f'<td style="padding:8px;font-size:0.7rem;color:#8B7E74;max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{caption_short}</td>'
            f'</tr>',
            unsafe_allow_html=True
        )

    st.markdown('</tbody></table></div>', unsafe_allow_html=True)


def render_recommendation_card(
    title: str,
    description: str,
    icon: str,
    priority: int = 1,
) -> None:
    """
    Render a recommendation card.

    Args:
        title: Recommendation title.
        description: Detailed description.
        icon: Emoji icon.
        priority: Priority level (1-3).
    """
    priority_colors = {
        1: "#D4AF37",
        2: "#C084FC",
        3: "#8B7E74",
    }
    border_color = priority_colors.get(priority, "#D4AF37")

    st.markdown(
        f'<div style="background:white;border-radius:12px;padding:20px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;border-top:3px solid {border_color};">'
        f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">'
        f'<span style="font-size:1.5rem;">{icon}</span>'
        f'<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:600;color:#3D3D3D;">{title}</div>'
        f'</div>'
        f'<div style="font-size:0.875rem;color:#8B7E74;line-height:1.6;">{description}</div>'
        f'</div>',
        unsafe_allow_html=True
    )
