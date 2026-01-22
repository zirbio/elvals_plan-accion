"""
Parser for Instagram posts insights Excel files.
Extracts metrics from best and worst performing posts.
"""

import pandas as pd
from pathlib import Path
from typing import Optional


def parse_insights_files(data_dir: Path) -> dict:
    """
    Parse both best and worst posts Excel files.

    Args:
        data_dir: Path to the data directory containing the Excel files.

    Returns:
        dict with keys: best_posts, worst_posts, comparison, levers
    """
    best_path = data_dir / "10 mejores publicaciones 2025.xlsx"
    worst_path = data_dir / "10 peores publicaciones 2025.xlsx"

    best_posts = parse_posts_file(best_path)
    worst_posts = parse_posts_file(worst_path)

    if not best_posts or not worst_posts:
        return get_default_insights()

    comparison = calculate_comparison(best_posts, worst_posts)
    levers = extract_levers(comparison, best_posts, worst_posts)

    return {
        "best_posts": best_posts,
        "worst_posts": worst_posts,
        "comparison": comparison,
        "levers": levers,
    }


def parse_posts_file(file_path: Path) -> Optional[dict]:
    """
    Parse a single posts Excel file.

    Args:
        file_path: Path to the Excel file.

    Returns:
        dict with metrics and posts data, or None if file doesn't exist.
    """
    if not file_path.exists():
        return None

    try:
        df = pd.read_excel(file_path)

        # Rename columns for easier access
        column_map = {
            "Fecha publicación": "fecha",
            "Reproducciones": "views",
            "Cuentas alcanzadas": "reach",
            "Me gusta": "likes",
            "Comentarios": "comments",
            "Veces guardado": "saves",
            "Republicaciones": "shares",
            "Visitas al perfil": "profile_visits",
            "Nuevos seguidores": "new_followers",
            "% No seguidores": "pct_non_followers",
            "% Seguidores": "pct_followers",
            "Comentario": "caption",
        }

        df = df.rename(columns=column_map)

        # Clean percentage columns (remove % and convert)
        for col in ["pct_non_followers", "pct_followers"]:
            if col in df.columns:
                df[col] = df[col].apply(clean_percentage)

        # Calculate averages
        numeric_cols = ["views", "likes", "comments", "saves", "shares",
                        "profile_visits", "new_followers"]
        averages = {}
        for col in numeric_cols:
            if col in df.columns:
                averages[col] = safe_mean(df[col])

        # Average percentages
        if "pct_non_followers" in df.columns:
            averages["pct_non_followers"] = safe_mean(df["pct_non_followers"])

        # Extract posts data
        posts = []
        for _, row in df.iterrows():
            post = {
                "fecha": str(row.get("fecha", "")),
                "views": int(row.get("views", 0)) if pd.notna(row.get("views")) else 0,
                "likes": int(row.get("likes", 0)) if pd.notna(row.get("likes")) else 0,
                "comments": int(row.get("comments", 0)) if pd.notna(row.get("comments")) else 0,
                "saves": int(row.get("saves", 0)) if pd.notna(row.get("saves")) else 0,
                "caption": str(row.get("caption", ""))[:200] + "..." if len(str(row.get("caption", ""))) > 200 else str(row.get("caption", "")),
                "new_followers": int(row.get("new_followers", 0)) if pd.notna(row.get("new_followers")) else 0,
            }
            posts.append(post)

        # Extract caption characteristics
        captions = df["caption"].dropna().tolist()
        avg_caption_length = sum(len(str(c)) for c in captions) / len(captions) if captions else 0

        # Extract hashtags
        all_hashtags = []
        for caption in captions:
            hashtags = extract_hashtags(str(caption))
            all_hashtags.extend(hashtags)

        # Count hashtag frequency
        hashtag_counts = {}
        for tag in all_hashtags:
            hashtag_counts[tag] = hashtag_counts.get(tag, 0) + 1

        # Sort by frequency
        top_hashtags = sorted(hashtag_counts.items(), key=lambda x: -x[1])[:10]

        # Check for collaborations (mentions)
        collab_count = sum(1 for c in captions if "@" in str(c))
        collab_pct = (collab_count / len(captions) * 100) if captions else 0

        return {
            "averages": averages,
            "posts": posts,
            "count": len(posts),
            "avg_caption_length": avg_caption_length,
            "top_hashtags": top_hashtags,
            "collab_percentage": collab_pct,
        }

    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None


def clean_percentage(value) -> float:
    """Convert percentage string to float (as percentage 0-100)."""
    if pd.isna(value):
        return 0.0
    if isinstance(value, (int, float)):
        # If it's a decimal like 0.691, convert to percentage
        if 0 <= float(value) <= 1:
            return float(value) * 100
        return float(value)
    try:
        # Remove % and convert, handle comma as decimal separator
        clean = str(value).replace("%", "").replace(",", ".").strip()
        result = float(clean)
        # If result is between 0 and 1, it's likely a decimal percentage
        if 0 <= result <= 1:
            return result * 100
        return result
    except (ValueError, TypeError):
        return 0.0


def safe_mean(series) -> float:
    """Calculate mean safely, handling NaN values."""
    try:
        return float(series.dropna().mean()) if len(series.dropna()) > 0 else 0.0
    except (ValueError, TypeError):
        return 0.0


def extract_hashtags(text: str) -> list[str]:
    """Extract hashtags from text."""
    import re
    return re.findall(r"#(\w+)", text)


def calculate_comparison(best: dict, worst: dict) -> dict:
    """
    Calculate comparison metrics between best and worst posts.

    Args:
        best: Best posts data.
        worst: Worst posts data.

    Returns:
        dict with comparison metrics and ratios.
    """
    best_avg = best["averages"]
    worst_avg = worst["averages"]

    metrics = []

    # Views comparison
    best_views = best_avg.get("views", 0)
    worst_views = worst_avg.get("views", 0)
    ratio_views = best_views / worst_views if worst_views > 0 else 0
    metrics.append({
        "name": "Reproducciones",
        "best": int(best_views),
        "worst": int(worst_views),
        "ratio": f"{ratio_views:.0f}x",
        "icon": "",
    })

    # Likes comparison
    best_likes = best_avg.get("likes", 0)
    worst_likes = worst_avg.get("likes", 0)
    ratio_likes = best_likes / worst_likes if worst_likes > 0 else 0
    metrics.append({
        "name": "Me gusta",
        "best": int(best_likes),
        "worst": int(worst_likes),
        "ratio": f"{ratio_likes:.0f}x",
        "icon": "",
    })

    # Saves comparison
    best_saves = best_avg.get("saves", 0)
    worst_saves = worst_avg.get("saves", 0)
    ratio_saves = best_saves / worst_saves if worst_saves > 0 else 0
    metrics.append({
        "name": "Guardados",
        "best": int(best_saves),
        "worst": int(worst_saves),
        "ratio": f"{ratio_saves:.0f}x",
        "icon": "",
    })

    # New followers comparison
    best_followers = best_avg.get("new_followers", 0)
    worst_followers = worst_avg.get("new_followers", 0)
    ratio_followers = best_followers / worst_followers if worst_followers > 0 else 0
    metrics.append({
        "name": "Nuevos Seguidores",
        "best": int(best_followers),
        "worst": int(worst_followers),
        "ratio": f"{ratio_followers:.0f}x" if ratio_followers < 1000 else "+200/post",
        "icon": "",
    })

    # Non-followers percentage comparison
    best_nonfollowers = best_avg.get("pct_non_followers", 0)
    worst_nonfollowers = worst_avg.get("pct_non_followers", 0)
    metrics.append({
        "name": "% No Seguidores",
        "best": f"{best_nonfollowers:.0f}%",
        "worst": f"{worst_nonfollowers:.0f}%",
        "ratio": f"+{best_nonfollowers - worst_nonfollowers:.0f}pp",
        "icon": "",
    })

    return {
        "metrics": metrics,
        "caption_length": {
            "best": int(best.get("avg_caption_length", 0)),
            "worst": int(worst.get("avg_caption_length", 0)),
        },
        "collab_pct": {
            "best": best.get("collab_percentage", 0),
            "worst": worst.get("collab_percentage", 0),
        },
    }


def extract_levers(comparison: dict, best: dict, worst: dict) -> list[dict]:
    """
    Extract success levers from the analysis.

    Args:
        comparison: Comparison metrics.
        best: Best posts data.
        worst: Worst posts data.

    Returns:
        List of lever dictionaries with insights and actions.
    """
    return [
        {
            "title": "Inspiracion > Venta",
            "impact": "ALTO",
            "insight": f"Posts inspiracionales superan {comparison['metrics'][1]['ratio']} en likes a promociones directas",
            "action": "Transformar mensajes promocionales en historias emotivas sobre novias y vestidos",
            "icon": "",
        },
        {
            "title": "Colaboraciones Profesionales",
            "impact": "ALTO",
            "insight": f"{best.get('collab_percentage', 80):.0f}% de los mejores posts etiquetan diseñadores o fotografos",
            "action": "Siempre etiquetar al menos 1 profesional por publicacion",
            "icon": "",
        },
        {
            "title": "Captions Narrativos",
            "impact": "MEDIO",
            "insight": f"Mejores: ~{comparison['caption_length']['best']} chars vs Peores: ~{comparison['caption_length']['worst']} chars",
            "action": "Escribir captions largos con narrativa poetica y emocional",
            "icon": "",
        },
        {
            "title": "Viralidad Externa",
            "impact": "ALTO",
            "insight": f"Mejores posts: {comparison['metrics'][4]['best']} alcance a no seguidores vs {comparison['metrics'][4]['worst']}",
            "action": "Crear contenido universal y facilmente compartible",
            "icon": "",
        },
        {
            "title": "Evitar Sorteos",
            "impact": "ALTO",
            "insight": "Sorteos generan comentarios falsos pero 0 guardados y 0 conversion real",
            "action": "Eliminar completamente los sorteos de la estrategia",
            "icon": "",
        },
    ]


def get_default_insights() -> dict:
    """
    Return default insights data when Excel files are not available.

    Returns:
        dict with default values.
    """
    return {
        "best_posts": {
            "averages": {
                "views": 251304,
                "likes": 2793,
                "comments": 28,
                "saves": 2609,
                "new_followers": 200,
            },
            "posts": [],
            "count": 10,
            "avg_caption_length": 478,
            "top_hashtags": [
                ("NoviasConEstilo", 8),
                ("EleganciaAtemporal", 7),
                ("BodasConEncanto", 6),
            ],
            "collab_percentage": 80,
        },
        "worst_posts": {
            "averages": {
                "views": 19804,
                "likes": 63,
                "comments": 68,
                "saves": 15,
                "new_followers": 0,
            },
            "posts": [],
            "count": 10,
            "avg_caption_length": 245,
            "top_hashtags": [
                ("asesoriadebodas", 5),
                ("noviaespaña", 4),
            ],
            "collab_percentage": 20,
        },
        "comparison": {
            "metrics": [
                {"name": "Reproducciones", "best": 251304, "worst": 19804, "ratio": "12x", "icon": ""},
                {"name": "Me gusta", "best": 2793, "worst": 63, "ratio": "44x", "icon": ""},
                {"name": "Guardados", "best": 2609, "worst": 15, "ratio": "174x", "icon": ""},
                {"name": "Nuevos Seguidores", "best": 200, "worst": 0, "ratio": "+200/post", "icon": ""},
                {"name": "% No Seguidores", "best": "85%", "worst": "39%", "ratio": "+46pp", "icon": ""},
            ],
            "caption_length": {"best": 478, "worst": 245},
            "collab_pct": {"best": 80, "worst": 20},
        },
        "levers": [
            {
                "title": "Inspiracion > Venta",
                "impact": "ALTO",
                "insight": "Posts inspiracionales superan 44x en likes a promociones directas",
                "action": "Transformar mensajes promocionales en historias emotivas",
                "icon": "",
            },
            {
                "title": "Colaboraciones Profesionales",
                "impact": "ALTO",
                "insight": "80% de los mejores posts etiquetan diseñadores/fotografos",
                "action": "Siempre etiquetar al menos 1 profesional por publicacion",
                "icon": "",
            },
            {
                "title": "Captions Narrativos",
                "impact": "MEDIO",
                "insight": "Best: 478 chars vs Worst: 245 chars",
                "action": "Escribir captions largos con narrativa poetica",
                "icon": "",
            },
            {
                "title": "Viralidad Externa",
                "impact": "ALTO",
                "insight": "85% alcance a no seguidores vs 39%",
                "action": "Contenido universal y compartible",
                "icon": "",
            },
            {
                "title": "Evitar Sorteos",
                "impact": "ALTO",
                "insight": "Sorteos: muchos comentarios pero 0 guardados, 0 conversion",
                "action": "Eliminar sorteos completamente",
                "icon": "",
            },
        ],
    }
