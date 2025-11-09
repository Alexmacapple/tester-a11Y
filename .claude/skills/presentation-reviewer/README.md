# Presentation Reviewer Skill

Skill de révision de présentations PowerPoint selon les standards de conseil (McKinsey, BCG) avec analyse multi-axes et conformité DSFR.

## Vue d'ensemble

Ce skill agit comme un **Manager de Conseil senior** pour réviser des présentations PowerPoint. Il combine des analyses automatisées (scripts Python) et une révision qualitative approfondie pour produire des commentaires directement intégrés dans les slides.

## Capacités

### 7 Axes d'Analyse

1. **Structure Logique** - Framework de storytelling, progression, principe de la pyramide
2. **Clarté du Message** - Titres, "So What?", densité du contenu
3. **Cohérence de la Trame** - Terminologie, transitions, fil conducteur
4. **Design et Formatage** - Cohérence visuelle, alignement, typographie, conformité DSFR
5. **Visualisation de Données** - Choix de graphiques, accessibilité, insights
6. **Storytelling et Frameworks** - SCQA, AIDA, PASS, Pyramide, MECE
7. **Accessibilité et Conformité** - RGAA, DSFR, contraste, lisibilité

### Fonctionnalités

- ✅ Analyse automatique (stats, problèmes techniques)
- ✅ Détection du framework de storytelling
- ✅ Suggestion du framework optimal selon contexte
- ✅ Commentaires directement dans les slides PowerPoint
- ✅ Vérification conformité DSFR et RGAA
- ✅ Propositions de corrections concrètes
- ✅ Rapport de synthèse détaillé

## Utilisation

### Cas d'usage 1 : Révision rapide

```
"Peux-tu réviser ma présentation et me dire ce qui ne va pas ?"
```

### Cas d'usage 2 : Révision complète avec commentaires

```
"Je veux une révision complète style McKinsey avec commentaires dans les slides"
```

### Cas d'usage 3 : Vérification DSFR

```
"Ma présentation respecte-t-elle les standards DSFR ?"
```

### Cas d'usage 4 : Aide à la restructuration

```
"Ma présentation manque de structure, comment l'améliorer ?"
```

## Structure du Skill

```
presentation-reviewer/
├── SKILL.md                          # Instructions principales
├── scripts/
│   ├── analyzer.py                   # Analyse automatique
│   ├── framework_detector.py         # Détection de framework
│   └── reviewer.py                   # Ajout de commentaires
├── references/
│   ├── checklist.md                  # Checklist exhaustive
│   ├── frameworks.md                 # Guide des frameworks
│   └── dsfr_standards.md            # Standards DSFR complets
└── assets/
    ├── template-dsfr.pptx           # Template de référence
    └── README.md
```

## Scripts Python

### analyzer.py
Analyse automatique de la présentation (stats, problèmes techniques)

**Usage** :
```bash
python3 scripts/analyzer.py presentation.pptx --output analysis.json
```

### framework_detector.py
Détecte le framework de storytelling et suggère le plus adapté

**Usage** :
```bash
python3 scripts/framework_detector.py presentation.pptx --suggest conseil
```

**Types** : commercial, problème, stratégie, compte-rendu, conseil, general

### reviewer.py
Ajoute les commentaires de révision dans le PowerPoint

**Usage** :
```bash
python3 scripts/reviewer.py presentation.pptx analysis.json --output presentation_revu.pptx
```

## Dépendances

- Python 3.7+
- python-pptx (`pip install python-pptx`)

## Frameworks Supportés

- **SCQA** (Situation, Complication, Question, Answer)
- **Pyramide de Minto** (Message principal → Arguments → Preuves)
- **AIDA** (Attention, Intérêt, Désir, Action)
- **PASS** (Problème, Agitation, Solution, Situation)
- **What/So What/Now What**
- **MECE** (Mutually Exclusive, Collectively Exhaustive)
- **Storytelling 3 actes**

## Standards DSFR

Conformité au **Design Système de l'État Français** :
- Palette de couleurs (Bleu France #000091, Rouge Marianne #E1000F)
- Typographie Marianne
- Logos officiels
- Accessibilité RGAA 4.1

## Installation

1. Installer le skill dans Claude Code
2. Installer les dépendances Python :
   ```bash
   pip install python-pptx
   ```

## Exemple de Workflow

1. Utilisateur soumet une présentation PowerPoint
2. Claude exécute `analyzer.py` et `framework_detector.py`
3. Claude analyse selon les 7 axes
4. Claude exécute `reviewer.py` pour ajouter les commentaires
5. Claude fournit :
   - Présentation commentée (PowerPoint)
   - Rapport de synthèse (Markdown)
   - Note globale /5
   - Top 10 des corrections prioritaires
   - Propositions de restructuration

## Auteur

Créé avec skill-creator pour Claude Code

## Licence

À définir selon votre organisation
