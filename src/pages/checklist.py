"""
Checklist page (Tab 2) - Weekly plan with interactive tasks.
"""

import streamlit as st
from pathlib import Path

from src.components.progress_ring import render_progress_ring, render_progress_bar
from src.components.task_card import render_day_header, render_ideas_bank
from src.parsers.checklist_parser import (
    parse_checklist_file,
    calculate_week_progress,
)
from src.utils.state import save_state


def render_checklist(docs_dir: Path, state: dict) -> dict:
    """
    Render the checklist page with interactive tasks.

    Args:
        docs_dir: Path to the documents directory.
        state: Current checkbox state dictionary.

    Returns:
        Updated state dictionary.
    """
    # Parse checklist
    checklist_path = docs_dir / "2026-01-17-checklist-semanas-1-4.md"
    checklist_data = parse_checklist_file(checklist_path)

    tasks = checklist_data.get("tasks", [])
    weeks = checklist_data.get("weeks", {})
    ideas = checklist_data.get("ideas", [])

    if not tasks:
        st.warning("No se encontraron tareas en el checklist.")
        return state

    # Get week names
    week_names = list(weeks.keys())

    if not week_names:
        st.error("No se encontraron semanas en el checklist.")
        return state

    # =========================================================================
    # WEEK SELECTOR WITH TABS
    # =========================================================================
    week_tabs = st.tabs(week_names)

    for tab, week_name in zip(week_tabs, week_names):
        with tab:
            week_data = weeks.get(week_name, {})

            # Calculate week progress
            week_tasks = [t for day_tasks in week_data.values() for t in day_tasks]
            week_progress = calculate_week_progress(tasks, state, week_name)

            # =========================================================================
            # WEEK HEADER WITH PROGRESS
            # =========================================================================
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(
                    f'<div style="margin-bottom:16px;">'
                    f'<span style="font-family:Montserrat,sans-serif;font-size:0.9rem;color:#8B7E74;">'
                    f'Progreso: <strong>{week_progress["completed"]}/{week_progress["total"]}</strong> tareas'
                    f'</span>'
                    f'</div>',
                    unsafe_allow_html=True
                )

                render_progress_bar(
                    completed=week_progress["completed"],
                    total=week_progress["total"],
                )

            with col2:
                render_progress_ring(
                    percentage=week_progress["percentage"],
                    size=80,
                )

            # =========================================================================
            # DAY SECTIONS
            # =========================================================================
            day_names = list(week_data.keys())

            for day_name in day_names:
                day_tasks = week_data.get(day_name, [])

                if not day_tasks:
                    continue

                # Day header
                if day_name and day_name != "General":
                    render_day_header(day_name)

                # Tasks for this day
                for task in day_tasks:
                    task_id = task.get("id", "")
                    text = task.get("text", "")
                    time = task.get("time", "")
                    default_done = task.get("done", False)

                    current_value = state.get(task_id, default_done)

                    # Format label with time badge
                    label = text
                    if time:
                        label = f"{text} ({time})"

                    # Render checkbox
                    new_value = st.checkbox(
                        label,
                        value=current_value,
                        key=task_id,
                    )

                    # Update state if changed
                    if new_value != current_value:
                        state[task_id] = new_value
                        save_state(state)
                        st.rerun()

    # =========================================================================
    # IDEAS BANK (Outside tabs)
    # =========================================================================
    st.markdown("---")

    if ideas:
        render_ideas_bank(ideas)
    else:
        # Default ideas if parsing didn't work
        default_ideas = [
            {
                "category": "Emocionales/Aspiracionales",
                "items": [
                    "POV: el dia de tu boda",
                    "Momentos que toda novia deberia vivir",
                    "Cuando ves a tu padre por primera vez vestida de novia",
                    "El momento del si quiero",
                    "Detalles que hacen una boda perfecta",
                ],
            },
            {
                "category": "Educativos/Tips",
                "items": [
                    "3 errores que cometen todas las novias",
                    "Lo que nadie te cuenta sobre organizar tu boda",
                    "Como elegir el vestido perfecto para tu cuerpo",
                    "5 preguntas que debes hacer al wedding planner",
                    "Cuanto cuesta realmente una boda",
                ],
            },
            {
                "category": "Tendencias adaptadas",
                "items": [
                    "[Audio trending] con transiciones de vestidos",
                    "[Audio trending] con get ready with me novia",
                    "[Audio trending] con antes/despues decoracion",
                ],
            },
            {
                "category": "Proveedores/Inspiracion",
                "items": [
                    "Descubriendo a [fotografo]",
                    "Este venue os va a enamorar",
                    "Vestido de [disenador] que es una obra de arte",
                    "Floristas que deberias conocer",
                ],
            },
        ]
        render_ideas_bank(default_ideas)

    return state


def render_week_summary(week_name: str, progress: dict) -> None:
    """
    Render a summary card for a week's progress.

    Args:
        week_name: Name of the week.
        progress: Progress statistics dict.
    """
    status_color = "#86EFAC" if progress["percentage"] >= 100 else "#FBBF24" if progress["percentage"] >= 50 else "#FCA5A5"

    st.markdown(
        f'<div style="background:white;border-radius:16px;padding:20px;box-shadow:0 2px 12px rgba(0,0,0,0.04);border:1px solid #F0E6E8;text-align:center;">'
        f'<div style="font-family:Playfair Display,serif;font-size:1.125rem;color:#3D3D3D;margin-bottom:8px;">{week_name}</div>'
        f'<div style="font-family:Playfair Display,serif;font-size:2rem;font-weight:600;color:{status_color};">{progress["percentage"]:.0f}%</div>'
        f'<div style="font-size:0.875rem;color:#8B7E74;">{progress["completed"]}/{progress["total"]} tareas</div>'
        f'</div>',
        unsafe_allow_html=True
    )
