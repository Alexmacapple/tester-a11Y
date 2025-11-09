# Classes utilitaires DSFR

## Table des matières
- [Système de grille](#système-de-grille)
- [Espacements](#espacements)
- [Typographie](#typographie)
- [Couleurs](#couleurs)
- [Affichage](#affichage)
- [Icônes](#icônes)
- [Accessibilité](#accessibilité)

## Système de grille

### Container
- `fr-container` : Container centré avec marges latérales
- `fr-container--fluid` : Container pleine largeur
- `fr-container-sm` : Container petit (max 576px)
- `fr-container-md` : Container moyen (max 768px)
- `fr-container-lg` : Container large (max 992px)
- `fr-container-xl` : Container extra large (max 1248px)

### Lignes
- `fr-grid-row` : Ligne de la grille
- `fr-grid-row--gutters` : Ligne avec gouttières entre colonnes
- `fr-grid-row--no-gutters` : Ligne sans gouttières
- `fr-grid-row--center` : Ligne centrée horizontalement
- `fr-grid-row--right` : Ligne alignée à droite
- `fr-grid-row--middle` : Ligne centrée verticalement
- `fr-grid-row--bottom` : Ligne alignée en bas

### Colonnes
- `fr-col` : Colonne flexible
- `fr-col-1` à `fr-col-12` : Colonnes de largeur fixe (1/12 à 12/12)
- `fr-col-sm-*` : Colonnes pour écrans small (≥576px)
- `fr-col-md-*` : Colonnes pour écrans medium (≥768px)
- `fr-col-lg-*` : Colonnes pour écrans large (≥992px)
- `fr-col-xl-*` : Colonnes pour écrans extra large (≥1248px)

### Décalages
- `fr-col-offset-*` : Décalage de colonne (1 à 11)
- `fr-col-sm-offset-*` : Décalage pour écrans small
- `fr-col-md-offset-*` : Décalage pour écrans medium
- `fr-col-lg-offset-*` : Décalage pour écrans large
- `fr-col-xl-offset-*` : Décalage pour écrans extra large

## Espacements

### Marges (margin)
#### Toutes directions
- `fr-m-*` : Marge sur tous les côtés
  - Valeurs : 0, 1v, 1w, 2v, 2w, 3v, 3w, 4w, 5w, 6w, 7w, 8w, 9w, 10w, 12w, 15w

#### Horizontales
- `fr-mx-*` : Marges gauche et droite
- `fr-ml-*` : Marge gauche uniquement
- `fr-mr-*` : Marge droite uniquement

#### Verticales
- `fr-my-*` : Marges haut et bas
- `fr-mt-*` : Marge haut uniquement
- `fr-mb-*` : Marge bas uniquement

### Paddings (padding)
#### Toutes directions
- `fr-p-*` : Padding sur tous les côtés
  - Valeurs identiques aux marges

#### Horizontales
- `fr-px-*` : Paddings gauche et droite
- `fr-pl-*` : Padding gauche uniquement
- `fr-pr-*` : Padding droite uniquement

#### Verticales
- `fr-py-*` : Paddings haut et bas
- `fr-pt-*` : Padding haut uniquement
- `fr-pb-*` : Padding bas uniquement

### Valeurs spéciales
- `*-0` : Aucun espacement
- `*-1v` : 0.25rem
- `*-1w` : 0.5rem
- `*-2w` : 1rem
- `*-3w` : 1.5rem
- `*-4w` : 2rem
- `*-5w` : 2.5rem
- `*-6w` : 3rem
- `*-7w` : 3.5rem
- `*-8w` : 4rem

## Typographie

### Tailles de texte
- `fr-text--xs` : Très petit (0.75rem)
- `fr-text--sm` : Petit (0.875rem)
- `fr-text--md` : Moyen (1rem) - par défaut
- `fr-text--lg` : Grand (1.125rem)
- `fr-text--xl` : Très grand (1.25rem)
- `fr-text--lead` : Texte d'introduction (1.25rem avec line-height augmenté)

### Poids de texte
- `fr-text--light` : Léger (300)
- `fr-text--regular` : Normal (400) - par défaut
- `fr-text--bold` : Gras (700)

### Alignement
- `fr-text--left` : Aligné à gauche
- `fr-text--center` : Centré
- `fr-text--right` : Aligné à droite
- `fr-text--justify` : Justifié

### Transformation
- `fr-text--uppercase` : Majuscules
- `fr-text--lowercase` : Minuscules
- `fr-text--capitalize` : Première lettre en majuscule

### Décoration
- `fr-text--underline` : Souligné
- `fr-text--no-underline` : Sans soulignement
- `fr-text--line-through` : Barré

### Styles de liste
- `fr-list--no-marker` : Liste sans puces/numéros

## Couleurs

### Couleurs de texte
- `fr-text--default-grey` : Gris par défaut
- `fr-text--action-high-blue-france` : Bleu France
- `fr-text--action-high-red-marianne` : Rouge Marianne
- `fr-text--info` : Bleu info
- `fr-text--success` : Vert succès
- `fr-text--warning` : Orange avertissement
- `fr-text--error` : Rouge erreur

### Couleurs de fond
- `fr-background--default-grey` : Fond gris
- `fr-background--contrast-grey` : Fond gris contrasté
- `fr-background--alt-grey` : Fond gris alternatif
- `fr-background--action-low-blue-france` : Fond bleu France clair
- `fr-background--action-low-red-marianne` : Fond rouge Marianne clair

### Bordures
- `fr-border` : Bordure standard
- `fr-border--top` : Bordure haute uniquement
- `fr-border--right` : Bordure droite uniquement
- `fr-border--bottom` : Bordure basse uniquement
- `fr-border--left` : Bordure gauche uniquement

## Affichage

### Display
- `fr-display--none` : Masqué
- `fr-display--inline` : En ligne
- `fr-display--inline-block` : En ligne bloc
- `fr-display--block` : Bloc
- `fr-display--table` : Table
- `fr-display--table-cell` : Cellule de table
- `fr-display--flex` : Flexbox
- `fr-display--inline-flex` : Flexbox en ligne

### Visibilité responsive
- `fr-hidden` : Toujours masqué
- `fr-hidden-sm` : Masqué sur small et plus
- `fr-hidden-md` : Masqué sur medium et plus
- `fr-hidden-lg` : Masqué sur large et plus
- `fr-hidden-xl` : Masqué sur extra large

### Visibilité par breakpoint
- `fr-unhidden-sm` : Visible sur small et plus
- `fr-unhidden-md` : Visible sur medium et plus
- `fr-unhidden-lg` : Visible sur large et plus
- `fr-unhidden-xl` : Visible sur extra large

## Icônes

### Icônes système
Format : `fr-icon-[nom]-[style]`

Styles disponibles :
- `-line` : Contour (par défaut)
- `-fill` : Rempli

### Icônes courantes
- `fr-icon-arrow-right-line` : Flèche droite
- `fr-icon-arrow-left-line` : Flèche gauche
- `fr-icon-arrow-up-line` : Flèche haut
- `fr-icon-arrow-down-line` : Flèche bas
- `fr-icon-check-line` : Validation
- `fr-icon-close-line` : Fermeture
- `fr-icon-error-line` : Erreur
- `fr-icon-info-line` : Information
- `fr-icon-warning-line` : Avertissement
- `fr-icon-search-line` : Recherche
- `fr-icon-menu-line` : Menu
- `fr-icon-user-line` : Utilisateur
- `fr-icon-account-circle-line` : Compte
- `fr-icon-lock-line` : Verrouillé
- `fr-icon-mail-line` : Email
- `fr-icon-phone-line` : Téléphone
- `fr-icon-calendar-line` : Calendrier
- `fr-icon-time-line` : Heure
- `fr-icon-download-line` : Téléchargement
- `fr-icon-upload-line` : Téléversement
- `fr-icon-external-link-line` : Lien externe
- `fr-icon-file-line` : Fichier
- `fr-icon-folder-line` : Dossier

### Utilisation dans les boutons
```html
<button class="fr-btn fr-btn--icon-left fr-icon-arrow-left-line">
    Retour
</button>
<button class="fr-btn fr-btn--icon-right fr-icon-arrow-right-line">
    Suivant
</button>
```

## Accessibilité

### Classes d'assistance
- `fr-sr-only` : Visible uniquement par les lecteurs d'écran
- `fr-sr-only-focusable` : Visible au focus uniquement
- `fr-link--no-underline` : Lien sans soulignement
- `fr-enlarge-link` : Zone cliquable étendue
- `fr-responsive-vid` : Vidéo responsive
- `fr-responsive-img` : Image responsive

### Attributs ARIA importants
- `role="navigation"` : Pour les éléments de navigation
- `role="search"` : Pour les formulaires de recherche
- `role="main"` : Pour le contenu principal
- `role="complementary"` : Pour les contenus complémentaires
- `role="alert"` : Pour les messages d'alerte
- `aria-label` : Label pour les éléments sans texte visible
- `aria-labelledby` : Référence à un élément servant de label
- `aria-describedby` : Référence à un élément de description
- `aria-current="page"` : Page courante dans la navigation
- `aria-expanded` : État ouvert/fermé
- `aria-controls` : Élément contrôlé
- `aria-hidden="true"` : Masqué aux lecteurs d'écran

### Focus et navigation clavier
- Tous les éléments interactifs doivent être accessibles au clavier
- L'ordre de tabulation doit être logique
- Le focus doit être visible
- Les raccourcis clavier ne doivent pas entrer en conflit avec ceux du système

### Contrastes
Le DSFR respecte les normes WCAG AA :
- Contraste minimum de 4.5:1 pour le texte normal
- Contraste minimum de 3:1 pour le texte large
- Contraste minimum de 3:1 pour les éléments d'interface
