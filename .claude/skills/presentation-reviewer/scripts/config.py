#!/usr/bin/env python3
"""
Configuration pour l'analyseur de présentations PowerPoint.

Ce module permet de personnaliser les seuils et critères d'analyse
selon les besoins spécifiques de l'utilisateur ou du contexte.
"""

import json
from pathlib import Path
from typing import Dict, Any


# Configuration par défaut (standards de conseil)
DEFAULT_CONFIG = {
    # === Limites de contenu ===
    'max_words_per_slide': 50,
    'max_bullets_per_slide': 7,
    'min_words_per_slide': 5,

    # === Typographie ===
    'min_font_size': 14,
    'min_title_font_size': 18,
    'max_font_variations': 4,

    # === Structure ===
    'max_dense_slides_consecutive': 3,
    'dense_slide_threshold': 40,  # en mots
    'min_slides_for_toc': 15,     # table des matières recommandée si >15 slides

    # === Timing ===
    'minutes_per_slide': 2,  # durée moyenne par slide en minutes
    'max_slides_30min': 15,  # nombre max de slides pour 30 min

    # === Sévérité des problèmes ===
    'severity_rules': {
        'high': [
            'no_title',
            'contrast_insufficient',
            'too_many_words',
            'no_conclusion'
        ],
        'medium': [
            'font_inconsistency',
            'too_many_bullets',
            'dense_slides_consecutive',
            'missing_logo'
        ],
        'low': [
            'empty_slide',
            'minor_formatting',
            'suggestion'
        ]
    },

    # === Conformité DSFR ===
    'dsfr': {
        'enforce': False,  # Activer la vérification DSFR stricte
        'required_colors': ['#000091', '#E1000F'],  # Bleu France, Rouge Marianne
        'required_logos': ['RF', 'ministere'],
        'min_contrast_ratio': 4.5,
        'required_font': 'Marianne'
    },

    # === Accessibilité RGAA ===
    'rgaa': {
        'level': 'AA',  # AA ou AAA
        'check_contrast': True,
        'check_alt_text': True,
        'check_color_only_info': True
    },

    # === Frameworks ===
    'framework_detection': {
        'min_confidence': 0.3,  # confiance minimum pour détecter un framework
        'weight_position': True,  # pondérer selon position des mots-clés
        'suggest_if_none': True   # suggérer un framework si aucun détecté
    }
}


# Configurations prédéfinies pour différents contextes
PRESET_CONFIGS = {
    'conseil': DEFAULT_CONFIG,  # Standards McKinsey/BCG

    'executive': {
        **DEFAULT_CONFIG,
        'max_words_per_slide': 30,
        'max_bullets_per_slide': 5,
        'max_slides_30min': 12,
        'minutes_per_slide': 2.5,
    },

    'technique': {
        **DEFAULT_CONFIG,
        'max_words_per_slide': 70,
        'max_bullets_per_slide': 10,
        'min_font_size': 12,
        'dense_slide_threshold': 60,
    },

    'commercial': {
        **DEFAULT_CONFIG,
        'max_words_per_slide': 40,
        'max_bullets_per_slide': 6,
        'min_font_size': 16,  # Plus lisible
    },

    'dsfr-strict': {
        **DEFAULT_CONFIG,
        'dsfr': {
            'enforce': True,
            'required_colors': ['#000091', '#E1000F', '#161616'],
            'required_logos': ['RF', 'ministere'],
            'min_contrast_ratio': 4.5,
            'required_font': 'Marianne'
        },
        'rgaa': {
            'level': 'AAA',
            'check_contrast': True,
            'check_alt_text': True,
            'check_color_only_info': True
        },
        'min_font_size': 14,
        'min_title_font_size': 18,
    }
}


def load_config(config_file: str = None, preset: str = None) -> Dict[str, Any]:
    """
    Charge la configuration depuis un fichier JSON, un preset, ou utilise la config par défaut.

    Args:
        config_file: Chemin vers un fichier JSON de configuration personnalisée
        preset: Nom d'un preset prédéfini ('conseil', 'executive', 'technique', 'commercial', 'dsfr-strict')

    Returns:
        Dictionnaire de configuration

    Exemples:
        >>> config = load_config()  # Config par défaut
        >>> config = load_config(preset='executive')  # Preset executive
        >>> config = load_config(config_file='custom.json')  # Config personnalisée
    """
    # Commencer avec la config par défaut
    config = DEFAULT_CONFIG.copy()

    # Appliquer un preset si spécifié
    if preset:
        if preset in PRESET_CONFIGS:
            preset_config = PRESET_CONFIGS[preset]
            config = _deep_merge(config, preset_config)
        else:
            available = ', '.join(PRESET_CONFIGS.keys())
            raise ValueError(f"Preset '{preset}' inconnu. Disponibles: {available}")

    # Charger et merger un fichier de config personnalisé
    if config_file:
        custom_config = _load_json_config(config_file)
        config = _deep_merge(config, custom_config)

    return config


def _load_json_config(config_file: str) -> Dict[str, Any]:
    """Charge un fichier JSON de configuration."""
    config_path = Path(config_file)

    if not config_path.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable: {config_file}")

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erreur de parsing JSON dans {config_file}: {e}")


def _deep_merge(base: Dict, overlay: Dict) -> Dict:
    """
    Merge récursif de deux dictionnaires.
    Les valeurs de 'overlay' écrasent celles de 'base'.
    """
    result = base.copy()

    for key, value in overlay.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value

    return result


def save_config(config: Dict[str, Any], output_file: str) -> None:
    """
    Sauvegarde une configuration dans un fichier JSON.

    Args:
        config: Dictionnaire de configuration
        output_file: Chemin du fichier de sortie

    Exemple:
        >>> config = load_config(preset='executive')
        >>> save_config(config, 'my-config.json')
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    print(f"✅ Configuration sauvegardée: {output_file}")


def print_config(config: Dict[str, Any]) -> None:
    """Affiche une configuration de manière lisible."""
    print("\n📋 Configuration Active\n")
    print("=" * 60)

    for section, values in config.items():
        if isinstance(values, dict):
            print(f"\n{section.upper()}:")
            for key, value in values.items():
                print(f"  {key}: {value}")
        else:
            print(f"{section}: {values}")

    print("=" * 60 + "\n")


# CLI pour tester la configuration
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Gestion de la configuration")
    parser.add_argument('--preset', '-p', choices=list(PRESET_CONFIGS.keys()),
                       help='Utiliser un preset prédéfini')
    parser.add_argument('--load', '-l', help='Charger une configuration depuis un fichier JSON')
    parser.add_argument('--save', '-s', help='Sauvegarder la configuration dans un fichier')
    parser.add_argument('--print', action='store_true', help='Afficher la configuration')

    args = parser.parse_args()

    try:
        config = load_config(config_file=args.load, preset=args.preset)

        if args.print:
            print_config(config)

        if args.save:
            save_config(config, args.save)

    except Exception as e:
        print(f"❌ Erreur: {e}")
        exit(1)
