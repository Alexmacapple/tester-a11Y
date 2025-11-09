#!/usr/bin/env python3
"""
Vérificateur de contraste couleur pour conformité WCAG/RGAA.

Ce module permet de vérifier si le contraste entre deux couleurs
respecte les standards d'accessibilité WCAG 2.1 et RGAA 4.1.

Usage:
    python contrast_checker.py "#000091" --background "#FFFFFF"
    python contrast_checker.py "#000091" --dsfr
"""

from typing import Tuple, Dict, Any


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convertit une couleur hexadécimale en RGB.

    Args:
        hex_color: Couleur au format hex (ex: "#000091" ou "000091")

    Returns:
        Tuple (R, G, B) avec valeurs 0-255

    Example:
        >>> hex_to_rgb("#000091")
        (0, 0, 145)
    """
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError(f"Couleur hex invalide: #{hex_color} (doit être 6 caractères)")

    try:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError(f"Couleur hex invalide: #{hex_color}")


def rgb_to_luminance(rgb: Tuple[int, int, int]) -> float:
    """
    Calcule la luminance relative d'une couleur RGB selon WCAG 2.1.

    Args:
        rgb: Tuple (R, G, B) avec valeurs 0-255

    Returns:
        Luminance relative (0-1)

    Reference:
        https://www.w3.org/TR/WCAG21/#dfn-relative-luminance
    """
    r, g, b = [x / 255.0 for x in rgb]

    # Linearisation des valeurs RGB
    def linearize(channel):
        if channel <= 0.03928:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4

    r_lin, g_lin, b_lin = linearize(r), linearize(g), linearize(b)

    # Calcul de la luminance (formule WCAG)
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def calculate_contrast_ratio(color1: str, color2: str) -> float:
    """
    Calcule le ratio de contraste entre deux couleurs selon WCAG 2.1.

    Args:
        color1: Couleur hex (ex: "#000091")
        color2: Couleur hex (ex: "#FFFFFF")

    Returns:
        Ratio de contraste (1:1 à 21:1)

    Reference:
        https://www.w3.org/TR/WCAG21/#dfn-contrast-ratio

    Example:
        >>> calculate_contrast_ratio("#000091", "#FFFFFF")
        13.23
    """
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    lum1 = rgb_to_luminance(rgb1)
    lum2 = rgb_to_luminance(rgb2)

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)


def check_wcag_compliance(
    ratio: float,
    text_size: int = 14,
    is_bold: bool = False
) -> Dict[str, Any]:
    """
    Vérifie la conformité WCAG d'un ratio de contraste.

    Args:
        ratio: Ratio de contraste
        text_size: Taille du texte en points (pt)
        is_bold: Si le texte est en gras

    Returns:
        Dictionnaire avec résultats de conformité

    Reference:
        - WCAG 2.1 niveau AA : 4.5:1 (texte normal), 3:1 (grand texte)
        - WCAG 2.1 niveau AAA : 7:1 (texte normal), 4.5:1 (grand texte)
        - Grand texte : ≥18pt ou ≥14pt bold

    Example:
        >>> check_wcag_compliance(13.2, text_size=14, is_bold=False)
        {'ratio': 13.2, 'level': 'AAA', 'status': '✅ Excellent', ...}
    """
    # Déterminer si c'est du grand texte
    is_large_text = text_size >= 18 or (text_size >= 14 and is_bold)

    compliance = {
        "ratio": round(ratio, 2),
        "text_size": text_size,
        "is_bold": is_bold,
        "is_large_text": is_large_text,
        "aa_normal": ratio >= 4.5,
        "aa_large": ratio >= 3.0,
        "aaa_normal": ratio >= 7.0,
        "aaa_large": ratio >= 4.5
    }

    # Déterminer le niveau global
    if is_large_text:
        if compliance["aaa_large"]:
            compliance["level"] = "AAA"
            compliance["status"] = "✅ Excellent (AAA)"
            compliance["compliant"] = True
        elif compliance["aa_large"]:
            compliance["level"] = "AA"
            compliance["status"] = "✅ Conforme (AA)"
            compliance["compliant"] = True
        else:
            compliance["level"] = "FAIL"
            compliance["status"] = "❌ Non conforme"
            compliance["compliant"] = False
            compliance["min_ratio_required"] = 3.0
    else:
        if compliance["aaa_normal"]:
            compliance["level"] = "AAA"
            compliance["status"] = "✅ Excellent (AAA)"
            compliance["compliant"] = True
        elif compliance["aa_normal"]:
            compliance["level"] = "AA"
            compliance["status"] = "✅ Conforme (AA)"
            compliance["compliant"] = True
        else:
            compliance["level"] = "FAIL"
            compliance["status"] = "❌ Non conforme"
            compliance["compliant"] = False
            compliance["min_ratio_required"] = 4.5

    return compliance


# Palette DSFR officielle
DSFR_COLORS = {
    "#000091": "Bleu France",
    "#000074": "Bleu France 975",
    "#1212FF": "Bleu France 113",
    "#E1000F": "Rouge Marianne",
    "#C9191E": "Rouge Marianne 472",
    "#F95C5E": "Rouge Marianne 425",
    "#161616": "Gris 1000 (Texte principal)",
    "#383838": "Gris 800",
    "#666666": "Gris 625",
    "#929292": "Gris 425",
    "#CECECE": "Gris 200",
    "#E5E5E5": "Gris 175",
    "#EEEEEE": "Gris 950",
    "#F6F6F6": "Gris 975",
    "#FFFFFF": "Blanc",
    "#0063CB": "Bleu Info",
    "#004F9F": "Bleu Info (hover)",
    "#18753C": "Vert Succès",
    "#0D5C2E": "Vert Succès (hover)",
    "#FC5D00": "Orange Attention",
    "#C74600": "Orange Attention (hover)",
    "#CE0500": "Rouge Erreur",
    "#9F0400": "Rouge Erreur (hover)"
}


def check_dsfr_colors(foreground: str, background: str = "#FFFFFF") -> Dict[str, Any]:
    """
    Vérifie si une combinaison de couleurs DSFR est accessible.

    Args:
        foreground: Couleur de texte hex
        background: Couleur de fond hex (défaut: blanc)

    Returns:
        Dict avec analyse de conformité DSFR et RGAA

    Example:
        >>> result = check_dsfr_colors("#000091", "#FFFFFF")
        >>> print(result['is_dsfr'], result['compliant'])
        True True
    """
    ratio = calculate_contrast_ratio(foreground, background)

    # Vérifier si la couleur foreground est dans la palette DSFR
    color_name = DSFR_COLORS.get(foreground.upper(), None)

    result = check_wcag_compliance(ratio)
    result["color_name"] = color_name if color_name else "❌ Couleur non-DSFR"
    result["is_dsfr"] = foreground.upper() in DSFR_COLORS
    result["foreground"] = foreground
    result["background"] = background

    return result


def suggest_dsfr_alternative(target_color: str, min_contrast: float = 4.5,
                             background: str = "#FFFFFF") -> Dict[str, Any]:
    """
    Suggère une couleur DSFR alternative si le contraste est insuffisant.

    Args:
        target_color: Couleur souhaitée (hex)
        min_contrast: Ratio de contraste minimum requis
        background: Couleur de fond (hex)

    Returns:
        Dict avec suggestions de couleurs DSFR alternatives
    """
    target_rgb = hex_to_rgb(target_color)
    suggestions = []

    for dsfr_hex, dsfr_name in DSFR_COLORS.items():
        ratio = calculate_contrast_ratio(dsfr_hex, background)

        if ratio >= min_contrast:
            dsfr_rgb = hex_to_rgb(dsfr_hex)

            # Calculer la distance euclidienne dans l'espace RGB
            distance = sum((c1 - c2) ** 2 for c1, c2 in zip(target_rgb, dsfr_rgb)) ** 0.5

            suggestions.append({
                "color": dsfr_hex,
                "name": dsfr_name,
                "contrast_ratio": round(ratio, 2),
                "color_distance": round(distance, 1)
            })

    # Trier par distance de couleur (plus proche en premier)
    suggestions.sort(key=lambda x: x["color_distance"])

    return {
        "target_color": target_color,
        "min_contrast_required": min_contrast,
        "background": background,
        "suggestions": suggestions[:5]  # Top 5
    }


# CLI pour utilisation en ligne de commande
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Vérifier le contraste entre deux couleurs (WCAG 2.1 / RGAA 4.1)"
    )
    parser.add_argument("foreground", help="Couleur de premier plan (texte) en hex")
    parser.add_argument("--background", "-b", default="#FFFFFF",
                       help="Couleur de fond en hex (défaut: blanc #FFFFFF)")
    parser.add_argument("--size", "-s", type=int, default=14,
                       help="Taille du texte en points (défaut: 14)")
    parser.add_argument("--bold", action="store_true",
                       help="Texte en gras")
    parser.add_argument("--dsfr", action="store_true",
                       help="Vérification DSFR spécifique")
    parser.add_argument("--suggest", action="store_true",
                       help="Suggérer des alternatives DSFR si non conforme")

    args = parser.parse_args()

    try:
        if args.dsfr:
            result = check_dsfr_colors(args.foreground, args.background)
        else:
            ratio = calculate_contrast_ratio(args.foreground, args.background)
            result = check_wcag_compliance(ratio, args.size, args.bold)
            result["foreground"] = args.foreground
            result["background"] = args.background

        print(f"\n🎨 Vérification de Contraste WCAG 2.1 / RGAA 4.1")
        print(f"{'='*60}")
        print(f"Couleur texte     : {result['foreground']}")
        if 'color_name' in result:
            print(f"                    ({result['color_name']})")
        print(f"Couleur fond      : {result['background']}")
        print(f"Taille texte      : {result.get('text_size', args.size)}pt {'(gras)' if result.get('is_bold', args.bold) else ''}")
        print(f"Ratio de contraste: {result['ratio']}:1")
        print(f"\n{result['status']}")
        print(f"Niveau WCAG       : {result['level']}")

        if 'is_dsfr' in result:
            if not result['is_dsfr']:
                print(f"\n⚠️  Attention : Couleur non conforme à la palette DSFR officielle")
            else:
                print(f"\n✅ Couleur conforme à la palette DSFR")

        if not result.get('compliant', True) and (args.suggest or args.dsfr):
            print(f"\n💡 Suggestions de couleurs DSFR alternatives:")
            suggestions = suggest_dsfr_alternative(
                args.foreground,
                result.get('min_ratio_required', 4.5),
                args.background
            )

            for i, sug in enumerate(suggestions['suggestions'][:3], 1):
                print(f"\n   {i}. {sug['color']} - {sug['name']}")
                print(f"      Contraste: {sug['contrast_ratio']}:1")
                print(f"      Similarité: {100 - sug['color_distance']/4.5:.0f}%")

        print(f"{'='*60}\n")

    except ValueError as e:
        print(f"❌ Erreur: {e}")
        exit(1)
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
