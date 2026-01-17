"""
Parser for the checklist markdown file.
Extracts structured task data from markdown tables and lists.
"""

import re
from pathlib import Path
from typing import Optional


def parse_checklist_file(file_path: Path) -> dict:
    """
    Parse the entire checklist file and return structured data.

    Args:
        file_path: Path to the checklist markdown file.

    Returns:
        dict with keys: tasks, weeks, summary, ideas
    """
    if not file_path.exists():
        return {"tasks": [], "weeks": {}, "summary": {}, "ideas": []}

    content = file_path.read_text(encoding="utf-8")

    return {
        "tasks": parse_tasks(content),
        "weeks": group_tasks_by_week(parse_tasks(content)),
        "summary": parse_summary_metrics(content),
        "ideas": parse_ideas_bank(content),
    }


def parse_tasks(content: str) -> list[dict]:
    """
    Parse all tasks from the checklist content.

    Args:
        content: Raw markdown content.

    Returns:
        List of task dictionaries with keys: id, week, day, text, time, done
    """
    tasks = []
    current_week = ""
    current_day = ""
    task_id = 0

    lines = content.split("\n")

    for line in lines:
        # Detect week headers: ## SEMANA 1: ...
        week_match = re.match(r"^## (SEMANA \d+[^#]*)", line, re.IGNORECASE)
        if week_match:
            current_week = week_match.group(1).strip()
            continue

        # Detect day headers: ### Lunes - ...
        day_match = re.match(r"^### (.+)", line)
        if day_match:
            day_text = day_match.group(1).strip()
            # Skip headers that aren't days
            if not any(skip in day_text.lower() for skip in ["resumen", "metricas", "preguntas", "notas"]):
                current_day = day_text
            continue

        # Parse table rows: | [ ] Task text | time | status |
        table_task = re.match(
            r"\|\s*\[([ xX])\]\s*(.+?)\s*\|\s*(\d+\w+)?\s*\|",
            line
        )
        if table_task:
            is_done = table_task.group(1).lower() == "x"
            task_text = table_task.group(2).strip()
            time_estimate = table_task.group(3) or ""

            # Clean up task text (remove trailing | and other artifacts)
            task_text = re.sub(r"\s*\|.*$", "", task_text).strip()

            if task_text and not task_text.startswith("-"):
                tasks.append({
                    "id": f"task_{task_id}",
                    "week": current_week,
                    "day": current_day,
                    "text": task_text,
                    "time": time_estimate,
                    "done": is_done,
                })
                task_id += 1
            continue

        # Parse standalone checkboxes: - [ ] Task text
        loose_task = re.match(r"^-?\s*\[([ xX])\]\s*(.+)$", line)
        if loose_task:
            is_done = loose_task.group(1).lower() == "x"
            task_text = loose_task.group(2).strip()

            # Skip if it's a table row or metadata
            if "|" not in task_text and task_text:
                tasks.append({
                    "id": f"task_{task_id}",
                    "week": current_week,
                    "day": current_day,
                    "text": task_text,
                    "time": "",
                    "done": is_done,
                })
                task_id += 1

    return tasks


def group_tasks_by_week(tasks: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """
    Group tasks by week and day.

    Args:
        tasks: List of task dictionaries.

    Returns:
        Nested dict: {week_name: {day_name: [tasks]}}
    """
    weeks = {}

    for task in tasks:
        week = task.get("week") or "Sin semana"
        day = task.get("day") or "General"

        if week not in weeks:
            weeks[week] = {}
        if day not in weeks[week]:
            weeks[week][day] = []

        weeks[week][day].append(task)

    return weeks


def parse_summary_metrics(content: str) -> dict:
    """
    Parse summary metrics from the checklist.

    Args:
        content: Raw markdown content.

    Returns:
        Dict with weekly objectives and targets.
    """
    summaries = {}

    # Find week summary sections
    summary_pattern = r"### Resumen Semana (\d+)\s*\n(.*?)(?=\n##|\n---|\Z)"
    matches = re.findall(summary_pattern, content, re.DOTALL)

    for week_num, section in matches:
        metrics = {}

        # Parse table rows in summary
        metric_rows = re.findall(
            r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|",
            section
        )

        for metric, value in metric_rows:
            metric = metric.strip()
            value = value.strip()
            if metric and value and metric.lower() not in ["metrica", "---"]:
                metrics[metric] = value

        summaries[f"Semana {week_num}"] = metrics

    return summaries


def parse_ideas_bank(content: str) -> list[dict]:
    """
    Parse the ideas bank section.

    Args:
        content: Raw markdown content.

    Returns:
        List of idea groups with categories and items.
    """
    ideas = []

    # Find ideas section
    ideas_match = re.search(
        r"## IDEAS DE CONTENIDO.*?\n(.*?)(?=\n##|\n---|\Z)",
        content,
        re.DOTALL | re.IGNORECASE
    )

    if not ideas_match:
        return ideas

    ideas_section = ideas_match.group(1)

    # Parse categories (### headers)
    category_pattern = r"###\s*(.+?)\s*\n(.*?)(?=\n###|\Z)"
    categories = re.findall(category_pattern, ideas_section, re.DOTALL)

    for category, items_text in categories:
        items = []

        # Parse checkbox items
        item_matches = re.findall(r"-\s*\[\s*\]\s*(.+?)(?=\n|$)", items_text)
        items.extend([item.strip() for item in item_matches if item.strip()])

        if items:
            ideas.append({
                "category": category.strip(),
                "items": items,
            })

    return ideas


def get_today_tasks(tasks: list[dict], day_name: Optional[str] = None) -> list[dict]:
    """
    Get tasks for today or a specific day.

    Args:
        tasks: List of all tasks.
        day_name: Optional specific day (e.g., "Lunes"). If None, uses current day.

    Returns:
        List of tasks for the specified day.
    """
    import datetime

    if day_name is None:
        # Get Spanish day name
        day_names_es = {
            0: "lunes",
            1: "martes",
            2: "miercoles",
            3: "jueves",
            4: "viernes",
            5: "sabado",
            6: "domingo",
        }
        day_name = day_names_es.get(datetime.datetime.now().weekday(), "lunes")

    day_name_lower = day_name.lower()

    return [
        task for task in tasks
        if task.get("day", "").lower().startswith(day_name_lower)
    ]


def calculate_week_progress(tasks: list[dict], state: dict, week_name: str) -> dict:
    """
    Calculate progress statistics for a specific week.

    Args:
        tasks: List of all tasks.
        state: Current completion state dict.
        week_name: Name of the week to calculate for.

    Returns:
        Dict with total, completed, pending, percentage.
    """
    week_tasks = [t for t in tasks if week_name.lower() in t.get("week", "").lower()]
    total = len(week_tasks)
    completed = sum(1 for t in week_tasks if state.get(t["id"], t.get("done", False)))

    return {
        "total": total,
        "completed": completed,
        "pending": total - completed,
        "percentage": round((completed / total * 100) if total > 0 else 0, 1),
    }
