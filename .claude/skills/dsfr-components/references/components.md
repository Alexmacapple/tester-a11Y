# Référence des composants DSFR

## Table des matières
- [Boutons](#boutons)
- [Alertes](#alertes)
- [Formulaires](#formulaires)
- [Navigation](#navigation)
- [Cartes](#cartes)
- [Modales](#modales)
- [Tableaux](#tableaux)
- [Badges](#badges)
- [Accordéons](#accordéons)
- [Onglets](#onglets)

## Boutons

### Variantes principales
- `fr-btn` : Bouton principal (fond bleu)
- `fr-btn fr-btn--secondary` : Bouton secondaire (contour bleu)
- `fr-btn fr-btn--tertiary` : Bouton tertiaire (sans contour)
- `fr-btn fr-btn--tertiary-no-outline` : Bouton tertiaire sans bordure

### Tailles
- `fr-btn--sm` : Petit
- Par défaut : Moyen
- `fr-btn--lg` : Grand

### Icônes
- `fr-btn--icon-left fr-icon-[nom]` : Icône à gauche
- `fr-btn--icon-right fr-icon-[nom]` : Icône à droite

### États
- `disabled` : Bouton désactivé
- `aria-pressed="true"` : Bouton activé (toggle)

## Alertes

### Types d'alertes
- `fr-alert--info` : Information (bleu)
- `fr-alert--success` : Succès (vert)
- `fr-alert--warning` : Avertissement (orange)
- `fr-alert--error` : Erreur (rouge)

### Structure
```html
<div class="fr-alert fr-alert--[type]" role="alert">
    <h3 class="fr-alert__title">Titre</h3>
    <p>Description de l'alerte</p>
</div>
```

## Formulaires

### Champs de texte
```html
<div class="fr-input-group">
    <label class="fr-label" for="input-id">
        Label du champ
        <span class="fr-hint-text">Texte d'aide</span>
    </label>
    <input class="fr-input" type="text" id="input-id" name="input-name">
</div>
```

### Champs avec erreur
```html
<div class="fr-input-group fr-input-group--error">
    <label class="fr-label" for="input-id">Label</label>
    <input class="fr-input" type="text" id="input-id" aria-describedby="input-id-error">
    <p id="input-id-error" class="fr-error-text">Message d'erreur</p>
</div>
```

### Cases à cocher
```html
<div class="fr-checkbox-group">
    <input type="checkbox" id="checkbox-1" name="checkbox-1">
    <label class="fr-label" for="checkbox-1">Option 1</label>
</div>
```

### Boutons radio
```html
<div class="fr-radio-group">
    <input type="radio" id="radio-1" name="radio-group" value="1">
    <label class="fr-label" for="radio-1">Option 1</label>
</div>
```

### Sélecteur
```html
<div class="fr-select-group">
    <label class="fr-label" for="select">Label du sélecteur</label>
    <select class="fr-select" id="select" name="select">
        <option value="">Sélectionner une option</option>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
    </select>
</div>
```

## Navigation

### Fil d'Ariane
```html
<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb">
        Voir le fil d'Ariane
    </button>
    <div class="fr-collapse" id="breadcrumb">
        <ol class="fr-breadcrumb__list">
            <li><a class="fr-breadcrumb__link" href="#">Accueil</a></li>
            <li><a class="fr-breadcrumb__link" href="#">Niveau 1</a></li>
            <li><a class="fr-breadcrumb__link" aria-current="page">Page courante</a></li>
        </ol>
    </div>
</nav>
```

### Menu de navigation
```html
<nav class="fr-nav" role="navigation" aria-label="Menu principal">
    <ul class="fr-nav__list">
        <li class="fr-nav__item">
            <button class="fr-nav__btn" aria-expanded="false" aria-controls="nav-1">
                Menu avec sous-menu
            </button>
            <div class="fr-collapse" id="nav-1">
                <ul class="fr-menu__list">
                    <li><a class="fr-nav__link" href="#">Sous-item 1</a></li>
                    <li><a class="fr-nav__link" href="#">Sous-item 2</a></li>
                </ul>
            </div>
        </li>
        <li class="fr-nav__item">
            <a class="fr-nav__link" href="#">Lien simple</a>
        </li>
    </ul>
</nav>
```

### Pagination
```html
<nav role="navigation" class="fr-pagination" aria-label="Pagination">
    <ul class="fr-pagination__list">
        <li>
            <a class="fr-pagination__link fr-pagination__link--first" href="#">
                Première page
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--prev" href="#">
                Page précédente
            </a>
        </li>
        <li><a class="fr-pagination__link" href="#" aria-current="page">1</a></li>
        <li><a class="fr-pagination__link" href="#">2</a></li>
        <li><a class="fr-pagination__link" href="#">3</a></li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--next" href="#">
                Page suivante
            </a>
        </li>
        <li>
            <a class="fr-pagination__link fr-pagination__link--last" href="#">
                Dernière page
            </a>
        </li>
    </ul>
</nav>
```

## Cartes

### Carte standard
```html
<div class="fr-card">
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Titre de la carte</a>
            </h3>
            <p class="fr-card__desc">Description de la carte</p>
            <div class="fr-card__start">
                <p class="fr-card__detail">Détail</p>
            </div>
        </div>
    </div>
    <div class="fr-card__header">
        <div class="fr-card__img">
            <img src="image.jpg" alt="">
        </div>
    </div>
</div>
```

### Carte horizontale
```html
<div class="fr-card fr-card--horizontal">
    <div class="fr-card__img">
        <img src="image.jpg" alt="">
    </div>
    <div class="fr-card__body">
        <div class="fr-card__content">
            <h3 class="fr-card__title">
                <a href="#">Titre</a>
            </h3>
            <p class="fr-card__desc">Description</p>
        </div>
    </div>
</div>
```

## Modales

### Structure de base
```html
<dialog id="modal-1" class="fr-modal" role="dialog" aria-labelledby="modal-1-title">
    <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
            <div class="fr-col-12 fr-col-md-8 fr-col-lg-6">
                <div class="fr-modal__body">
                    <div class="fr-modal__header">
                        <button class="fr-btn--close fr-btn" aria-controls="modal-1">
                            Fermer
                        </button>
                    </div>
                    <div class="fr-modal__content">
                        <h1 id="modal-1-title" class="fr-modal__title">
                            Titre de la modale
                        </h1>
                        <p>Contenu de la modale</p>
                    </div>
                    <div class="fr-modal__footer">
                        <button class="fr-btn">Action principale</button>
                        <button class="fr-btn fr-btn--secondary">Action secondaire</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### Ouverture de modale
```html
<button class="fr-btn" data-fr-opened="false" aria-controls="modal-1">
    Ouvrir la modale
</button>
```

## Tableaux

### Tableau simple
```html
<div class="fr-table">
    <table>
        <caption>Titre du tableau</caption>
        <thead>
            <tr>
                <th scope="col">En-tête 1</th>
                <th scope="col">En-tête 2</th>
                <th scope="col">En-tête 3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Donnée 1</td>
                <td>Donnée 2</td>
                <td>Donnée 3</td>
            </tr>
        </tbody>
    </table>
</div>
```

### Tableau avec défilement horizontal
```html
<div class="fr-table fr-table--no-scroll">
    <div class="fr-table__wrapper">
        <div class="fr-table__container">
            <div class="fr-table__content">
                <table>
                    <!-- Contenu du tableau -->
                </table>
            </div>
        </div>
    </div>
</div>
```

## Badges

### Types de badges
- `fr-badge` : Badge standard (gris)
- `fr-badge fr-badge--info` : Information (bleu)
- `fr-badge fr-badge--success` : Succès (vert)
- `fr-badge fr-badge--warning` : Avertissement (orange)
- `fr-badge fr-badge--error` : Erreur (rouge)
- `fr-badge fr-badge--new` : Nouveau (vert menthe)

### Tailles
- `fr-badge--sm` : Petit
- Par défaut : Moyen

### Badges avec icônes
```html
<span class="fr-badge fr-badge--success fr-badge--icon-left">
    <span class="fr-icon-check-line" aria-hidden="true"></span>
    Validé
</span>
```

## Accordéons

### Structure
```html
<div class="fr-accordions-group">
    <section class="fr-accordion">
        <h3 class="fr-accordion__title">
            <button class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-1">
                Titre de l'accordéon
            </button>
        </h3>
        <div class="fr-collapse" id="accordion-1">
            <p>Contenu de l'accordéon</p>
        </div>
    </section>
</div>
```

## Onglets

### Structure
```html
<div class="fr-tabs">
    <ul class="fr-tabs__list" role="tablist" aria-label="Navigation par onglets">
        <li role="presentation">
            <button id="tab-1" class="fr-tabs__tab" tabindex="0" role="tab" 
                    aria-selected="true" aria-controls="tabpanel-1">
                Onglet 1
            </button>
        </li>
        <li role="presentation">
            <button id="tab-2" class="fr-tabs__tab" tabindex="-1" role="tab" 
                    aria-selected="false" aria-controls="tabpanel-2">
                Onglet 2
            </button>
        </li>
    </ul>
    <div id="tabpanel-1" class="fr-tabs__panel fr-tabs__panel--selected" 
         role="tabpanel" aria-labelledby="tab-1" tabindex="0">
        <p>Contenu onglet 1</p>
    </div>
    <div id="tabpanel-2" class="fr-tabs__panel" 
         role="tabpanel" aria-labelledby="tab-2" tabindex="0">
        <p>Contenu onglet 2</p>
    </div>
</div>
```
