"""
Task card component with premium checkbox design.
The main interactive element of the checklist.
"""

import streamlit as st
from typing import Callable, Optional


def render_task_card(
    task_id: str,
    text: str,
    completed: bool,
    time_estimate: Optional[str] = None,
    on_change: Optional[Callable[[str, bool], None]] = None,
) -> bool:
    """
    Render a premium task card with checkbox.

    Args:
        task_id: Unique identifier for the task.
        text: Task description text.
        completed: Whether the task is completed.
        time_estimate: Optional time estimate (e.g., "15min").
        on_change: Optional callback when state changes.

    Returns:
        bool: The new completion state after any changes.
    """
    # Create the checkbox with Streamlit
    time_badge = f" ({time_estimate})" if time_estimate else ""

    new_value = st.checkbox(
        f"{text}{time_badge}",
        value=completed,
        key=task_id,
    )

    # If state changed, call callback
    if new_value != completed and on_change:
        on_change(task_id, new_value)

    return new_value


def render_task_card_html(
    text: str,
    completed: bool,
    time_estimate: Optional[str] = None,
) -> str:
    """
    Return HTML for a task card (non-interactive display).

    Args:
        text: Task description text.
        completed: Whether the task is completed.
        time_estimate: Optional time estimate.

    Returns:
        str: HTML string for the task card.
    """
    completed_class = "completed" if completed else ""
    checkbox_class = "checked" if completed else ""
    text_style = "text-decoration: line-through; color: #8B7E74;" if completed else ""

    time_html = ""
    if time_estimate:
        time_html = f'<span class="task-time">{time_estimate}</span>'

    return f"""
    <div class="task-card {completed_class}">
        <div class="task-checkbox {checkbox_class}"></div>
        <span class="task-text" style="{text_style}">{text}</span>
        {time_html}
    </div>
    """


def render_day_header(day_name: str, icon: str = "") -> None:
    """
    Render a day section header.

    Args:
        day_name: Name of the day (e.g., "Lunes - Dia de Auditoria").
        icon: Optional emoji icon.
    """
    # Map day names to icons
    day_icons = {
        "lunes": "",
        "martes": "",
        "miercoles": "",
        "jueves": "",
        "viernes": "",
        "sabado": "",
        "domingo": "",
    }

    if not icon:
        day_lower = day_name.lower().split()[0] if day_name else ""
        icon = day_icons.get(day_lower, "")

    st.markdown(
        f'<div style="background:linear-gradient(135deg,#FF6B9D 0%,#C084FC 100%);color:white;padding:12px 20px;border-radius:12px;margin:24px 0 12px 0;font-family:Playfair Display,serif;font-weight:500;font-size:1rem;display:flex;align-items:center;gap:12px;">'
        f'<span style="font-size:1.25rem;">{icon}</span>'
        f'<span>{day_name}</span>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_task_list(
    tasks: list[dict],
    state: dict,
    on_change: Optional[Callable[[str, bool], None]] = None,
) -> dict:
    """
    Render a list of tasks with checkboxes.

    Args:
        tasks: List of task dicts with keys: id, text, time, done.
        state: Current state dictionary.
        on_change: Optional callback when any task changes.

    Returns:
        dict: Updated state dictionary.
    """
    updated_state = state.copy()

    for task in tasks:
        task_id = task.get("id", "")
        text = task.get("text", "")
        time = task.get("time", "")
        default_done = task.get("done", False)

        current_value = state.get(task_id, default_done)

        new_value = render_task_card(
            task_id=task_id,
            text=text,
            completed=current_value,
            time_estimate=time,
            on_change=on_change,
        )

        if new_value != current_value:
            updated_state[task_id] = new_value

    return updated_state


def render_ideas_bank(ideas: list[dict]) -> None:
    """
    Render the ideas bank section (expandable).

    Args:
        ideas: List of idea dicts with keys: category, items.
    """
    with st.expander("Ideas de Contenido", expanded=False):
        for idea_group in ideas:
            category = idea_group.get("category", "")
            items = idea_group.get("items", [])

            st.markdown(f"**{category}**")

            for item in items:
                st.markdown(
                    f'<div style="padding:8px 12px;margin:4px 0;background:#FFFBF7;border-radius:8px;border-left:3px solid #C084FC;font-size:0.9rem;color:#3D3D3D;">{item}</div>',
                    unsafe_allow_html=True
                )

            st.markdown("")
