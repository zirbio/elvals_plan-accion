"""
Strategy page (Tab 3) - Plan overview with KPIs and business models.
"""

import streamlit as st
from pathlib import Path

from src.components.metric_cards import render_metric_grid, render_kpi_comparison
from src.components.timeline import render_phase_cards
from src.parsers.plan_parser import parse_plan_file


def render_strategy(docs_dir: Path) -> None:
    """
    Render the strategy page.

    Args:
        docs_dir: Path to the documents directory.
    """
    # Parse plan file
    plan_path = docs_dir / "2026-01-17-el-vals-de-la-novia-plan.md"
    plan_data = parse_plan_file(plan_path)

    phases = plan_data.get("phases", [])
    business_models = plan_data.get("business_models", [])
    projections = plan_data.get("projections", [])

    # =========================================================================
    # PHASE OVERVIEW
    # =========================================================================
    st.markdown("### Fases Estrategicas")

    phase_cards = [
        {
            "name": "Fase A: Rehabilitacion",
            "description": "Subir engagement de 0.24% a 1.5%+ mediante transicion a Reels y engagement activo",
            "duration": "Meses 1-3",
            "status": "active",
        },
        {
            "name": "Fase B: Monetizacion",
            "description": "Implementar 3 modelos de negocio combinados para generar ingresos recurrentes",
            "duration": "Meses 4-12",
            "status": "pending",
        },
    ]

    render_phase_cards(phase_cards, current_phase=0)

    # =========================================================================
    # KPI DASHBOARD
    # =========================================================================
    st.markdown("### KPIs Objetivo")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Fase A - Rehabilitacion (Mes 3)**")
        render_kpi_comparison("Engagement Rate", 0.24, 1.5, "%")
        render_kpi_comparison("Avg. Likes", 269, 1000, "")
        render_kpi_comparison("Avg. Comments", 7, 40, "")
        render_kpi_comparison("Seguidores", 114900, 120000, "")

    with col2:
        st.markdown("**Fase B - Monetizacion (Mes 12)**")
        render_kpi_comparison("Lista Email", 0, 500, "")
        render_kpi_comparison("Proveedores B2B", 0, 30, "")
        render_kpi_comparison("Ingresos/Mes", 0, 10500, "")
        render_kpi_comparison("Patrocinios Activos", 0, 10, "")

    # =========================================================================
    # BUSINESS MODELS
    # =========================================================================
    st.markdown("### Modelos de Negocio")

    cols = st.columns(3)

    models_data = [
        {
            "name": "Afiliados + Patrocinios",
            "icon": "",
            "potential": "1,500-4,000/mes",
            "effort": 4,
            "start": "Mes 4",
            "description": "Comisiones de Etsy, ASOS, Booking + posts patrocinados con marcas de bodas",
        },
        {
            "name": "Productos Digitales",
            "icon": "",
            "potential": "1,000-5,000/mes",
            "effort": 5,
            "start": "Mes 6",
            "description": "Guias, checklists, templates de Canva para novias",
        },
        {
            "name": "Directorio B2B",
            "icon": "",
            "potential": "2,000-6,000/mes",
            "effort": 4,
            "start": "Mes 8",
            "description": "Suscripciones de fotografos, floristas, venues y otros proveedores",
        },
    ]

    for col, model in zip(cols, models_data):
        with col:
            # Effort stars
            stars = "" * model["effort"] + "" * (5 - model["effort"])

            st.markdown(
                f'<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;height:100%;">'
                f'<div style="font-size:2rem;margin-bottom:12px;">{model["icon"]}</div>'
                f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#3D3D3D;margin-bottom:8px;">{model["name"]}</div>'
                f'<div style="font-size:0.875rem;color:#8B7E74;margin-bottom:16px;line-height:1.5;">{model["description"]}</div>'
                f'<div style="display:flex;justify-content:space-between;align-items:center;padding-top:12px;border-top:1px solid #F0E6E8;">'
                f'<div>'
                f'<div style="font-size:0.75rem;color:#8B7E74;">Potencial</div>'
                f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#FF6B9D;">{model["potential"]}</div>'
                f'</div>'
                f'<div style="text-align:right;">'
                f'<div style="font-size:0.75rem;color:#8B7E74;">Inicio</div>'
                f'<div style="font-weight:500;color:#3D3D3D;">{model["start"]}</div>'
                f'</div>'
                f'</div>'
                f'<div style="margin-top:12px;font-size:0.875rem;">'
                f'<span style="color:#8B7E74;">Ratio tiempo/beneficio:</span>'
                f'<span style="color:#D4AF37;">{stars}</span>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    # =========================================================================
    # FINANCIAL PROJECTION
    # =========================================================================
    st.markdown("### Proyeccion Financiera")

    # Create projection table
    st.markdown(
        '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;overflow-x:auto;">'
        '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;">'
        '<thead>'
        '<tr style="border-bottom:2px solid #F0E6E8;">'
        '<th style="text-align:left;padding:12px 8px;color:#8B7E74;">Mes</th>'
        '<th style="text-align:right;padding:12px 8px;color:#8B7E74;">Afiliados</th>'
        '<th style="text-align:right;padding:12px 8px;color:#8B7E74;">Productos</th>'
        '<th style="text-align:right;padding:12px 8px;color:#8B7E74;">B2B</th>'
        '<th style="text-align:right;padding:12px 8px;color:#3D3D3D;font-weight:600;">Total</th>'
        '</tr>'
        '</thead>'
        '<tbody>',
        unsafe_allow_html=True
    )

    projection_rows = [
        ("1-3", "-", "-", "-", "0"),
        ("4", "500", "-", "-", "500"),
        ("5", "1,500", "-", "-", "1,500"),
        ("6", "1,500", "800", "-", "2,300"),
        ("7", "1,800", "1,500", "-", "3,300"),
        ("8", "2,000", "1,800", "1,000", "4,800"),
        ("9", "2,000", "2,000", "2,000", "6,000"),
        ("10", "2,200", "2,200", "3,000", "7,400"),
        ("11", "2,200", "2,500", "4,000", "8,700"),
        ("12", "2,500", "3,000", "5,000", "10,500"),
    ]

    for i, (month, aff, prod, b2b, total) in enumerate(projection_rows):
        bg = "#FFFBF7" if i % 2 == 0 else "white"
        total_color = "#FF6B9D" if total != "0" else "#8B7E74"

        st.markdown(
            f'<tr style="background:{bg};border-bottom:1px solid #F0E6E8;">'
            f'<td style="padding:10px 8px;font-weight:500;">Mes {month}</td>'
            f'<td style="padding:10px 8px;text-align:right;color:#8B7E74;">{aff}</td>'
            f'<td style="padding:10px 8px;text-align:right;color:#8B7E74;">{prod}</td>'
            f'<td style="padding:10px 8px;text-align:right;color:#8B7E74;">{b2b}</td>'
            f'<td style="padding:10px 8px;text-align:right;font-weight:600;color:{total_color};">{total}</td>'
            f'</tr>',
            unsafe_allow_html=True
        )

    st.markdown('</tbody></table></div>', unsafe_allow_html=True)

    # Summary row
    st.markdown(
        '<div style="display:flex;justify-content:space-around;margin-top:24px;flex-wrap:wrap;gap:16px;">'
        '<div style="text-align:center;">'
        '<div style="font-size:0.875rem;color:#8B7E74;">Total Ano 1</div>'
        '<div style="font-family:Playfair Display,serif;font-size:1.5rem;font-weight:600;color:#FF6B9D;">~45,000-50,000</div>'
        '</div>'
        '<div style="text-align:center;">'
        '<div style="font-size:0.875rem;color:#8B7E74;">Mes 12 Estabilizado</div>'
        '<div style="font-family:Playfair Display,serif;font-size:1.5rem;font-weight:600;color:#C084FC;">10,500/mes</div>'
        '</div>'
        '<div style="text-align:center;">'
        '<div style="font-size:0.875rem;color:#8B7E74;">Proyeccion Ano 2</div>'
        '<div style="font-family:Playfair Display,serif;font-size:1.5rem;font-weight:600;color:#D4AF37;">~96,000-144,000</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # =========================================================================
    # TIME DISTRIBUTION
    # =========================================================================
    st.markdown("### Distribucion de Tiempo")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:600;color:#3D3D3D;margin-bottom:16px;">Por Fase</div>'
            '<div style="margin-bottom:12px;">'
            '<div style="display:flex;justify-content:space-between;margin-bottom:4px;">'
            '<span style="font-size:0.875rem;">Rehabilitacion (Meses 1-3)</span>'
            '<span style="font-weight:600;">6-8h/semana</span>'
            '</div>'
            '</div>'
            '<div style="margin-bottom:12px;">'
            '<div style="display:flex;justify-content:space-between;margin-bottom:4px;">'
            '<span style="font-size:0.875rem;">Monetizacion (Meses 4-7)</span>'
            '<span style="font-weight:600;">8-10h/semana</span>'
            '</div>'
            '</div>'
            '<div>'
            '<div style="display:flex;justify-content:space-between;margin-bottom:4px;">'
            '<span style="font-size:0.875rem;">Estabilizado (Mes 8+)</span>'
            '<span style="font-weight:600;">8-11h/semana</span>'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;">'
            '<div style="font-family:Playfair Display,serif;font-size:1rem;font-weight:600;color:#3D3D3D;margin-bottom:16px;">Semanal (Estabilizado)</div>'
            '<div style="font-size:0.875rem;line-height:2;">'
            '<div style="display:flex;justify-content:space-between;"><span>Creacion contenido</span><span style="font-weight:500;">4-5h</span></div>'
            '<div style="display:flex;justify-content:space-between;"><span>Engagement y comunidad</span><span style="font-weight:500;">1-2h</span></div>'
            '<div style="display:flex;justify-content:space-between;"><span>Afiliados/patrocinios</span><span style="font-weight:500;">1h</span></div>'
            '<div style="display:flex;justify-content:space-between;"><span>Productos digitales</span><span style="font-weight:500;">1h</span></div>'
            '<div style="display:flex;justify-content:space-between;"><span>Directorio B2B</span><span style="font-weight:500;">1-2h</span></div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
