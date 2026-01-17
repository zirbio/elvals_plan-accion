"""
Competitors page (Tab 4) - Market analysis and positioning.
"""

import streamlit as st
from pathlib import Path

from src.components.competitor_card import (
    render_competitor_card,
    render_positioning_map,
    render_opportunity_card,
)
from src.parsers.competitor_parser import (
    parse_competitor_file,
    get_default_competitors,
    get_default_opportunities,
)


def render_competitors(docs_dir: Path) -> None:
    """
    Render the competitors analysis page.

    Args:
        docs_dir: Path to the documents directory.
    """
    # Parse competitor file
    competitor_path = docs_dir / "2026-01-17-analisis-competidores.md"
    comp_data = parse_competitor_file(competitor_path)

    competitors = comp_data.get("competitors", get_default_competitors())
    opportunities = comp_data.get("opportunities", get_default_opportunities())

    # =========================================================================
    # POSITIONING MAP
    # =========================================================================
    st.markdown("### Mapa de Posicionamiento")

    render_positioning_map()

    # =========================================================================
    # COMPETITOR CARDS
    # =========================================================================
    st.markdown("### Analisis de Competidores")

    # Priority competitors (direct)
    st.markdown("**Competidores Directos (Prioridad)**")

    priority_competitors = [c for c in competitors if c.get("priority")]
    priority_competitors.sort(key=lambda x: int(x.get("priority", "99")))

    if priority_competitors:
        cols = st.columns(min(3, len(priority_competitors)))
        for col, comp in zip(cols, priority_competitors[:3]):
            with col:
                render_competitor_card(
                    name=comp.get("name", ""),
                    handle=comp.get("handle", ""),
                    followers=comp.get("followers", "0"),
                    model=comp.get("model", ""),
                    avatar_initials=comp.get("avatar_initials"),
                    differentiator=comp.get("differentiator"),
                    priority=comp.get("priority"),
                )

    # Other competitors
    st.markdown("**Competidores Aspiracionales y Corporativos**")

    other_competitors = [c for c in competitors if not c.get("priority")]

    if other_competitors:
        cols = st.columns(min(4, len(other_competitors)))
        for col, comp in zip(cols, other_competitors[:4]):
            with col:
                render_competitor_card(
                    name=comp.get("name", ""),
                    handle=comp.get("handle", ""),
                    followers=comp.get("followers", "0"),
                    model=comp.get("model", ""),
                    avatar_initials=comp.get("avatar_initials"),
                    differentiator=comp.get("differentiator"),
                )

    # =========================================================================
    # COMPARISON TABLE
    # =========================================================================
    st.markdown("### Comparativa de Modelos")

    st.markdown(
        '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;overflow-x:auto;">'
        '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;">'
        '<thead>'
        '<tr style="border-bottom:2px solid #F0E6E8;">'
        '<th style="text-align:left;padding:12px 8px;color:#8B7E74;">Cuenta</th>'
        '<th style="text-align:right;padding:12px 8px;color:#8B7E74;">Seguidores</th>'
        '<th style="text-align:left;padding:12px 8px;color:#8B7E74;">Modelo</th>'
        '<th style="text-align:left;padding:12px 8px;color:#8B7E74;">Diferenciador</th>'
        '</tr>'
        '</thead>'
        '<tbody>',
        unsafe_allow_html=True
    )

    table_data = [
        ("Invitada Perfecta", "~500K", "Contenido + Blog + Afiliados", "Foco en invitadas", False),
        ("Bodas.net", "303K", "Directorio B2B", "Corporativo + Sorteos", False),
        ("Bridalada", "292K", "Marca de moda propia", "Personal + Accesible", False),
        ("Miss Cavallier", "281K", "Alquiler vestidos", "Wedding planner real", False),
        ("El Vals de la Novia", "115K", "Por definir", "Inspiracion visual", True),
        ("Una Boda Original", "~115K", "Inspiracion", "Galeria de calidad", False),
        ("La Champanera", "~100K", "Agencia comunicacion", "Anti-topicos", False),
        ("TELVA Novias", "76K", "Medio tradicional", "Editorial/Tendencias", False),
    ]

    for i, (name, followers, model, diff, highlight) in enumerate(table_data):
        bg = "#FDF4FF" if highlight else ("#FFFBF7" if i % 2 == 0 else "white")
        name_style = "font-weight: 600; color: #FF6B9D;" if highlight else ""
        border = "2px solid #C084FC" if highlight else "1px solid #F0E6E8"

        st.markdown(
            f'<tr style="background:{bg};border-bottom:{border};">'
            f'<td style="padding:10px 8px;{name_style}">{name}</td>'
            f'<td style="padding:10px 8px;text-align:right;">{followers}</td>'
            f'<td style="padding:10px 8px;color:#8B7E74;">{model}</td>'
            f'<td style="padding:10px 8px;color:#8B7E74;font-style:italic;">{diff}</td>'
            f'</tr>',
            unsafe_allow_html=True
        )

    st.markdown('</tbody></table></div>', unsafe_allow_html=True)

    # =========================================================================
    # OPPORTUNITIES
    # =========================================================================
    st.markdown("### Oportunidades de Mercado")

    opportunity_data = [
        {
            "title": "Reels/Video Corto",
            "description": "La mayoria de competidores sigue siendo muy estatica. Oportunidad de ser first mover en formato video.",
            "icon": "",
        },
        {
            "title": "Productos Digitales",
            "description": "Ningun competidor tiene cursos o guias claros. Territorio completamente libre para capturar.",
            "icon": "",
        },
        {
            "title": "Comunidad/Membresia",
            "description": "No hay clubes de novias ni comunidades activas. Oportunidad de crear engagement real y recurrente.",
            "icon": "",
        },
        {
            "title": "Educacion Estructurada",
            "description": "Solo hay tips sueltos pero no formacion. Espacio para contenido educativo de valor.",
            "icon": "",
        },
    ]

    cols = st.columns(2)
    for i, opp in enumerate(opportunity_data):
        with cols[i % 2]:
            render_opportunity_card(
                title=opp["title"],
                description=opp["description"],
                icon=opp["icon"],
            )

    # =========================================================================
    # RECOMMENDATIONS
    # =========================================================================
    st.markdown("### Recomendaciones Estrategicas")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:Playfair Display,serif;font-size:1rem;font-weight:600;margin-bottom:12px;">Corto Plazo (Meses 1-3)</div>'
            '<ul style="font-size:0.875rem;color:#3D3D3D;padding-left:20px;line-height:1.8;">'
            '<li>Pivotar a Reels antes que competidores</li>'
            '<li>Aumentar contenido educativo/tips</li>'
            '<li>Estudiar que posts funcionan a Una Boda Original</li>'
            '<li>Empezar relaciones con proveedores</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:Playfair Display,serif;font-size:1rem;font-weight:600;margin-bottom:12px;">Medio Plazo (Meses 4-8)</div>'
            '<ul style="font-size:0.875rem;color:#3D3D3D;padding-left:20px;line-height:1.8;">'
            '<li>Lanzar primer producto digital</li>'
            '<li>Crear directorio de proveedores diferenciado</li>'
            '<li>Considerar web/blog para SEO</li>'
            '<li>Explorar colaboraciones estrategicas</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:Playfair Display,serif;font-size:1rem;font-weight:600;margin-bottom:12px;">Largo Plazo (Meses 9-12+)</div>'
            '<ul style="font-size:0.875rem;color:#3D3D3D;padding-left:20px;line-height:1.8;">'
            '<li>Evaluar modelo de agencia (como La Champanera)</li>'
            '<li>Considerar marca propia si hay demanda</li>'
            '<li>Expandir a otros mercados hispanohablantes</li>'
            '<li>Crear comunidad/membresia de novias</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

    # =========================================================================
    # POSITIONING STATEMENT
    # =========================================================================
    st.markdown("### Posicionamiento Propuesto")

    st.markdown(
        '<div style="background:linear-gradient(135deg,#FF6B9D15 0%,#C084FC15 100%);border:2px solid #C084FC;border-radius:16px;padding:32px;text-align:center;margin-top:16px;">'
        '<div style="font-family:Playfair Display,serif;font-size:1.5rem;font-weight:600;color:#3D3D3D;margin-bottom:16px;">"El Vals de la Novia: Tu guia personal para una boda con estilo"</div>'
        '<div style="display:flex;justify-content:center;gap:24px;flex-wrap:wrap;margin-top:20px;">'
        '<div style="background:white;padding:8px 16px;border-radius:9999px;font-size:0.875rem;color:#FF6B9D;font-weight:500;">Personal (vs corporativos)</div>'
        '<div style="background:white;padding:8px 16px;border-radius:9999px;font-size:0.875rem;color:#C084FC;font-weight:500;">Educativo (vs solo inspiracion)</div>'
        '<div style="background:white;padding:8px 16px;border-radius:9999px;font-size:0.875rem;color:#D4AF37;font-weight:500;">Video-first (vs estatico)</div>'
        '<div style="background:white;padding:8px 16px;border-radius:9999px;font-size:0.875rem;color:#8B7E74;font-weight:500;">Proveedores curados</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
