"""
Dashboard page (Tab 1) - Overview with hero section and key metrics.
"""

import streamlit as st
from pathlib import Path

from src.components.hero import render_hero, render_focus_section
from src.components.metric_cards import render_metric_grid, render_kpi_comparison
from src.components.progress_ring import render_progress_ring
from src.components.timeline import render_timeline, render_phase_cards, render_month_indicator
from src.parsers.checklist_parser import parse_checklist_file, get_today_tasks, calculate_week_progress
from src.parsers.plan_parser import parse_plan_file, get_current_phase


def render_dashboard(docs_dir: Path, state: dict) -> None:
    """
    Render the main dashboard page.

    Args:
        docs_dir: Path to the documents directory.
        state: Current checkbox state dictionary.
    """
    # Parse data files
    checklist_path = docs_dir / "2026-01-17-checklist-semanas-1-4.md"
    plan_path = docs_dir / "2026-01-17-el-vals-de-la-novia-plan.md"

    checklist_data = parse_checklist_file(checklist_path)
    plan_data = parse_plan_file(plan_path)

    tasks = checklist_data.get("tasks", [])
    kpis = plan_data.get("kpis", {})

    # =========================================================================
    # HERO SECTION - Engagement Goal
    # =========================================================================
    render_hero(
        title="Engagement Rate",
        current_value="0.24%",
        target_value="1.5%",
        subtitle="Objetivo de rehabilitacion - Fase A",
    )

    # =========================================================================
    # METRICS GRID
    # =========================================================================
    st.markdown("### Metricas Clave")

    # Calculate task metrics
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if state.get(t["id"], t.get("done", False)))
    completion_pct = round((completed_tasks / total_tasks * 100) if total_tasks > 0 else 0)

    # Current phase
    current_phase = get_current_phase(month=1)

    metrics = [
        {
            "value": "0.24%",
            "label": "Engagement Actual",
            "delta": "vs 1.5% objetivo",
            "delta_positive": False,
            "icon": "",
        },
        {
            "value": f"{completed_tasks}/{total_tasks}",
            "label": "Tareas Completadas",
            "delta": f"{completion_pct}%",
            "delta_positive": completion_pct > 25,
            "icon": "",
        },
        {
            "value": current_phase["name"],
            "label": "Fase Actual",
            "icon": "",
        },
        {
            "value": "1",
            "label": "Dias Activos",
            "delta": "Recien comenzando",
            "delta_positive": True,
            "icon": "",
        },
    ]

    render_metric_grid(metrics)

    # =========================================================================
    # TODAY'S FOCUS
    # =========================================================================
    st.markdown("")  # Spacing

    today_tasks = get_today_tasks(tasks)
    if today_tasks:
        # Filter out completed tasks for focus section
        pending_today = [t for t in today_tasks if not state.get(t["id"], t.get("done", False))]
        if pending_today:
            render_focus_section(pending_today[:5])
    else:
        # Show first day's tasks as default
        week1_tasks = [t for t in tasks if "semana 1" in t.get("week", "").lower()]
        monday_tasks = [t for t in week1_tasks if "lunes" in t.get("day", "").lower()]
        if monday_tasks:
            pending = [t for t in monday_tasks if not state.get(t["id"], t.get("done", False))]
            if pending:
                render_focus_section(pending[:5])

    # =========================================================================
    # 12 MONTH TIMELINE
    # =========================================================================
    st.markdown("### Timeline 12 Meses")

    timeline_items = [
        {"label": "Mes 1", "sublabel": "Transicion", "status": "active"},
        {"label": "Mes 2", "sublabel": "Reels", "status": "pending"},
        {"label": "Mes 3", "sublabel": "Consolidar", "status": "pending"},
        {"label": "Mes 4", "sublabel": "Afiliados", "status": "pending"},
        {"label": "Mes 5", "sublabel": "Patrocinios", "status": "pending"},
        {"label": "Mes 6", "sublabel": "Productos", "status": "pending"},
        {"label": "Mes 7", "sublabel": "Digitales", "status": "pending"},
        {"label": "Mes 8", "sublabel": "B2B", "status": "pending"},
        {"label": "Mes 9", "sublabel": "Directorio", "status": "pending"},
        {"label": "Mes 10", "sublabel": "Escalar", "status": "pending"},
        {"label": "Mes 11", "sublabel": "Optimizar", "status": "pending"},
        {"label": "Mes 12", "sublabel": "Estabilizar", "status": "pending"},
    ]

    render_timeline(timeline_items, current_index=0)

    # =========================================================================
    # PHASE OVERVIEW
    # =========================================================================
    st.markdown("### Fases del Plan")

    phases = [
        {
            "name": "Fase A: Rehabilitacion",
            "description": "Transicion a Reels, despertar audiencia dormida, aumentar engagement de 0.24% a 1.5%+",
            "duration": "Meses 1-3",
            "status": "active",
        },
        {
            "name": "Fase B: Monetizacion",
            "description": "Implementar 3 modelos de negocio: afiliados, productos digitales, y directorio B2B",
            "duration": "Meses 4-12",
            "status": "pending",
        },
    ]

    render_phase_cards(phases, current_phase=0)

    # =========================================================================
    # PROGRESS OVERVIEW
    # =========================================================================
    st.markdown("### Progreso General")

    col1, col2, col3 = st.columns(3)

    with col1:
        week1_progress = calculate_week_progress(tasks, state, "semana 1")
        render_progress_ring(
            percentage=week1_progress["percentage"],
            size=100,
            label="Semana 1",
        )

    with col2:
        week2_progress = calculate_week_progress(tasks, state, "semana 2")
        render_progress_ring(
            percentage=week2_progress["percentage"],
            size=100,
            label="Semana 2",
        )

    with col3:
        overall_pct = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        render_progress_ring(
            percentage=overall_pct,
            size=100,
            label="Total Mes 1",
        )

    # =========================================================================
    # KPI TARGETS
    # =========================================================================
    st.markdown("### KPIs Objetivo Semana 4")

    col1, col2 = st.columns(2)

    with col1:
        render_kpi_comparison(
            label="Engagement Rate",
            current=0.24,
            target=0.6,
            unit="%",
        )
        render_kpi_comparison(
            label="Avg. Likes",
            current=269,
            target=400,
            unit="",
        )

    with col2:
        render_kpi_comparison(
            label="Avg. Comments",
            current=7,
            target=15,
            unit="",
        )
        render_kpi_comparison(
            label="Reels Publicados",
            current=0,
            target=16,
            unit="",
        )
