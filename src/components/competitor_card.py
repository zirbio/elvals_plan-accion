"""
Competitor card component for the analysis section.
Displays competitor information in a visually appealing card.
"""

import streamlit as st
from typing import Optional


def render_competitor_card(
    name: str,
    handle: str,
    followers: str,
    model: str,
    avatar_initials: Optional[str] = None,
    differentiator: Optional[str] = None,
    priority: Optional[str] = None,
) -> None:
    """
    Render a competitor card with avatar and details.

    Args:
        name: Competitor's display name.
        handle: Instagram handle (e.g., "@invitada_perfecta").
        followers: Follower count (e.g., "500K").
        model: Business model description.
        avatar_initials: 2-letter initials for avatar (auto-generated if None).
        differentiator: Key differentiator/strength.
        priority: Priority level ("1", "2", etc.) for display badge.
    """
    # Generate initials if not provided
    if not avatar_initials:
        words = name.split()
        if len(words) >= 2:
            avatar_initials = words[0][0] + words[1][0]
        else:
            avatar_initials = name[:2]
        avatar_initials = avatar_initials.upper()

    priority_badge = ""
    if priority:
        priority_badge = f'<span style="position:absolute;top:12px;right:12px;background:linear-gradient(135deg,#D4AF37 0%,#F5E6D3 100%);color:white;width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:700;">{priority}</span>'

    diff_html = ""
    if differentiator:
        diff_html = f'<p style="margin-top:12px;padding-top:12px;border-top:1px solid #F0E6E8;font-size:0.8rem;color:#8B7E74;font-style:italic;">"{differentiator}"</p>'

    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:24px;border:1px solid #F0E6E8;position:relative;">'
        f'{priority_badge}'
        f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">'
        f'<div style="width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);display:flex;align-items:center;justify-content:center;color:white;font-weight:600;font-size:1.25rem;">{avatar_initials}</div>'
        f'<div>'
        f'<p style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#3D3D3D;margin:0;">{name}</p>'
        f'<p style="font-size:0.875rem;color:#8B7E74;margin:0;">{handle}</p>'
        f'</div>'
        f'</div>'
        f'<div style="display:flex;justify-content:space-between;align-items:center;">'
        f'<div>'
        f'<p style="font-family:Playfair Display,serif;font-size:1.5rem;font-weight:600;color:#FF6B9D;margin:0;">{followers}</p>'
        f'<p style="font-size:0.75rem;color:#8B7E74;margin:0;">seguidores</p>'
        f'</div>'
        f'<span style="font-size:0.75rem;background:#FFFBF7;padding:4px 12px;border-radius:9999px;color:#3D3D3D;">{model}</span>'
        f'</div>'
        f'{diff_html}'
        f'</div>',
        unsafe_allow_html=True
    )


def render_competitor_grid(competitors: list[dict], cols: int = 3) -> None:
    """
    Render a grid of competitor cards.

    Args:
        competitors: List of competitor dicts with card attributes.
        cols: Number of columns (2-4).
    """
    columns = st.columns(min(cols, len(competitors)))

    for i, comp in enumerate(competitors):
        with columns[i % cols]:
            render_competitor_card(
                name=comp.get("name", ""),
                handle=comp.get("handle", ""),
                followers=comp.get("followers", "0"),
                model=comp.get("model", ""),
                avatar_initials=comp.get("avatar_initials"),
                differentiator=comp.get("differentiator"),
                priority=comp.get("priority"),
            )


def render_positioning_map() -> None:
    """
    Render a visual positioning map of competitors using Streamlit columns.
    Shows relative size/positioning in the market.
    """
    # Use a simpler grid-based approach with Streamlit columns
    competitors = [
        ("Invitada Perfecta", "~500K", "#FF6B9D", "IP"),
        ("Bodas.net", "303K", "#8B7E74", "BN"),
        ("Bridalada", "292K", "#C084FC", "BR"),
        ("Miss Cavallier", "281K", "#C084FC", "MC"),
        ("El Vals de la Novia", "115K", "#D4AF37", "EVLN"),
        ("Una Boda Original", "~115K", "#F5E6D3", "UBO"),
        ("La Champanera", "~100K", "#F5E6D3", "LC"),
        ("TELVA Novias", "76K", "#8B7E74", "TN"),
    ]

    cols = st.columns(4)
    for i, (name, followers, color, initials) in enumerate(competitors):
        with cols[i % 4]:
            is_evln = initials == "EVLN"
            border = "3px solid #D4AF37" if is_evln else "none"
            text_color = "#3D3D3D" if is_evln else "white"

            st.markdown(
                f'<div style="text-align:center;padding:8px;">'
                f'<div style="width:50px;height:50px;border-radius:50%;background:{color};border:{border};'
                f'display:inline-flex;align-items:center;justify-content:center;'
                f'color:{text_color};font-weight:600;font-size:0.7rem;">{initials}</div>'
                f'<p style="font-size:0.7rem;margin:4px 0 0 0;color:#3D3D3D;">{name}</p>'
                f'<p style="font-size:0.65rem;margin:0;color:#8B7E74;">{followers}</p>'
                f'</div>',
                unsafe_allow_html=True
            )


def render_opportunity_card(
    title: str,
    description: str,
    icon: str = "",
) -> None:
    """
    Render an opportunity card highlighting market gaps.

    Args:
        title: Opportunity title.
        description: Detailed description.
        icon: Emoji icon.
    """
    st.markdown(
        f'<div style="background:linear-gradient(135deg,#D4AF3710 0%,#F5E6D330 100%);border:1px solid #D4AF37;border-radius:12px;padding:20px;margin:8px 0;">'
        f'<p style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#3D3D3D;margin:0 0 8px 0;">{icon} {title}</p>'
        f'<p style="font-size:0.9rem;color:#8B7E74;line-height:1.5;margin:0;">{description}</p>'
        f'</div>',
        unsafe_allow_html=True
    )
