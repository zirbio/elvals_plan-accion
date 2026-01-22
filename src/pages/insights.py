"""
Insights page (Tab 5) - Content analysis of best vs worst performing posts.
Identifies success levers and actionable patterns.
"""

import streamlit as st
from pathlib import Path

from src.parsers.insights_parser import parse_insights_files
from src.components.insight_cards import (
    render_comparison_metric,
    render_comparison_metric_text,
    render_lever_card,
    render_do_dont_section,
    render_hashtag_clouds,
    render_posts_table,
    render_recommendation_card,
)


def render_insights(data_dir: Path) -> None:
    """
    Render the insights page.

    Args:
        data_dir: Path to the data directory containing Excel files.
    """
    # Parse insights data
    data = parse_insights_files(data_dir)

    best_posts = data.get("best_posts", {})
    worst_posts = data.get("worst_posts", {})
    comparison = data.get("comparison", {})
    levers = data.get("levers", [])

    # =========================================================================
    # HERO SECTION
    # =========================================================================
    st.markdown(
        '<div style="text-align:center;margin-bottom:32px;">'
        '<div style="font-size:2.5rem;margin-bottom:8px;"></div>'
        '<div style="font-family:Playfair Display,serif;font-size:1.75rem;font-weight:600;color:#3D3D3D;">Insights de Contenido</div>'
        '<div style="font-size:0.9rem;color:#8B7E74;margin-top:8px;">Analisis de los 10 mejores vs 10 peores posts de Instagram</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # =========================================================================
    # COMPARISON METRICS
    # =========================================================================
    st.markdown("### Metricas Comparativas")
    st.markdown(
        '<div style="font-size:0.875rem;color:#8B7E74;margin-bottom:16px;">'
        'Promedio de metricas entre los 10 mejores y 10 peores posts'
        '</div>',
        unsafe_allow_html=True
    )

    metrics = comparison.get("metrics", [])

    # Render metrics in a row
    cols = st.columns(5)
    for i, metric in enumerate(metrics[:5]):
        with cols[i]:
            if isinstance(metric.get("best"), str) or isinstance(metric.get("worst"), str):
                render_comparison_metric_text(
                    name=metric.get("name", ""),
                    best=str(metric.get("best", "")),
                    worst=str(metric.get("worst", "")),
                    ratio=metric.get("ratio", ""),
                    icon=metric.get("icon", ""),
                )
            else:
                render_comparison_metric(
                    name=metric.get("name", ""),
                    best=metric.get("best", 0),
                    worst=metric.get("worst", 0),
                    ratio=metric.get("ratio", ""),
                    icon=metric.get("icon", ""),
                )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================================
    # SUCCESS LEVERS
    # =========================================================================
    st.markdown("### Palancas de Exito")
    st.markdown(
        '<div style="font-size:0.875rem;color:#8B7E74;margin-bottom:16px;">'
        'Factores clave identificados que diferencian el contenido exitoso'
        '</div>',
        unsafe_allow_html=True
    )

    # Render levers in rows of 2-3
    lever_cols = st.columns(2)
    for i, lever in enumerate(levers[:4]):
        with lever_cols[i % 2]:
            render_lever_card(
                title=lever.get("title", ""),
                impact=lever.get("impact", "MEDIO"),
                insight=lever.get("insight", ""),
                action=lever.get("action", ""),
                icon=lever.get("icon", ""),
            )

    # Fifth lever in full width
    if len(levers) > 4:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            render_lever_card(
                title=levers[4].get("title", ""),
                impact=levers[4].get("impact", "MEDIO"),
                insight=levers[4].get("insight", ""),
                action=levers[4].get("action", ""),
                icon=levers[4].get("icon", ""),
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================================
    # DO vs DON'T
    # =========================================================================
    st.markdown("### Lo que Funciona vs Lo que NO")

    do_items = [
        "Contenido inspiracional sobre vestidos y novias",
        "Captions largos y poeticos (~480 caracteres)",
        "Etiquetar diseñadores, fotografos y profesionales",
        "Tono educativo sobre tejidos, detalles y elegancia",
        "Historias emotivas de novias reales",
        "Hashtags: #NoviasConEstilo, #EleganciaAtemporal",
    ]

    dont_items = [
        "Promocion directa de servicios (Asesoria Boutique)",
        "CTAs agresivos (Escribeme ASESORIA por DM)",
        "Sorteos (generan engagement falso)",
        "Captions cortos y promocionales",
        "Contenido explicativo de servicios",
        "Hashtags: #asesoriadebodas, #weddingplanning",
    ]

    render_do_dont_section(do_items, dont_items)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================================
    # HASHTAGS
    # =========================================================================
    st.markdown("### Hashtags Efectivos")

    good_hashtags = best_posts.get("top_hashtags", [
        ("NoviasConEstilo", 8),
        ("EleganciaAtemporal", 7),
        ("BodasConEncanto", 6),
        ("DetallesQueEnamoran", 5),
        ("NoviasVintage", 4),
        ("BridalInspiration", 4),
        ("noviasreales", 3),
        ("noviaelegante", 3),
    ])

    bad_hashtags = worst_posts.get("top_hashtags", [
        ("asesoriadebodas", 5),
        ("noviaespaña", 4),
        ("WeddingPlanning", 4),
        ("weddingplanneronline", 3),
        ("organizatuboda", 3),
        ("bodaplanificada", 2),
    ])

    render_hashtag_clouds(good_hashtags, bad_hashtags)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================================
    # POSTS TABLE (Expandable)
    # =========================================================================
    st.markdown("### Detalle de Publicaciones")

    with st.expander("Ver tabla comparativa de posts", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            render_posts_table(
                posts=best_posts.get("posts", []),
                title=" Top 10 Posts",
                is_best=True,
            )

        with col2:
            render_posts_table(
                posts=worst_posts.get("posts", []),
                title=" Bottom 10 Posts",
                is_best=False,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================================
    # RECOMMENDATIONS
    # =========================================================================
    st.markdown("### Recomendaciones Especificas")
    st.markdown(
        '<div style="font-size:0.875rem;color:#8B7E74;margin-bottom:16px;">'
        'Acciones concretas basadas en el analisis de datos'
        '</div>',
        unsafe_allow_html=True
    )

    rec_cols = st.columns(3)

    recommendations = [
        {
            "title": "Transforma tus CTAs",
            "description": "En lugar de 'Escribeme ASESORIA', cuenta una historia de como ayudaste a una novia. El CTA puede ser sutil al final.",
            "icon": "",
            "priority": 1,
        },
        {
            "title": "Siempre Colabora",
            "description": "Cada post debe etiquetar al menos 1 profesional (diseñador, fotografo, venue). Amplifica el alcance y da credibilidad.",
            "icon": "",
            "priority": 1,
        },
        {
            "title": "Formato Largo",
            "description": "Escribe captions de 400-500 caracteres minimo. Usa narrativa poetica: 'La magia esta en los detalles...'",
            "icon": "",
            "priority": 2,
        },
    ]

    for i, rec in enumerate(recommendations):
        with rec_cols[i]:
            render_recommendation_card(
                title=rec["title"],
                description=rec["description"],
                icon=rec["icon"],
                priority=rec["priority"],
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # Second row of recommendations
    rec_cols2 = st.columns(3)

    recommendations2 = [
        {
            "title": "Cero Sorteos",
            "description": "Los sorteos generan muchos comentarios pero 0 guardados y 0 seguidores nuevos. Es engagement vacio que daña el algoritmo.",
            "icon": "",
            "priority": 1,
        },
        {
            "title": "Contenido Universal",
            "description": "El 85% del alcance de posts exitosos viene de NO seguidores. Crea contenido que cualquier persona pueda compartir.",
            "icon": "",
            "priority": 2,
        },
        {
            "title": "Destaca los Detalles",
            "description": "Habla de tejidos, bordados, caidas, broches vintage. El contenido educativo sobre moda nupcial genera guardados.",
            "icon": "",
            "priority": 2,
        },
    ]

    for i, rec in enumerate(recommendations2):
        with rec_cols2[i]:
            render_recommendation_card(
                title=rec["title"],
                description=rec["description"],
                icon=rec["icon"],
                priority=rec["priority"],
            )

    # =========================================================================
    # SUMMARY CARD
    # =========================================================================
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div style="background:linear-gradient(135deg,#FDF2F8 0%,#F3E8FF 50%,#FEF3C7 100%);border-radius:16px;padding:32px;text-align:center;margin-top:24px;">'
        '<div style="font-family:Playfair Display,serif;font-size:1.5rem;font-weight:600;color:#3D3D3D;margin-bottom:16px;">Formula del Exito</div>'
        '<div style="font-size:1rem;color:#8B7E74;line-height:1.8;max-width:600px;margin:0 auto;">'
        '<span style="font-weight:600;color:#FF6B9D;">Inspiracion</span> + '
        '<span style="font-weight:600;color:#C084FC;">Colaboraciones</span> + '
        '<span style="font-weight:600;color:#D4AF37;">Narrativa</span><br>'
        '= Posts que convierten seguidores y generan impacto real'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
