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

    # =========================================================================
    # STRATEGIC PAPER
    # =========================================================================
    render_strategy_paper()


def render_strategy_paper() -> None:
    """Render the strategic paper content from the plan document."""
    st.markdown("---")
    st.markdown(
        '<div style="text-align:center;margin:32px 0;">'
        '<div style="font-family:Playfair Display,serif;font-size:1.75rem;font-weight:600;color:#3D3D3D;">Paper Estrategico</div>'
        '<div style="font-size:0.875rem;color:#8B7E74;margin-top:8px;font-style:italic;">Documento completo de estrategia y metodologia</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # =========================================================================
    # SECTION 1: SITUACION ACTUAL Y DIAGNOSTICO
    # =========================================================================
    with st.expander("1. Situacion Actual y Diagnostico", expanded=False):
        st.markdown("#### KPIs de la cuenta (Enero 2026)")

        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Metrica</th>'
            '<th style="text-align:center;padding:10px;">Valor</th>'
            '<th style="text-align:center;padding:10px;">Benchmark</th>'
            '<th style="text-align:center;padding:10px;">Estado</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Seguidores</td><td style="text-align:center;">114,900</td><td style="text-align:center;">-</td><td style="text-align:center;">✅ Buena base</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Engagement Rate</td><td style="text-align:center;">0.24%</td><td style="text-align:center;">1.5-2.5%</td><td style="text-align:center;color:#DC2626;">🔴 Critico</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Avg. Likes</td><td style="text-align:center;">269</td><td style="text-align:center;">~1,150 esperados</td><td style="text-align:center;color:#DC2626;">🔴 76% por debajo</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Avg. Comments</td><td style="text-align:center;">7</td><td style="text-align:center;">~29 esperados</td><td style="text-align:center;color:#DC2626;">🔴 76% por debajo</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Crecimiento 30d</td><td style="text-align:center;">0.00%</td><td style="text-align:center;">0.5-2%</td><td style="text-align:center;color:#DC2626;">🔴 Estancado</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Total Posts</td><td style="text-align:center;">2,333</td><td style="text-align:center;">-</td><td style="text-align:center;">✅ Historial solido</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Ratio Likes/Comments</td><td style="text-align:center;">38.43</td><td style="text-align:center;">&lt;50</td><td style="text-align:center;">✅ Organico</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Follower/Following</td><td style="text-align:center;">65.71</td><td style="text-align:center;">&gt;50</td><td style="text-align:center;">✅ Saludable</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("#### Diagnostico")

        st.markdown(
            '<div style="background:#FEF2F2;border-left:4px solid #DC2626;padding:16px;margin:16px 0;border-radius:0 8px 8px 0;">'
            '<div style="font-weight:600;color:#991B1B;margin-bottom:8px;">Problema principal: El engagement de 0.24% es extremadamente bajo porque:</div>'
            '<ol style="margin:0;padding-left:20px;color:#7F1D1D;">'
            '<li><strong>Formato de contenido</strong>: Principalmente imagenes estaticas, penalizadas por el algoritmo 2025-2026</li>'
            '<li><strong>Algoritmo de Instagram</strong>: Favorece Reels (75% mas engagement que imagenes)</li>'
            '<li><strong>Audiencia dormida</strong>: No por ser falsa, sino porque el algoritmo no les muestra el contenido</li>'
            '</ol>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div style="background:#F0FDF4;border-left:4px solid #16A34A;padding:16px;margin:16px 0;border-radius:0 8px 8px 0;">'
            '<div style="font-weight:600;color:#166534;margin-bottom:8px;">Buenas noticias:</div>'
            '<ul style="margin:0;padding-left:20px;color:#14532D;">'
            '<li>La audiencia es real (crecimiento organico gradual)</li>'
            '<li>Habilidades avanzadas en edicion de Reels</li>'
            '<li>5-10 horas/semana disponibles</li>'
            '<li>Contenido de calidad (inspiracion + proveedores)</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("#### Categorias de contenido identificadas")
        st.markdown("Wedding • Formal Wear • Shopping & Fashion • Luxury Fashion • Jewelry • Lingerie & Intimates")

    # =========================================================================
    # SECTION 2: ESTRATEGIA GENERAL
    # =========================================================================
    with st.expander("2. Estrategia General", expanded=False):
        st.markdown("#### Enfoque en dos fases")

        st.markdown(
            '<div style="display:flex;gap:24px;flex-wrap:wrap;margin:24px 0;">'
            '<div style="flex:1;min-width:200px;background:linear-gradient(135deg,#FDF2F8 0%,#FCE7F3 100%);border-radius:16px;padding:24px;text-align:center;">'
            '<div style="font-size:2rem;margin-bottom:8px;">🔧</div>'
            '<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#BE185D;">FASE A: REHABILITACION</div>'
            '<div style="font-size:0.875rem;color:#9D174D;margin-top:8px;">Meses 1-3</div>'
            '<div style="margin-top:16px;font-size:0.875rem;color:#831843;">Subir engagement de 0.24% a 1.5%+</div>'
            '</div>'
            '<div style="display:flex;align-items:center;font-size:2rem;color:#D4AF37;">→</div>'
            '<div style="flex:1;min-width:200px;background:linear-gradient(135deg,#FEF3C7 0%,#FDE68A 100%);border-radius:16px;padding:24px;text-align:center;">'
            '<div style="font-size:2rem;margin-bottom:8px;">💰</div>'
            '<div style="font-family:Playfair Display,serif;font-size:1.125rem;font-weight:600;color:#B45309;">FASE B: MONETIZACION</div>'
            '<div style="font-size:0.875rem;color:#92400E;margin-top:8px;">Meses 4-12</div>'
            '<div style="margin-top:16px;font-size:0.875rem;color:#78350F;">Implementar 3 modelos de negocio combinados</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("#### Modelos de negocio seleccionados")

        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">#</th>'
            '<th style="text-align:left;padding:10px;">Modelo</th>'
            '<th style="text-align:center;padding:10px;">Ingreso potencial</th>'
            '<th style="text-align:center;padding:10px;">Ratio tiempo/beneficio</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;">1</td><td style="padding:10px;font-weight:500;">Productos digitales</td><td style="text-align:center;color:#FF6B9D;">€1,000-5,000/mes</td><td style="text-align:center;color:#D4AF37;">⭐⭐⭐⭐⭐</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;">2</td><td style="padding:10px;font-weight:500;">Afiliados + Patrocinios</td><td style="text-align:center;color:#FF6B9D;">€1,500-4,000/mes</td><td style="text-align:center;color:#D4AF37;">⭐⭐⭐⭐</td></tr>'
            '<tr><td style="padding:10px;">3</td><td style="padding:10px;font-weight:500;">Directorio proveedores B2B</td><td style="text-align:center;color:#FF6B9D;">€2,000-6,000/mes</td><td style="text-align:center;color:#D4AF37;">⭐⭐⭐⭐</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("#### Modelos descartados")
        st.markdown(
            '<div style="background:#FEF3C7;border-radius:8px;padding:16px;margin:16px 0;">'
            '<ul style="margin:0;padding-left:20px;color:#92400E;">'
            '<li><strong>Wedding Planner tradicional</strong>: no escala, muy intensivo en tiempo</li>'
            '<li><strong>Agencia de comunicacion</strong>: requiere equipo, gestion clientes</li>'
            '<li><strong>Media/revista pura</strong>: modelo fragil, depende 100% de ads</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

    # =========================================================================
    # SECTION 3: FASE A - REHABILITACION
    # =========================================================================
    with st.expander("3. Fase A: Plan de Rehabilitacion (Meses 1-3)", expanded=False):
        st.markdown("#### Fase 1: Transicion a Reels (Semanas 1-2)")
        st.markdown("**Objetivo**: Despertar la audiencia dormida")

        st.markdown("##### Semana 1: Reset y primeros Reels")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Dia</th>'
            '<th style="text-align:left;padding:10px;">Accion</th>'
            '<th style="text-align:center;padding:10px;">Tiempo</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;">1-2</td><td style="padding:10px;">Auditoria: revisar ultimos 20 posts, identificar mejor engagement</td><td style="text-align:center;">1h</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;">3</td><td style="padding:10px;">Publicar Reel #1: contenido de alto valor emocional</td><td style="text-align:center;">1.5h</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;">4-5</td><td style="padding:10px;">Stories diarias con encuestas/preguntas</td><td style="text-align:center;">30min/dia</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;">6</td><td style="padding:10px;">Publicar Reel #2: tendencia adaptada al nicho nupcial</td><td style="text-align:center;">1.5h</td></tr>'
            '<tr><td style="padding:10px;">7</td><td style="padding:10px;">Responder TODOS los comentarios + engagement en cuentas similares</td><td style="text-align:center;">1h</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("##### Tipos de Reels recomendados")
        st.markdown(
            '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:16px 0;">'
            '<div style="background:#FDF2F8;padding:12px;border-radius:8px;font-size:0.875rem;">"POV: el dia de tu boda" con musica emotiva</div>'
            '<div style="background:#FDF2F8;padding:12px;border-radius:8px;font-size:0.875rem;">Transformaciones vestido/look de novia</div>'
            '<div style="background:#FDF2F8;padding:12px;border-radius:8px;font-size:0.875rem;">"3 cosas que nadie te cuenta sobre..." (educativo)</div>'
            '<div style="background:#FDF2F8;padding:12px;border-radius:8px;font-size:0.875rem;">Compilaciones de momentos bonitos de bodas reales</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.markdown("#### Fase 2: Optimizacion y Engagement (Semanas 3-6)")
        st.markdown("**Objetivo**: Optimizar lo que funciona + crear comunidad activa")

        st.markdown("##### Ritmo de publicacion")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Tipo</th>'
            '<th style="text-align:center;padding:10px;">Frecuencia</th>'
            '<th style="text-align:center;padding:10px;">Tiempo semanal</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Reels</td><td style="text-align:center;">3-4/semana</td><td style="text-align:center;">4-5h</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Stories</td><td style="text-align:center;">Diarias (2-3/dia)</td><td style="text-align:center;">30min/dia</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Engagement activo</td><td style="text-align:center;">Diario</td><td style="text-align:center;">20min/dia</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("##### Tacticas de engagement activo")
        st.markdown(
            '<div style="background:#F0FDF4;border-radius:8px;padding:16px;margin:16px 0;">'
            '<ol style="margin:0;padding-left:20px;color:#166534;">'
            '<li><strong>"Primera hora dorada"</strong>: Los primeros 60 min despues de publicar, responder cada comentario con preguntas</li>'
            '<li><strong>Engagement reciproco</strong>: 15-20 min diarios comentando en cuentas de novias, wedding planners, fotografos</li>'
            '<li><strong>Stories interactivas</strong>: Minimo 1 encuesta o pregunta al dia</li>'
            '<li><strong>DMs</strong>: Responder mensajes y agradecer cuando compartan contenido</li>'
            '</ol>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.markdown("#### Fase 3: Consolidacion (Semanas 7-12)")
        st.markdown("**Objetivo**: Consolidar engagement + preparar monetizacion")

        st.markdown("##### Nuevas tacticas")
        st.markdown("""
**1. Colaboraciones estrategicas (sin cobrar aun)**
- Contactar 3-5 proveedores de bodas (fotografos, floristas, venues)
- Proponer: "Te presento en mi cuenta a cambio de contenido exclusivo"
- Objetivo: generar relaciones B2B + contenido de calidad

**2. Contenido "teaser" de valor premium**
- Stories destacadas organizadas por temas
- Un Reel mensual tipo "guia completa"
- Encuestas: "¿Os gustaria una guia descargable de X?"

**3. Construccion de lista de email**
- Crear Lead Magnet simple (ej: "Checklist de boda" PDF)
- Link en bio a landing page
- Objetivo: 500-1000 emails en 6 semanas
""")

        st.markdown("##### KPIs Fase A (semana 12)")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Metrica</th>'
            '<th style="text-align:center;padding:10px;">Inicio</th>'
            '<th style="text-align:center;padding:10px;">Objetivo</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Engagement rate</td><td style="text-align:center;">0.24%</td><td style="text-align:center;color:#16A34A;font-weight:600;">&gt;1.5%</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Avg. likes</td><td style="text-align:center;">269</td><td style="text-align:center;color:#16A34A;font-weight:600;">&gt;1,000</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Avg. comments</td><td style="text-align:center;">7</td><td style="text-align:center;color:#16A34A;font-weight:600;">&gt;40</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Seguidores</td><td style="text-align:center;">114,900</td><td style="text-align:center;color:#16A34A;font-weight:600;">&gt;120,000</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Lista email</td><td style="text-align:center;">0</td><td style="text-align:center;color:#16A34A;font-weight:600;">&gt;500</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Relaciones con proveedores</td><td style="text-align:center;">0</td><td style="text-align:center;color:#16A34A;font-weight:600;">5-10</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

    # =========================================================================
    # SECTION 4: FASE B - MONETIZACION
    # =========================================================================
    with st.expander("4. Fase B: Plan de Monetizacion (Meses 4-12)", expanded=False):
        st.markdown("#### Secuencia de implementacion")

        st.markdown(
            '<div style="display:flex;gap:16px;flex-wrap:wrap;margin:24px 0;align-items:center;justify-content:center;">'
            '<div style="background:linear-gradient(135deg,#DBEAFE 0%,#BFDBFE 100%);border-radius:12px;padding:20px;text-align:center;min-width:150px;">'
            '<div style="font-size:0.75rem;color:#1E40AF;margin-bottom:4px;">MES 4-5</div>'
            '<div style="font-weight:600;color:#1E3A8A;">AFILIADOS + PATROCINIOS</div>'
            '<div style="font-size:0.75rem;color:#3B82F6;margin-top:8px;">Rapido</div>'
            '</div>'
            '<div style="font-size:1.5rem;color:#D4AF37;">→</div>'
            '<div style="background:linear-gradient(135deg,#F3E8FF 0%,#E9D5FF 100%);border-radius:12px;padding:20px;text-align:center;min-width:150px;">'
            '<div style="font-size:0.75rem;color:#6B21A8;margin-bottom:4px;">MES 6-7</div>'
            '<div style="font-weight:600;color:#581C87;">PRODUCTOS DIGITALES</div>'
            '<div style="font-size:0.75rem;color:#9333EA;margin-top:8px;">Escala</div>'
            '</div>'
            '<div style="font-size:1.5rem;color:#D4AF37;">→</div>'
            '<div style="background:linear-gradient(135deg,#FEF3C7 0%,#FDE68A 100%);border-radius:12px;padding:20px;text-align:center;min-width:150px;">'
            '<div style="font-size:0.75rem;color:#B45309;margin-bottom:4px;">MES 8-12</div>'
            '<div style="font-weight:600;color:#78350F;">DIRECTORIO B2B</div>'
            '<div style="font-size:0.75rem;color:#D97706;margin-top:8px;">Recurrente</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.markdown("#### Mes 4-5: Afiliados + Primeros Patrocinios")
        st.markdown("**Por que primero**: Requiere minimo esfuerzo y genera ingresos inmediatos.")

        st.markdown("##### Programas de afiliados recomendados")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Programa</th>'
            '<th style="text-align:center;padding:10px;">Comision</th>'
            '<th style="text-align:left;padding:10px;">Relevancia</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Etsy</td><td style="text-align:center;">4%</td><td style="padding:10px;">Decoracion, invitaciones</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">ASOS/Zalando</td><td style="text-align:center;">5-8%</td><td style="padding:10px;">Looks invitadas</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Booking/Airbnb</td><td style="text-align:center;">3-4%</td><td style="padding:10px;">Lunas de miel</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Amazon</td><td style="text-align:center;">3-10%</td><td style="padding:10px;">Listas de boda, accesorios</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Proveedores locales</td><td style="text-align:center;">10-20%</td><td style="padding:10px;">Negociar directamente</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("##### Tarifas de patrocinio estimadas (con engagement 1.5%+)")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Formato</th>'
            '<th style="text-align:center;padding:10px;">Precio</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Post/Reel patrocinado</td><td style="text-align:center;color:#FF6B9D;font-weight:600;">€500-1,500</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Story patrocinada</td><td style="text-align:center;color:#FF6B9D;font-weight:600;">€150-400</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Pack (Reel + Stories)</td><td style="text-align:center;color:#FF6B9D;font-weight:600;">€700-2,000</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("**Ingreso esperado mes 5**: €1,000-2,500")

        st.markdown("---")
        st.markdown("#### Mes 6-7: Primer Producto Digital")
        st.markdown("**Por que segundo**: Ya sabras que interesa a la audiencia por datos de afiliados.")

        st.markdown("##### Productos recomendados")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Producto</th>'
            '<th style="text-align:center;padding:10px;">Precio</th>'
            '<th style="text-align:center;padding:10px;">Esfuerzo crear</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Guia "Planifica tu boda paso a paso"</td><td style="text-align:center;color:#FF6B9D;">€29-39</td><td style="text-align:center;">20-30h</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Pack templates Canva para bodas</td><td style="text-align:center;color:#FF6B9D;">€15-29</td><td style="text-align:center;">15-20h</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Checklist interactivo de boda</td><td style="text-align:center;color:#FF6B9D;">€9-15</td><td style="text-align:center;">10h</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("**Ingreso esperado mes 7**: €1,500-3,500 (afiliados + producto)")

        st.markdown("---")
        st.markdown("#### Mes 8-12: Directorio de Proveedores B2B")
        st.markdown("**Por que tercero**: Ya tendras autoridad demostrada e ingresos estables.")

        st.markdown("##### Estructura de precios")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Tier</th>'
            '<th style="text-align:center;padding:10px;">Precio/mes</th>'
            '<th style="text-align:left;padding:10px;">Incluye</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Basico</td><td style="text-align:center;color:#FF6B9D;">€50-100</td><td style="padding:10px;">Mencion en Stories 1x/mes + directorio web</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Premium</td><td style="text-align:center;color:#FF6B9D;">€150-300</td><td style="padding:10px;">Reel dedicado + Stories + directorio destacado</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">VIP</td><td style="text-align:center;color:#FF6B9D;">€400-600</td><td style="padding:10px;">Todo lo anterior + colaboracion contenido mensual</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

        st.markdown("##### Potencial con 25-30 proveedores")
        st.markdown(
            '<div style="background:#F0FDF4;border-radius:8px;padding:16px;margin:16px 0;">'
            '<div style="font-size:0.875rem;color:#166534;">'
            '<div>15 basicos x €75 = €1,125</div>'
            '<div>8 premium x €200 = €1,600</div>'
            '<div>5 VIP x €500 = €2,500</div>'
            '<div style="font-weight:600;margin-top:8px;font-size:1rem;">Total: €5,225/mes</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("**Ingreso esperado mes 12**: €3,000-6,000/mes (recurrente)")

    # =========================================================================
    # SECTION 5: METRICAS Y SEGUIMIENTO
    # =========================================================================
    with st.expander("5. Metricas de Seguimiento", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### KPIs semanales")
            st.markdown("""
- Engagement rate por post
- Alcance por Reel
- Saves y shares por post
- Respuestas en Stories
- Crecimiento de seguidores
""")

        with col2:
            st.markdown("#### KPIs mensuales")
            st.markdown("""
- Engagement rate promedio
- Crecimiento total de seguidores
- Ingresos por fuente
- Conversion de afiliados
- Nuevos suscriptores email
""")

        st.markdown("#### Herramientas recomendadas")
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Herramienta</th>'
            '<th style="text-align:left;padding:10px;">Uso</th>'
            '<th style="text-align:center;padding:10px;">Coste</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Instagram Insights</td><td style="padding:10px;">Metricas basicas</td><td style="text-align:center;color:#16A34A;">Gratis</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">HypeAuditor</td><td style="padding:10px;">Analisis profundo</td><td style="text-align:center;color:#16A34A;">Gratis (basico)</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Metricool</td><td style="padding:10px;">Programacion + analytics</td><td style="text-align:center;">€12/mes</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Gumroad/Hotmart</td><td style="padding:10px;">Venta productos digitales</td><td style="text-align:center;">Comision</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Mailchimp/ConvertKit</td><td style="padding:10px;">Email marketing</td><td style="text-align:center;color:#16A34A;">Gratis hasta 500-1000</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

    # =========================================================================
    # SECTION 6: RIESGOS Y MITIGACION
    # =========================================================================
    with st.expander("6. Riesgos y Mitigacion", expanded=False):
        st.markdown(
            '<table style="width:100%;border-collapse:collapse;font-size:0.875rem;margin:16px 0;">'
            '<thead><tr style="border-bottom:2px solid #F0E6E8;background:#FFFBF7;">'
            '<th style="text-align:left;padding:10px;">Riesgo</th>'
            '<th style="text-align:center;padding:10px;">Prob.</th>'
            '<th style="text-align:center;padding:10px;">Impacto</th>'
            '<th style="text-align:left;padding:10px;">Mitigacion</th>'
            '</tr></thead><tbody>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Engagement no sube</td><td style="text-align:center;color:#D97706;">Media</td><td style="text-align:center;color:#DC2626;">Alto</td><td style="padding:10px;">Ajustar contenido, probar formatos, analizar competencia</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Pocas marcas interesadas</td><td style="text-align:center;color:#16A34A;">Baja</td><td style="text-align:center;color:#D97706;">Medio</td><td style="padding:10px;">Empezar con afiliados, demostrar valor con datos</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;"><td style="padding:10px;font-weight:500;">Producto digital no vende</td><td style="text-align:center;color:#D97706;">Media</td><td style="text-align:center;color:#D97706;">Medio</td><td style="padding:10px;">Validar idea antes de crear, empezar con producto pequeno</td></tr>'
            '<tr style="border-bottom:1px solid #F0E6E8;background:#FFFBF7;"><td style="padding:10px;font-weight:500;">Proveedores no pagan B2B</td><td style="text-align:center;color:#D97706;">Media</td><td style="text-align:center;color:#D97706;">Medio</td><td style="padding:10px;">Ofrecer prueba gratuita, demostrar ROI</td></tr>'
            '<tr><td style="padding:10px;font-weight:500;">Cambios algoritmo Instagram</td><td style="text-align:center;color:#DC2626;">Alta</td><td style="text-align:center;color:#D97706;">Medio</td><td style="padding:10px;">Diversificar (email, web), no depender 100% de IG</td></tr>'
            '</tbody></table>',
            unsafe_allow_html=True
        )

    # =========================================================================
    # SECTION 7: FUENTES Y REFERENCIAS
    # =========================================================================
    with st.expander("7. Fuentes y Referencias", expanded=False):
        st.markdown("""
**Analisis y Benchmarks**
- HypeAuditor - Analisis El Vals de la Novia
- Social Insider - Instagram Benchmarks 2025
- Hootsuite - Engagement rates por industria

**Monetizacion**
- Authority Hacker - Wedding Affiliate Programs
- Kajabi - Creator Economy
- Influencer Marketing Hub - Instagram Money Calculator

**Estrategia Instagram**
- Plann - How to Revive a Dead Instagram Account
- ContentStudio - Instagram Shadowban Guide
""")

        st.markdown(
            '<div style="background:#F5F5F4;border-radius:8px;padding:16px;margin-top:16px;font-size:0.75rem;color:#78716C;text-align:center;">'
            '<em>Documento creado: 17 de enero de 2026</em><br>'
            '<em>Proxima revision recomendada: 17 de febrero de 2026 (fin Fase 1)</em>'
            '</div>',
            unsafe_allow_html=True
        )
