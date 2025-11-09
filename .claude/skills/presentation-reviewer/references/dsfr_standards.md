# Standards DSFR pour Présentations PowerPoint
## Design Système de l'État Français

Ce document détaille les standards à respecter pour créer des présentations PowerPoint conformes au Design Système de l'État Français (DSFR) et aux exigences d'accessibilité.

---

## 1. Palette de Couleurs DSFR

### Couleurs Principales

**Bleu France** (couleur principale de l'État)
- Hex: `#000091`
- RGB: (0, 0, 145)
- Usage: Titres principaux, éléments d'accentuation, boutons

**Rouge Marianne** (couleur secondaire)
- Hex: `#E1000F`
- RGB: (225, 0, 15)
- Usage: Alertes, points importants, accentuation

**Gris DSFR**
- Gris 1000 (texte principal): `#161616`
- Gris 800: `#383838`
- Gris 200 (fond clair): `#E5E5E5`
- Gris 50 (fond très clair): `#F6F6F6`

### Couleurs Fonctionnelles

**Succès**
- Vert succès: `#18753C`
- Vert succès (hover): `#0D5C2E`

**Information**
- Bleu info: `#0063CB`
- Bleu info (hover): `#004F9F`

**Attention**
- Orange attention: `#FC5D00`
- Orange attention (hover): `#C74600`

**Erreur**
- Rouge erreur: `#CE0500`
- Rouge erreur (hover): `#9F0400`

### Règles d'Usage des Couleurs

1. **Ratio de contraste**
   - Texte sur fond: minimum 4.5:1
   - Grands textes (≥18pt): minimum 3:1
   - Éléments graphiques: minimum 3:1

2. **Pas d'information par la couleur seule**
   - Toujours doubler avec forme, texte ou icône
   - Exemple: graphique avec motifs en plus des couleurs

3. **Hiérarchie visuelle**
   - Bleu France: éléments principaux
   - Gris foncé: texte courant
   - Couleurs fonctionnelles: états et messages

---

## 2. Typographie Marianne

### Police Officielle

**Marianne** est la police officielle du DSFR
- Marianne Regular: texte courant
- Marianne Bold: titres et emphase
- Marianne Medium: sous-titres

### Si Marianne n'est pas disponible

**Alternatives de secours (fallback):**
1. Arial (largement disponible)
2. Helvetica
3. Sans-serif système

### Hiérarchie Typographique

**Titre de présentation**
- Police: Marianne Bold
- Taille: 32-36pt
- Couleur: Bleu France (#000091)

**Titres de slides**
- Police: Marianne Bold
- Taille: 24-28pt
- Couleur: Gris 1000 (#161616) ou Bleu France

**Sous-titres**
- Police: Marianne Medium
- Taille: 18-20pt
- Couleur: Gris 800 (#383838)

**Texte principal**
- Police: Marianne Regular
- Taille: 14-16pt
- Couleur: Gris 1000 (#161616)
- Interligne: 1.5

**Notes et légendes**
- Police: Marianne Regular
- Taille: 10-12pt
- Couleur: Gris 800 (#383838)

### Règles Typographiques

1. **Pas de texte tout en majuscules** (sauf acronymes)
2. **Gras avec parcimonie** (titres et mots-clés seulement)
3. **Pas d'italique** sauf citations
4. **Éviter le souligné** (réservé aux liens web)
5. **Alignement à gauche** pour le texte (pas de justification)

---

## 3. Mise en Page et Structure

### Format Standard
- Format: 16:9 (1920×1080px ou 1280×720px)
- Alternative: 4:3 si projecteur ancien

### Marges et Grille

**Marges recommandées**
- Haut: 80px
- Bas: 80px (120px avec pied de page)
- Gauche: 100px
- Droite: 100px

**Grille de colonnes**
- Système de grille à 12 colonnes
- Gouttière: 20px
- Permet alignement cohérent

### Zones de la Slide

```
┌──────────────────────────────────────┐
│ [Logo]            Titre        [Date] │ ← En-tête (80px)
├──────────────────────────────────────┤
│                                      │
│                                      │
│         Contenu Principal            │
│                                      │
│                                      │
├──────────────────────────────────────┤
│ Ministère | Source | Page 1/10       │ ← Pied de page (120px)
└──────────────────────────────────────┘
```

### Slide de Titre

**Éléments obligatoires:**
- Titre de la présentation (centré, Marianne Bold 36pt)
- Logo République Française (en haut à gauche)
- Logo ministère/organisation (en haut à droite)
- Date et lieu (centré, sous le titre)
- Auteur(s) si pertinent

### Slides de Contenu

**Structure recommandée:**
- Titre de slide (aligné à gauche, en haut)
- Contenu dans la zone centrale
- Source des données (pied de page, petite taille)
- Numérotation (pied de page, droite)

---

## 4. Logos et Identité Visuelle

### Logo République Française

**Usage obligatoire pour:**
- Communications officielles de l'État
- Présentations gouvernementales
- Documents administratifs

**Spécifications:**
- Position: En haut à gauche
- Taille: hauteur 60-80px
- Zone de protection: 20px minimum autour
- Pas de déformation ou modification
- Couleur: RVB (0, 0, 145) sur fond clair

**Variantes:**
- Logo couleur sur fond blanc/clair
- Logo blanc sur fond bleu/foncé
- Jamais de logo noir sauf impression N&B

### Logo Marianne

**Quand l'utiliser:**
- Représentation de l'État français
- Communication gouvernementale
- Événements officiels

**Règles:**
- Ne jamais déformer
- Respecter les proportions
- Zone de protection égale à la hauteur du M

### Logos Ministères

- Position: En haut à droite
- Taille: proportionnelle au logo RF
- Alignement vertical avec logo RF

---

## 5. Accessibilité Numérique (RGAA)

### Conformité Obligatoire

Les présentations officielles de l'État doivent être conformes au **RGAA 4.1** (Référentiel Général d'Amélioration de l'Accessibilité).

### Critères Principaux

**1. Contraste des couleurs**
- Texte normal: ratio ≥ 4.5:1
- Grand texte (≥18pt): ratio ≥ 3:1
- Éléments d'interface: ratio ≥ 3:1

Outils de vérification:
- WebAIM Contrast Checker
- Colour Contrast Analyser

**2. Texte alternatif**
- Toute image informative doit avoir un texte alt
- Images décoratives: texte alt vide
- Graphiques: description textuelle complète

**3. Structure et navigation**
- Titres de slides présents et hiérarchisés
- Ordre de lecture logique des éléments
- Numérotation visible des slides

**4. Utilisation de la couleur**
- Jamais d'information par la couleur seule
- Ajouter formes, motifs, texte
- Exemple graphique accessible:
  ```
  ✓ Barres avec motifs + couleurs
  ✗ Barres avec couleurs seules
  ```

**5. Lisibilité**
- Police minimum 14pt (contenu)
- Police minimum 18pt (titres)
- Interligne minimum 1.5
- Éviter texte sur images complexes

**6. Animations et transitions**
- Pas d'animations automatiques > 5 secondes
- Possibilité de mettre en pause
- Pas d'effets de clignotement (épilepsie)

**7. Langue**
- Attribut de langue défini (français)
- Acronymes explicités à la première occurrence

---

## 6. Éléments Graphiques

### Icônes DSFR

**Bibliothèque Remix Icon**
Le DSFR utilise la bibliothèque Remix Icon.

**Règles d'usage:**
- Style: Outline (contour) prioritaire
- Taille: 24px, 32px, ou 48px
- Couleur: Bleu France ou Gris 800
- Pas de mélange de styles d'icônes

**Icônes courantes:**
- Information: `ri-information-line`
- Attention: `ri-error-warning-line`
- Succès: `ri-checkbox-circle-line`
- Erreur: `ri-close-circle-line`

### Illustrations

**Style recommandé:**
- Illustrations vectorielles simples
- Palette DSFR uniquement
- Pas de photos sauf si nécessaire
- Pas d'images clipart

### Graphiques et Diagrammes

**Barres et colonnes**
- Couleurs DSFR
- Motifs pour différenciation
- Légendes explicites
- Axes étiquetés

**Courbes**
- Lignes épaisses (≥ 2px)
- Marqueurs sur points clés
- Couleurs contrastées
- Éviter plus de 5 courbes

**Camemberts**
- Maximum 5-6 segments
- Étiquettes avec pourcentages
- Légende si nécessaire
- Éviter la 3D

---

## 7. Composants DSFR Adaptés

### Boutons (pour slides interactives)

**Bouton primaire**
- Fond: Bleu France (#000091)
- Texte: Blanc
- Bordure: Aucune
- Coins arrondis: 4px

**Bouton secondaire**
- Fond: Transparent
- Texte: Bleu France
- Bordure: 1px Bleu France
- Coins arrondis: 4px

### Alertes et Messages

**Structure:**
```
┌─────────────────────────────────────┐
│ [Icône] Type d'alerte               │
│ Message principal                    │
│ Détails supplémentaires (optionnel) │
└─────────────────────────────────────┘
```

**Types:**
- Info: Fond bleu clair, icône info bleue
- Succès: Fond vert clair, icône succès verte
- Attention: Fond orange clair, icône attention orange
- Erreur: Fond rouge clair, icône erreur rouge

### Tags et Badges

- Hauteur: 24px
- Padding: 4px 8px
- Coins arrondis: 4px
- Texte: Marianne Regular 12pt

---

## 8. Templates de Slides

### Slide de Titre (Page 1)

```
┌──────────────────────────────────────┐
│ [Logo RF]              [Logo Min.]   │
│                                      │
│                                      │
│        TITRE DE LA PRÉSENTATION      │
│           (Marianne Bold 36pt)       │
│                                      │
│        Sous-titre si nécessaire      │
│           (Marianne Regular 20pt)    │
│                                      │
│              Date et lieu            │
│                                      │
└──────────────────────────────────────┘
```

### Slide de Section

```
┌──────────────────────────────────────┐
│ [Logo RF]              [Logo Min.]   │
│                                      │
│                                      │
│                                      │
│            NOM DE LA SECTION         │
│           (Marianne Bold 32pt)       │
│               (Centré)               │
│                                      │
│                                      │
│                                      │
│ Ministère              Page 2/10     │
└──────────────────────────────────────┘
```

### Slide de Contenu Standard

```
┌──────────────────────────────────────┐
│ [Logo RF]   Titre de la slide        │
├──────────────────────────────────────┤
│                                      │
│ • Point 1                            │
│ • Point 2                            │
│ • Point 3                            │
│                                      │
│  [Graphique ou visuel si applicable] │
│                                      │
│                                      │
│ Source: xxx   Ministère   Page 3/10  │
└──────────────────────────────────────┘
```

---

## 9. Checklist DSFR Spécifique

### Identité Visuelle
- [ ] Logo République Française présent (haut gauche)
- [ ] Logo ministère/organisation présent (haut droit) si applicable
- [ ] Logos non déformés et dans la zone de protection
- [ ] Marianne comme police principale (ou Arial en fallback)

### Couleurs
- [ ] Palette DSFR respectée (Bleu France, Rouge Marianne, Gris)
- [ ] Contraste suffisant (≥ 4.5:1 pour texte)
- [ ] Pas d'information par la couleur seule
- [ ] Couleurs fonctionnelles utilisées correctement

### Typographie
- [ ] Marianne Bold pour titres
- [ ] Marianne Regular pour texte
- [ ] Taille minimum 14pt pour contenu
- [ ] Taille minimum 18pt pour titres de slides
- [ ] Interligne 1.5 minimum

### Structure
- [ ] Format 16:9
- [ ] Marges respectées (100px gauche/droite, 80px haut/bas)
- [ ] Numérotation des slides (pied de page)
- [ ] Titre sur chaque slide

### Accessibilité
- [ ] Contraste vérifié et conforme
- [ ] Textes alternatifs sur images
- [ ] Pas d'animations automatiques > 5s
- [ ] Acronymes explicités
- [ ] Graphiques accessibles (motifs + couleurs)

---

## 10. Ressources et Outils

### Documentation Officielle
- **Site DSFR**: https://www.systeme-de-design.gouv.fr/
- **RGAA**: https://accessibilite.numerique.gouv.fr/
- **Charte graphique État**: Disponible sur le site du SIG

### Outils de Vérification

**Contraste:**
- WebAIM Contrast Checker
- Colour Contrast Analyser (CCA)

**Accessibilité:**
- Assistant RGAA (extension navigateur)
- NVDA (lecteur d'écran gratuit)

**Polices:**
- Téléchargement Marianne: Site DSFR
- Installation système requise pour PowerPoint

### Templates PowerPoint

Télécharger les templates officiels depuis:
- Intranet ministériel
- Site du SIG (Service d'Information du Gouvernement)
- Demande auprès de la DITP

---

## Patterns grep pour recherche rapide

```bash
# Rechercher les couleurs DSFR
grep -A 3 "Bleu France\|Rouge Marianne" references/dsfr_standards.md

# Rechercher les règles d'accessibilité
grep -A 5 "Accessibilité\|RGAA\|Contraste" references/dsfr_standards.md

# Rechercher les spécifications typographiques
grep -A 4 "Marianne.*Police\|Typographie" references/dsfr_standards.md

# Checklist complète
grep -A 30 "Checklist DSFR" references/dsfr_standards.md
```
