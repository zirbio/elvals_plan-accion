"""
State management for El Vals de la Novia dashboard.
Handles local persistence with JSON files.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Any

# Default state file path
STATE_FILE = Path(__file__).parent.parent.parent / ".checklist_state.json"


def load_state() -> dict:
    """
    Load the application state from the JSON file.

    Returns:
        dict: The saved state, or empty dict if no state exists.
    """
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_state(state: dict) -> bool:
    """
    Save the application state to the JSON file.

    Args:
        state: The state dictionary to save.

    Returns:
        bool: True if save was successful, False otherwise.
    """
    try:
        # Add last updated timestamp
        state["_last_updated"] = datetime.now().isoformat()

        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
        return True
    except IOError:
        return False


def get_task_state(task_id: str, default: bool = False) -> bool:
    """
    Get the completion state of a specific task.

    Args:
        task_id: The unique identifier of the task.
        default: Default value if task not found.

    Returns:
        bool: Whether the task is completed.
    """
    state = load_state()
    return state.get(task_id, default)


def set_task_state(task_id: str, completed: bool) -> bool:
    """
    Set the completion state of a specific task.

    Args:
        task_id: The unique identifier of the task.
        completed: Whether the task is completed.

    Returns:
        bool: True if save was successful.
    """
    state = load_state()
    state[task_id] = completed
    return save_state(state)


def get_completed_count(task_ids: list[str]) -> int:
    """
    Count how many tasks are completed from a list of task IDs.

    Args:
        task_ids: List of task IDs to check.

    Returns:
        int: Number of completed tasks.
    """
    state = load_state()
    return sum(1 for tid in task_ids if state.get(tid, False))


def reset_all_tasks() -> bool:
    """
    Reset all task states (clear the state file).

    Returns:
        bool: True if reset was successful.
    """
    return save_state({})


def get_stats() -> dict:
    """
    Get statistics about the current state.

    Returns:
        dict: Statistics including total tasks, completed count, etc.
    """
    state = load_state()

    # Filter out metadata keys
    task_keys = [k for k in state.keys() if not k.startswith("_")]
    completed = sum(1 for k in task_keys if state.get(k, False))

    return {
        "total_tracked": len(task_keys),
        "completed": completed,
        "pending": len(task_keys) - completed,
        "completion_rate": (completed / len(task_keys) * 100) if task_keys else 0,
        "last_updated": state.get("_last_updated"),
    }


def init_session_state(st) -> dict:
    """
    Initialize Streamlit session state with saved data.

    Args:
        st: Streamlit module.

    Returns:
        dict: The current state.
    """
    if "checkbox_state" not in st.session_state:
        st.session_state.checkbox_state = load_state()

    return st.session_state.checkbox_state


def sync_state(st) -> None:
    """
    Sync session state to persistent storage.

    Args:
        st: Streamlit module.
    """
    if "checkbox_state" in st.session_state:
        save_state(st.session_state.checkbox_state)
