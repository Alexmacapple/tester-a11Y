#!/usr/bin/env python3
"""
Générateur de composants DSFR
Créé des composants conformes au Design System de l'État Français
"""

import argparse
import json
from typing import Dict, Any

def generate_button(variant: str = "primary", size: str = "md", icon: str = None, disabled: bool = False) -> str:
    """Génère un bouton DSFR"""
    classes = ["fr-btn"]
    
    # Variantes
    if variant == "secondary":
        classes.append("fr-btn--secondary")
    elif variant == "tertiary":
        classes.append("fr-btn--tertiary")
    elif variant == "tertiary-no-outline":
        classes.append("fr-btn--tertiary-no-outline")
    
    # Tailles
    if size == "sm":
        classes.append("fr-btn--sm")
    elif size == "lg":
        classes.append("fr-btn--lg")
    
    # Icône
    if icon:
        classes.append(f"fr-btn--icon-{icon}")
    
    disabled_attr = 'disabled aria-disabled="true"' if disabled else ''
    
    return f'<button class="{" ".join(classes)}" {disabled_attr}>Libellé bouton</button>'


def generate_alert(type: str = "info", title: str = "", description: str = "", closable: bool = False) -> str:
    """Génère une alerte DSFR"""
    alert_class = f"fr-alert fr-alert--{type}"
    
    close_button = """
    <button class="fr-btn--close fr-btn" title="Masquer le message" onclick="const alert = this.parentNode; alert.parentNode.removeChild(alert); return false;">
        Masquer le message
    </button>""" if closable else ""
    
    return f"""
<div class="{alert_class}" role="alert">
    <h3 class="fr-alert__title">{title or 'Titre de l\'alerte'}</h3>
    <p>{description or 'Description de l\'alerte'}</p>
    {close_button}
</div>"""


def generate_accordion(items: list) -> str:
    """Génère un accordéon DSFR"""
    accordion_html = '<div class="fr-accordions-group">\n'
    
    for i, item in enumerate(items):
        accordion_html += f"""
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-{i}">
                {item.get('title', f'Titre {i+1}')}
            </button>
        </h3>
        <div class="fr-collapse" id="accordion-{i}">
            <p>{item.get('content', 'Contenu de l\'accordéon')}</p>
        </div>
    </section>"""
    
    accordion_html += '\n</div>'
    return accordion_html


def generate_card(title: str = "", description: str = "", image: str = None, link: str = "#") -> str:
    """Génère une carte DSFR"""
    image_html = f"""
    <div class="fr-card__img">
        <img src="{image}" alt="" />
    </div>""" if image else ""
    
    return f"""
<div class="fr-card fr-card--horizontal">
    {image_html}
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="{link}">{title or 'Titre de la carte'}</a>
            </h3>
            <p class="fr-card__desc">{description or 'Description de la carte'}</p>
        </div>
    </div>
</div>"""


def generate_modal(title: str = "", content: str = "") -> str:
    """Génère une modale DSFR"""
    return f"""
<dialog id="fr-modal" class="fr-modal" role="dialog" aria-labelledby="fr-modal-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button class="fr-btn--close fr-btn" title="Fermer" aria-controls="fr-modal">Fermer</button>
                    </div>
                    <div class="fr-modal__content">
                        <h1 id="fr-modal-title" class="fr-modal__title">{title or 'Titre de la modale'}</h1>
                        <p>{content or 'Contenu de la modale'}</p>
                    </div>
                    <div class="fr-modal__footer">
                        <button class="fr-btn">Action principale</button>
                        <button class="fr-btn fr-btn--secondary">Action secondaire</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>"""


def generate_form_input(label: str, type: str = "text", required: bool = False, hint: str = None, error: str = None) -> str:
    """Génère un champ de formulaire DSFR"""
    input_id = label.lower().replace(" ", "-")
    required_attr = 'required aria-required="true"' if required else ''
    error_class = ' fr-input-group--error' if error else ''
    
    hint_html = f'<span class="fr-hint-text">{hint}</span>' if hint else ''
    error_html = f'<p id="{input_id}-error" class="fr-error-text">{error}</p>' if error else ''
    
    return f"""
<div class="fr-input-group{error_class}">
    <label class="fr-label" for="{input_id}">
        {label}
        {hint_html}
    </label>
    <input class="fr-input" type="{type}" id="{input_id}" name="{input_id}" {required_attr} />
    {error_html}
</div>"""


def generate_breadcrumb(items: list) -> str:
    """Génère un fil d'Ariane DSFR"""
    breadcrumb_html = """
<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb">Voir le fil d'Ariane</button>
    <div class="fr-collapse" id="breadcrumb">
        <ol class="fr-breadcrumb__list">"""
    
    for i, item in enumerate(items[:-1]):
        breadcrumb_html += f"""
            <li>
                <a class="fr-breadcrumb__link" href="{item.get('url', '#')}">{item.get('label', f'Niveau {i+1}')}</a>
            </li>"""
    
    # Dernier élément (page courante)
    if items:
        breadcrumb_html += f"""
            <li>
                <a class="fr-breadcrumb__link" aria-current="page">{items[-1].get('label', 'Page courante')}</a>
            </li>"""
    
    breadcrumb_html += """
        </ol>
    </div>
</nav>"""
    return breadcrumb_html


def main():
    parser = argparse.ArgumentParser(description="Générateur de composants DSFR")
    parser.add_argument("component", help="Type de composant à générer", 
                       choices=["button", "alert", "accordion", "card", "modal", "input", "breadcrumb"])
    parser.add_argument("--config", help="Configuration JSON du composant", type=str)
    
    args = parser.parse_args()
    
    config = json.loads(args.config) if args.config else {}
    
    generators = {
        "button": lambda: generate_button(**config),
        "alert": lambda: generate_alert(**config),
        "accordion": lambda: generate_accordion(config.get("items", [])),
        "card": lambda: generate_card(**config),
        "modal": lambda: generate_modal(**config),
        "input": lambda: generate_form_input(config.get("label", "Label"), **{k: v for k, v in config.items() if k != "label"}),
        "breadcrumb": lambda: generate_breadcrumb(config.get("items", []))
    }
    
    print(generators[args.component]())


if __name__ == "__main__":
    main()
