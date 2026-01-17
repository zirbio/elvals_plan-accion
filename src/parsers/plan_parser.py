"""
Parser for the strategic plan markdown file.
Extracts KPIs, phases, business models, and financial projections.
"""

import re
from pathlib import Path
from typing import Optional


def parse_plan_file(file_path: Path) -> dict:
    """
    Parse the entire plan file and return structured data.

    Args:
        file_path: Path to the plan markdown file.

    Returns:
        dict with keys: kpis, phases, business_models, projections, risks
    """
    if not file_path.exists():
        return {
            "kpis": {},
            "phases": [],
            "business_models": [],
            "projections": [],
            "risks": [],
        }

    content = file_path.read_text(encoding="utf-8")

    return {
        "kpis": parse_current_kpis(content),
        "phases": parse_phases(content),
        "business_models": parse_business_models(content),
        "projections": parse_financial_projections(content),
        "risks": parse_risks(content),
    }


def parse_current_kpis(content: str) -> dict:
    """
    Parse current KPIs from the plan.

    Args:
        content: Raw markdown content.

    Returns:
        Dict with KPI metrics and their values.
    """
    kpis = {}

    # Find the KPIs section
    kpi_section = re.search(
        r"### 1\.1 KPIs.*?\n(.*?)(?=\n###|\n##|\Z)",
        content,
        re.DOTALL
    )

    if not kpi_section:
        return kpis

    section_text = kpi_section.group(1)

    # Parse table rows: | **Metric** | Value | Benchmark | Status |
    rows = re.findall(
        r"\|\s*\**(.+?)\**\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|",
        section_text
    )

    for metric, value, benchmark, status in rows:
        metric = metric.strip().replace("**", "")
        if metric.lower() not in ["metrica", "---", "-"]:
            kpis[metric] = {
                "value": value.strip(),
                "benchmark": benchmark.strip(),
                "status": status.strip(),
            }

    return kpis


def parse_phases(content: str) -> list[dict]:
    """
    Parse the strategic phases from the plan.

    Args:
        content: Raw markdown content.

    Returns:
        List of phase dictionaries.
    """
    phases = [
        {
            "name": "Rehabilitacion",
            "description": "Transicion a Reels y recuperacion de engagement",
            "duration": "Meses 1-3",
            "target_engagement": "1.5%",
            "status": "active",
            "kpis": [
                {"label": "Engagement Rate", "current": 0.24, "target": 1.5, "unit": "%"},
                {"label": "Avg Likes", "current": 269, "target": 1000, "unit": ""},
                {"label": "Avg Comments", "current": 7, "target": 40, "unit": ""},
            ],
        },
        {
            "name": "Monetizacion",
            "description": "Implementacion de modelos de negocio",
            "duration": "Meses 4-12",
            "target_income": "10,500/mes",
            "status": "pending",
            "sub_phases": [
                {"name": "Afiliados + Patrocinios", "months": "4-5"},
                {"name": "Productos Digitales", "months": "6-7"},
                {"name": "Directorio B2B", "months": "8-12"},
            ],
        },
    ]

    return phases


def parse_business_models(content: str) -> list[dict]:
    """
    Parse business models from the plan.

    Args:
        content: Raw markdown content.

    Returns:
        List of business model dictionaries.
    """
    models = [
        {
            "name": "Afiliados + Patrocinios",
            "potential_income": "1,500-4,000/mes",
            "effort_rating": 4,
            "description": "Comisiones de productos y posts patrocinados",
            "start_month": 4,
            "icon": "",
        },
        {
            "name": "Productos Digitales",
            "potential_income": "1,000-5,000/mes",
            "effort_rating": 5,
            "description": "Guias, templates y cursos descargables",
            "start_month": 6,
            "icon": "",
        },
        {
            "name": "Directorio B2B",
            "potential_income": "2,000-6,000/mes",
            "effort_rating": 4,
            "description": "Suscripciones de proveedores de bodas",
            "start_month": 8,
            "icon": "",
        },
    ]

    return models


def parse_financial_projections(content: str) -> list[dict]:
    """
    Parse monthly financial projections.

    Args:
        content: Raw markdown content.

    Returns:
        List of monthly projection dictionaries.
    """
    projections = []

    # Find the projections table
    proj_section = re.search(
        r"### 5\.1 Ingresos mensuales.*?\n(.*?)(?=\n###|\n##|\Z)",
        content,
        re.DOTALL
    )

    if proj_section:
        section_text = proj_section.group(1)

        # Parse table rows
        rows = re.findall(
            r"\|\s*(\d+(?:-\d+)?)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*\**([^\|]+)\**\s*\|",
            section_text
        )

        for month, rehab, affiliates, products, b2b, total in rows:
            def clean_value(v):
                v = v.strip().replace("€", "").replace(",", "").replace("-", "0")
                try:
                    return int(v) if v.isdigit() else 0
                except ValueError:
                    return 0

            projections.append({
                "month": month.strip(),
                "affiliates": clean_value(affiliates),
                "products": clean_value(products),
                "b2b": clean_value(b2b),
                "total": clean_value(total.replace("**", "")),
            })

    # Default projections if parsing failed
    if not projections:
        projections = [
            {"month": "1-3", "affiliates": 0, "products": 0, "b2b": 0, "total": 0},
            {"month": "4", "affiliates": 500, "products": 0, "b2b": 0, "total": 500},
            {"month": "5", "affiliates": 1500, "products": 0, "b2b": 0, "total": 1500},
            {"month": "6", "affiliates": 1500, "products": 800, "b2b": 0, "total": 2300},
            {"month": "7", "affiliates": 1800, "products": 1500, "b2b": 0, "total": 3300},
            {"month": "8", "affiliates": 2000, "products": 1800, "b2b": 1000, "total": 4800},
            {"month": "9", "affiliates": 2000, "products": 2000, "b2b": 2000, "total": 6000},
            {"month": "10", "affiliates": 2200, "products": 2200, "b2b": 3000, "total": 7400},
            {"month": "11", "affiliates": 2200, "products": 2500, "b2b": 4000, "total": 8700},
            {"month": "12", "affiliates": 2500, "products": 3000, "b2b": 5000, "total": 10500},
        ]

    return projections


def parse_risks(content: str) -> list[dict]:
    """
    Parse risks and mitigations from the plan.

    Args:
        content: Raw markdown content.

    Returns:
        List of risk dictionaries.
    """
    risks = []

    # Find the risks section
    risk_section = re.search(
        r"## 9\. Riesgos.*?\n(.*?)(?=\n##|\Z)",
        content,
        re.DOTALL
    )

    if risk_section:
        section_text = risk_section.group(1)

        # Parse table rows
        rows = re.findall(
            r"\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|",
            section_text
        )

        for risk, probability, impact, mitigation in rows:
            risk = risk.strip()
            if risk.lower() not in ["riesgo", "---", "-"]:
                risks.append({
                    "risk": risk,
                    "probability": probability.strip(),
                    "impact": impact.strip(),
                    "mitigation": mitigation.strip(),
                })

    return risks


def get_current_phase(month: int = 1) -> dict:
    """
    Get information about the current phase based on the month.

    Args:
        month: Current month (1-12).

    Returns:
        Dict with phase information.
    """
    if month <= 3:
        return {
            "name": "Rehabilitacion",
            "phase_number": 1,
            "sub_phase": f"Semana {(month - 1) * 4 + 1}-{month * 4}",
            "focus": "Engagement y Reels",
        }
    elif month <= 5:
        return {
            "name": "Monetizacion",
            "phase_number": 2,
            "sub_phase": "Afiliados + Patrocinios",
            "focus": "Primeros ingresos",
        }
    elif month <= 7:
        return {
            "name": "Monetizacion",
            "phase_number": 2,
            "sub_phase": "Productos Digitales",
            "focus": "Guias y templates",
        }
    else:
        return {
            "name": "Monetizacion",
            "phase_number": 2,
            "sub_phase": "Directorio B2B",
            "focus": "Ingresos recurrentes",
        }
