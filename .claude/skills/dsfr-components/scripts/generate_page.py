#!/usr/bin/env python3
"""
Générateur de pages DSFR complètes
Créé des pages HTML avec la structure et les composants DSFR
"""

import argparse
from datetime import datetime

def generate_html_page(
    title: str = "Site officiel de l'État français",
    page_type: str = "standard",
    content: str = "",
    include_header: bool = True,
    include_footer: bool = True,
    dark_mode: bool = False
) -> str:
    """Génère une page HTML complète avec DSFR"""
    
    dark_scheme = 'data-fr-scheme="dark"' if dark_mode else ''
    
    header_html = generate_header() if include_header else ""
    footer_html = generate_footer() if include_footer else ""
    
    return f"""<!DOCTYPE html>
<html lang="fr" {dark_scheme}>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
    
    <!-- DSFR CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.11.2/dist/dsfr.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.11.2/dist/utility/icons/icons.min.css">
    
    <!-- Favicon -->
    <link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.11.2/dist/favicon/apple-touch-icon.png">
    <link rel="icon" href="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.11.2/dist/favicon/favicon.svg" type="image/svg+xml">
</head>
<body>
    {header_html}
    
    <main id="contenu">
        <div class="fr-container">
            {generate_page_content(page_type, content)}
        </div>
    </main>
    
    {footer_html}
    
    <!-- DSFR JS -->
    <script type="module" src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.11.2/dist/dsfr.module.min.js"></script>
    <script nomodule src="https://cdn.jsdelivr.net/npm/@gouvfr/dsfr@1.11.2/dist/dsfr.nomodule.min.js"></script>
</body>
</html>"""


def generate_header() -> str:
    """Génère l'en-tête DSFR"""
    return """
    <header role="banner" class="fr-header">
        <div class="fr-header__body">
            <div class="fr-container">
                <div class="fr-header__body-row">
                    <div class="fr-header__brand fr-enlarge-link">
                        <div class="fr-header__brand-top">
                            <div class="fr-header__logo">
                                <a href="/" title="Accueil - Nom du site">
                                    <p class="fr-logo">République<br>Française</p>
                                </a>
                            </div>
                            <div class="fr-header__operator">
                                <img src="/logo-operateur.svg" alt="Logo opérateur" style="height: 70px;">
                            </div>
                            <div class="fr-header__navbar">
                                <button class="fr-btn--search fr-btn" data-fr-opened="false" aria-controls="modal-search" title="Rechercher">
                                    Rechercher
                                </button>
                                <button class="fr-btn--menu fr-btn" data-fr-opened="false" aria-controls="modal-menu" aria-haspopup="menu" title="Menu">
                                    Menu
                                </button>
                            </div>
                        </div>
                        <div class="fr-header__service">
                            <a href="/" title="Accueil - Nom du site">
                                <p class="fr-header__service-title">Nom du service</p>
                            </a>
                            <p class="fr-header__service-tagline">Baseline - précisions sur l'organisation</p>
                        </div>
                    </div>
                    <div class="fr-header__tools">
                        <div class="fr-header__tools-links">
                            <ul class="fr-btns-group">
                                <li>
                                    <a class="fr-btn fr-btn--icon-left fr-icon-account-circle-line" href="/connexion">
                                        Se connecter
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="fr-header__menu fr-modal" id="modal-menu" aria-labelledby="button-menu">
            <div class="fr-container">
                <button class="fr-btn--close fr-btn" aria-controls="modal-menu" title="Fermer">
                    Fermer
                </button>
                <div class="fr-header__menu-links"></div>
                <nav class="fr-nav" id="navigation" role="navigation" aria-label="Menu principal">
                    <ul class="fr-nav__list">
                        <li class="fr-nav__item">
                            <a class="fr-nav__link" href="#" target="_self">Accueil</a>
                        </li>
                        <li class="fr-nav__item">
                            <a class="fr-nav__link" href="#" target="_self">Services</a>
                        </li>
                        <li class="fr-nav__item">
                            <a class="fr-nav__link" href="#" target="_self">Documentation</a>
                        </li>
                        <li class="fr-nav__item">
                            <a class="fr-nav__link" href="#" target="_self">Contact</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>"""


def generate_footer() -> str:
    """Génère le pied de page DSFR"""
    return """
    <footer class="fr-footer" role="contentinfo" id="footer">
        <div class="fr-container">
            <div class="fr-footer__body">
                <div class="fr-footer__brand fr-enlarge-link">
                    <a href="/" title="Accueil">
                        <p class="fr-logo">République<br>Française</p>
                    </a>
                </div>
                <div class="fr-footer__content">
                    <p class="fr-footer__content-desc">Description du service et de ses fonctionnalités</p>
                    <ul class="fr-footer__content-list">
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" target="_blank" href="https://legifrance.gouv.fr">legifrance.gouv.fr</a>
                        </li>
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" target="_blank" href="https://gouvernement.fr">gouvernement.fr</a>
                        </li>
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" target="_blank" href="https://service-public.fr">service-public.fr</a>
                        </li>
                        <li class="fr-footer__content-item">
                            <a class="fr-footer__content-link" target="_blank" href="https://data.gouv.fr">data.gouv.fr</a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="fr-footer__bottom">
                <ul class="fr-footer__bottom-list">
                    <li class="fr-footer__bottom-item">
                        <a class="fr-footer__bottom-link" href="/plan-du-site">Plan du site</a>
                    </li>
                    <li class="fr-footer__bottom-item">
                        <a class="fr-footer__bottom-link" href="/accessibilite">Accessibilité : non conforme</a>
                    </li>
                    <li class="fr-footer__bottom-item">
                        <a class="fr-footer__bottom-link" href="/mentions-legales">Mentions légales</a>
                    </li>
                    <li class="fr-footer__bottom-item">
                        <a class="fr-footer__bottom-link" href="/donnees-personnelles">Données personnelles</a>
                    </li>
                    <li class="fr-footer__bottom-item">
                        <a class="fr-footer__bottom-link" href="/gestion-des-cookies">Gestion des cookies</a>
                    </li>
                </ul>
                <div class="fr-footer__bottom-copy">
                    <p>Sauf mention contraire, tous les contenus de ce site sont sous <a href="https://github.com/etalab/licence-ouverte/blob/master/LO.md" target="_blank">licence etalab-2.0</a></p>
                </div>
            </div>
        </div>
    </footer>"""


def generate_page_content(page_type: str, custom_content: str = "") -> str:
    """Génère le contenu principal selon le type de page"""
    
    if page_type == "landing":
        return f"""
            <div class="fr-grid-row fr-grid-row--center fr-py-8w">
                <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                    <h1>Bienvenue sur notre service</h1>
                    <p class="fr-text--lead">Service numérique de l'État français pour simplifier vos démarches administratives.</p>
                    
                    <div class="fr-callout">
                        <h3 class="fr-callout__title">Information importante</h3>
                        <p class="fr-callout__text">Ce service est en phase de test. Vos retours nous aident à l'améliorer.</p>
                    </div>
                    
                    <div class="fr-grid-row fr-grid-row--gutters fr-mt-6w">
                        <div class="fr-col-12 fr-col-md-4">
                            <div class="fr-tile fr-tile--vertical">
                                <div class="fr-tile__body">
                                    <h4 class="fr-tile__title">
                                        <a href="#" class="fr-tile__link">Service 1</a>
                                    </h4>
                                    <p class="fr-tile__desc">Description du premier service</p>
                                </div>
                            </div>
                        </div>
                        <div class="fr-col-12 fr-col-md-4">
                            <div class="fr-tile fr-tile--vertical">
                                <div class="fr-tile__body">
                                    <h4 class="fr-tile__title">
                                        <a href="#" class="fr-tile__link">Service 2</a>
                                    </h4>
                                    <p class="fr-tile__desc">Description du deuxième service</p>
                                </div>
                            </div>
                        </div>
                        <div class="fr-col-12 fr-col-md-4">
                            <div class="fr-tile fr-tile--vertical">
                                <div class="fr-tile__body">
                                    <h4 class="fr-tile__title">
                                        <a href="#" class="fr-tile__link">Service 3</a>
                                    </h4>
                                    <p class="fr-tile__desc">Description du troisième service</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    {custom_content}
                </div>
            </div>"""
    
    elif page_type == "form":
        return f"""
            <div class="fr-grid-row fr-grid-row--center fr-py-8w">
                <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                    <h1>Formulaire de contact</h1>
                    
                    <form action="/submit" method="post">
                        <fieldset class="fr-fieldset">
                            <legend class="fr-fieldset__legend">Vos informations</legend>
                            
                            <div class="fr-input-group">
                                <label class="fr-label" for="nom">Nom
                                    <span class="fr-hint-text">Format : Nom de famille</span>
                                </label>
                                <input class="fr-input" type="text" id="nom" name="nom" required>
                            </div>
                            
                            <div class="fr-input-group">
                                <label class="fr-label" for="prenom">Prénom</label>
                                <input class="fr-input" type="text" id="prenom" name="prenom" required>
                            </div>
                            
                            <div class="fr-input-group">
                                <label class="fr-label" for="email">Adresse électronique
                                    <span class="fr-hint-text">Format : nom@domaine.fr</span>
                                </label>
                                <input class="fr-input" type="email" id="email" name="email" required>
                            </div>
                            
                            <div class="fr-input-group">
                                <label class="fr-label" for="message">Message</label>
                                <textarea class="fr-input" id="message" name="message" rows="5" required></textarea>
                            </div>
                            
                            <div class="fr-checkbox-group">
                                <input type="checkbox" id="conditions" name="conditions" required>
                                <label class="fr-label" for="conditions">
                                    J'accepte les conditions générales d'utilisation
                                </label>
                            </div>
                        </fieldset>
                        
                        <div class="fr-btns-group fr-btns-group--right">
                            <button class="fr-btn" type="submit">
                                Envoyer
                            </button>
                            <button class="fr-btn fr-btn--secondary" type="reset">
                                Annuler
                            </button>
                        </div>
                    </form>
                    {custom_content}
                </div>
            </div>"""
    
    elif page_type == "dashboard":
        return f"""
            <div class="fr-py-8w">
                <h1>Tableau de bord</h1>
                
                <div class="fr-tabs">
                    <ul class="fr-tabs__list" role="tablist" aria-label="Navigation par onglets">
                        <li role="presentation">
                            <button id="tabpanel-1" class="fr-tabs__tab" tabindex="0" role="tab" aria-selected="true" aria-controls="tabpanel-1-panel">Vue d'ensemble</button>
                        </li>
                        <li role="presentation">
                            <button id="tabpanel-2" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tabpanel-2-panel">Statistiques</button>
                        </li>
                        <li role="presentation">
                            <button id="tabpanel-3" class="fr-tabs__tab" tabindex="-1" role="tab" aria-selected="false" aria-controls="tabpanel-3-panel">Paramètres</button>
                        </li>
                    </ul>
                    <div id="tabpanel-1-panel" class="fr-tabs__panel fr-tabs__panel--selected" role="tabpanel" aria-labelledby="tabpanel-1" tabindex="0">
                        <div class="fr-grid-row fr-grid-row--gutters">
                            <div class="fr-col-12 fr-col-md-3">
                                <div class="fr-callout">
                                    <p class="fr-callout__text">
                                        <span class="fr-text--bold fr-text--lg">1 234</span><br>
                                        Utilisateurs actifs
                                    </p>
                                </div>
                            </div>
                            <div class="fr-col-12 fr-col-md-3">
                                <div class="fr-callout">
                                    <p class="fr-callout__text">
                                        <span class="fr-text--bold fr-text--lg">567</span><br>
                                        Nouveaux cette semaine
                                    </p>
                                </div>
                            </div>
                            <div class="fr-col-12 fr-col-md-3">
                                <div class="fr-callout">
                                    <p class="fr-callout__text">
                                        <span class="fr-text--bold fr-text--lg">89%</span><br>
                                        Taux de satisfaction
                                    </p>
                                </div>
                            </div>
                            <div class="fr-col-12 fr-col-md-3">
                                <div class="fr-callout">
                                    <p class="fr-callout__text">
                                        <span class="fr-text--bold fr-text--lg">12</span><br>
                                        Tickets en attente
                                    </p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="fr-table fr-mt-6w">
                            <table>
                                <caption>Dernières activités</caption>
                                <thead>
                                    <tr>
                                        <th scope="col">Date</th>
                                        <th scope="col">Utilisateur</th>
                                        <th scope="col">Action</th>
                                        <th scope="col">Statut</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>20/10/2025</td>
                                        <td>Jean Dupont</td>
                                        <td>Création de compte</td>
                                        <td><span class="fr-badge fr-badge--success">Succès</span></td>
                                    </tr>
                                    <tr>
                                        <td>20/10/2025</td>
                                        <td>Marie Martin</td>
                                        <td>Modification profil</td>
                                        <td><span class="fr-badge fr-badge--success">Succès</span></td>
                                    </tr>
                                    <tr>
                                        <td>19/10/2025</td>
                                        <td>Pierre Durand</td>
                                        <td>Tentative connexion</td>
                                        <td><span class="fr-badge fr-badge--error">Échec</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                {custom_content}
            </div>"""
    
    else:  # Standard page
        return f"""
            <div class="fr-grid-row fr-grid-row--center fr-py-8w">
                <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
                    <h1>Titre de la page</h1>
                    <p class="fr-text--lead">Introduction ou résumé du contenu de la page.</p>
                    
                    <h2>Section principale</h2>
                    <p>Contenu de la section principale avec tous les détails nécessaires.</p>
                    
                    <h3>Sous-section</h3>
                    <p>Détails supplémentaires organisés en sous-sections pour une meilleure lisibilité.</p>
                    
                    {custom_content if custom_content else '<p>Ajoutez votre contenu personnalisé ici.</p>'}
                </div>
            </div>"""


def main():
    parser = argparse.ArgumentParser(description="Générateur de pages DSFR")
    parser.add_argument("--title", default="Site officiel", help="Titre de la page")
    parser.add_argument("--type", default="standard", 
                       choices=["standard", "landing", "form", "dashboard"],
                       help="Type de page à générer")
    parser.add_argument("--content", default="", help="Contenu HTML personnalisé à insérer")
    parser.add_argument("--no-header", action="store_true", help="Exclure l'en-tête")
    parser.add_argument("--no-footer", action="store_true", help="Exclure le pied de page")
    parser.add_argument("--dark", action="store_true", help="Activer le mode sombre")
    parser.add_argument("--output", help="Fichier de sortie")
    
    args = parser.parse_args()
    
    html = generate_html_page(
        title=args.title,
        page_type=args.type,
        content=args.content,
        include_header=not args.no_header,
        include_footer=not args.no_footer,
        dark_mode=args.dark
    )
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Page générée : {args.output}")
    else:
        print(html)


if __name__ == "__main__":
    main()
