"""
Parser for the competitor analysis markdown file.
Extracts competitor data, opportunities, and recommendations.
"""

import re
from pathlib import Path
from typing import Optional


def parse_competitor_file(file_path: Path) -> dict:
    """
    Parse the entire competitor analysis file.

    Args:
        file_path: Path to the competitor analysis markdown file.

    Returns:
        dict with keys: competitors, opportunities, recommendations
    """
    if not file_path.exists():
        return {
            "competitors": get_default_competitors(),
            "opportunities": get_default_opportunities(),
            "recommendations": [],
        }

    content = file_path.read_text(encoding="utf-8")

    return {
        "competitors": parse_competitors(content),
        "opportunities": parse_opportunities(content),
        "recommendations": parse_recommendations(content),
    }


def parse_competitors(content: str) -> list[dict]:
    """
    Parse individual competitor profiles.

    Args:
        content: Raw markdown content.

    Returns:
        List of competitor dictionaries.
    """
    competitors = []

    # Define competitor patterns to extract
    competitor_sections = [
        ("INVITADA PERFECTA", "@invitada_perfecta", "IP"),
        ("BRIDALADA", "@bridalada", "BR"),
        ("MISS CAVALLIER", "@misscavallier", "MC"),
        ("UNA BODA ORIGINAL", "@unabodaoriginal", "UBO"),
        ("LA CHAMPANERA", "@lachampanera", "LC"),
        ("BODAS.NET", "@bodasnet", "BN"),
        ("TELVA NOVIAS", "@telvanovias", "TN"),
    ]

    for name, handle, initials in competitor_sections:
        # Find the section for this competitor
        section_pattern = rf"###.*?{name}.*?\n(.*?)(?=\n###|\n##|\Z)"
        match = re.search(section_pattern, content, re.DOTALL | re.IGNORECASE)

        if match:
            section = match.group(1)

            # Extract followers
            followers_match = re.search(
                r"Seguidores\s*\|\s*[~]?(\d+(?:,\d+)?(?:K|\.?\d+)?)",
                section,
                re.IGNORECASE
            )
            followers = followers_match.group(1) if followers_match else "?"

            # Format followers
            if followers and followers != "?":
                followers = followers.replace(",", "")
                if followers.isdigit() and int(followers) >= 1000:
                    followers = f"{int(int(followers) / 1000)}K"

            # Extract business model (look for Modelo de negocio section)
            model_match = re.search(
                r"Modelo de negocio.*?[-\*]\s*(.+?)(?=\n[-\*]|\n\*\*|\n##|\Z)",
                section,
                re.DOTALL | re.IGNORECASE
            )
            model = model_match.group(1).strip() if model_match else "Contenido + Patrocinios"

            # Clean up model text
            model = re.sub(r"\*\*.*?\*\*:?\s*", "", model)
            model = model.split("\n")[0].strip()[:50]

            # Extract differentiator from strengths
            diff_match = re.search(
                r"Fortalezas.*?[-\*]\s*(.+?)(?=\n[-\*]|\n\*\*|\n##|\Z)",
                section,
                re.DOTALL | re.IGNORECASE
            )
            differentiator = diff_match.group(1).strip() if diff_match else None
            if differentiator:
                differentiator = differentiator.split("\n")[0].strip()[:60]

            competitors.append({
                "name": name.title(),
                "handle": handle,
                "followers": followers,
                "model": model,
                "avatar_initials": initials,
                "differentiator": differentiator,
            })

    # If parsing failed, return defaults
    if not competitors:
        return get_default_competitors()

    return competitors


def get_default_competitors() -> list[dict]:
    """
    Return default competitor data.

    Returns:
        List of competitor dictionaries.
    """
    return [
        {
            "name": "Invitada Perfecta",
            "handle": "@invitada_perfecta",
            "followers": "500K",
            "model": "Contenido + Blog + Afiliados",
            "avatar_initials": "IP",
            "differentiator": "Foco en invitadas",
            "priority": "4",
        },
        {
            "name": "Bodas.net",
            "handle": "@bodasnet",
            "followers": "303K",
            "model": "Directorio B2B",
            "avatar_initials": "BN",
            "differentiator": "Corporativo + Sorteos",
            "priority": None,
        },
        {
            "name": "Bridalada",
            "handle": "@bridalada",
            "followers": "292K",
            "model": "Marca de moda propia",
            "avatar_initials": "BR",
            "differentiator": "Personal + Accesible",
            "priority": "3",
        },
        {
            "name": "Miss Cavallier",
            "handle": "@misscavallier",
            "followers": "281K",
            "model": "Alquiler vestidos",
            "avatar_initials": "MC",
            "differentiator": "Wedding planner real",
            "priority": None,
        },
        {
            "name": "Una Boda Original",
            "handle": "@unabodaoriginal",
            "followers": "115K",
            "model": "Inspiracion visual",
            "avatar_initials": "UBO",
            "differentiator": "Galeria de calidad",
            "priority": "1",
        },
        {
            "name": "La Champanera",
            "handle": "@lachampanera",
            "followers": "100K",
            "model": "Agencia comunicacion",
            "avatar_initials": "LC",
            "differentiator": "Anti-topicos",
            "priority": "2",
        },
        {
            "name": "TELVA Novias",
            "handle": "@telvanovias",
            "followers": "76K",
            "model": "Medio tradicional",
            "avatar_initials": "TN",
            "differentiator": "Editorial/Tendencias",
            "priority": None,
        },
    ]


def parse_opportunities(content: str) -> list[dict]:
    """
    Parse market opportunities and gaps.

    Args:
        content: Raw markdown content.

    Returns:
        List of opportunity dictionaries.
    """
    opportunities = []

    # Find opportunities section
    opp_section = re.search(
        r"Gaps y oportunidades.*?\n(.*?)(?=\n##|\Z)",
        content,
        re.DOTALL | re.IGNORECASE
    )

    if opp_section:
        section = opp_section.group(1)

        # Parse numbered items
        items = re.findall(
            r"\d+\.\s*\**(.+?)\**\s*[-—]\s*(.+?)(?=\n\d+\.|\n\*\*|\Z)",
            section
        )

        for title, description in items:
            opportunities.append({
                "title": title.strip(),
                "description": description.strip(),
            })

    # Default opportunities if parsing failed
    if not opportunities:
        return get_default_opportunities()

    return opportunities


def get_default_opportunities() -> list[dict]:
    """
    Return default market opportunities.

    Returns:
        List of opportunity dictionaries.
    """
    return [
        {
            "title": "Reels/Video corto",
            "description": "La mayoria sigue siendo muy estatica. Oportunidad de first mover en formato video.",
            "icon": "",
        },
        {
            "title": "Productos Digitales",
            "description": "Ningun competidor tiene cursos o guias claros. Territorio libre.",
            "icon": "",
        },
        {
            "title": "Comunidad/Membresia",
            "description": "No hay clubes de novias. Oportunidad de crear engagement real.",
            "icon": "",
        },
        {
            "title": "Educacion Estructurada",
            "description": "Tips sueltos pero no formacion. Espacio para contenido educativo.",
            "icon": "",
        },
    ]


def parse_recommendations(content: str) -> list[dict]:
    """
    Parse strategic recommendations.

    Args:
        content: Raw markdown content.

    Returns:
        List of recommendation dictionaries grouped by timeframe.
    """
    recommendations = []

    # Find recommendations section
    rec_section = re.search(
        r"## 6\. Recomendaciones.*?\n(.*?)(?=\n##|\Z)",
        content,
        re.DOTALL
    )

    if rec_section:
        section = rec_section.group(1)

        # Parse by timeframe
        timeframes = [
            ("Corto plazo", "meses 1-3"),
            ("Medio plazo", "meses 4-8"),
            ("Largo plazo", "meses 9-12"),
        ]

        for title, duration in timeframes:
            pattern = rf"###.*?{title}.*?\n(.*?)(?=\n###|\Z)"
            match = re.search(pattern, section, re.DOTALL | re.IGNORECASE)

            if match:
                items_text = match.group(1)
                items = re.findall(r"-\s*\[\s*\]\s*(.+?)(?=\n-|\Z)", items_text)

                recommendations.append({
                    "timeframe": title,
                    "duration": duration,
                    "items": [item.strip() for item in items if item.strip()],
                })

    return recommendations


def get_competitor_comparison_data() -> list[dict]:
    """
    Get formatted data for competitor comparison table.

    Returns:
        List of comparison row dictionaries.
    """
    return [
        {
            "account": "Invitada Perfecta",
            "followers": "~500K",
            "model": "Contenido + Blog + Afiliados",
            "differentiator": "Foco en invitadas",
        },
        {
            "account": "Bodas.net",
            "followers": "303K",
            "model": "Directorio B2B",
            "differentiator": "Corporativo + Sorteos",
        },
        {
            "account": "Bridalada",
            "followers": "292K",
            "model": "Marca de moda propia",
            "differentiator": "Personal + Accesible",
        },
        {
            "account": "Miss Cavallier",
            "followers": "281K",
            "model": "Alquiler vestidos",
            "differentiator": "Wedding planner real",
        },
        {
            "account": "El Vals de la Novia",
            "followers": "115K",
            "model": "Por definir",
            "differentiator": "Inspiracion visual",
            "highlight": True,
        },
        {
            "account": "Una Boda Original",
            "followers": "~115K",
            "model": "Inspiracion",
            "differentiator": "Galeria de calidad",
        },
        {
            "account": "La Champanera",
            "followers": "~100K",
            "model": "Agencia comunicacion",
            "differentiator": "Anti-topicos",
        },
        {
            "account": "TELVA Novias",
            "followers": "76K",
            "model": "Medio tradicional",
            "differentiator": "Editorial/Tendencias",
        },
    ]
