# Rapport de Révision de Présentation

**Fichier analysé** : {filename}
**Date d'analyse** : {date}
**Analyseur** : presentation-reviewer skill v1.1
**Configuration** : {config_file}

---

## 📊 Synthèse Executive

| Métrique | Valeur | Statut |
|----------|--------|--------|
| **Note Globale** | {note}/10 | {status_emoji} |
| **Total de slides** | {total_slides} | - |
| **Mots par slide (moy.)** | {avg_words} | {words_status} |
| **Problèmes critiques** | {high_issues} | {critical_status} |
| **Framework détecté** | {framework} ({confidence}%) | {framework_status} |

**Verdict** : {verdict_text}

---

## 🎯 Top 5 des Corrections Prioritaires

### 1. {issue_1_title} 🔴

**Slide concernée** : {slide_number}
**Problème** : {problem_description}
**Impact** : {impact_description}
**Action recommandée** : {action}

**Avant** :
```
{before_text}
```

**Après** :
```
{after_text}
```

---

### 2. {issue_2_title} 🔴
...

---

## 📈 Analyse par Axe

### Axe 1 : Structure Logique (Score: {structure_score}/10)

**Framework détecté** : {framework}
**Confiance** : {confidence}%
**Framework recommandé** : {recommended_framework}

**Points forts** :
- ✅ {strength_1}
- ✅ {strength_2}

**Points d'amélioration** :
- ⚠️ {weakness_1}
- ⚠️ {weakness_2}

**Recommandations** :
1. {recommendation_1}
2. {recommendation_2}

---

### Axe 2 : Clarté du Message (Score: {clarity_score}/10)

**Slides sans titre** : {no_title_count}
**Slides trop denses (>50 mots)** : {dense_count}
**"So What?" clair** : {so_what_score}%

**Titres à améliorer** :

| Slide | Titre actuel | Titre proposé |
|-------|--------------|---------------|
| 3 | {old_title_3} | {new_title_3} |
| 7 | {old_title_7} | {new_title_7} |

---

### Axe 3 : Cohérence de la Trame (Score: {coherence_score}/10)
...

### Axe 4 : Design et Formatage (Score: {design_score}/10)

**Conformité DSFR** : {dsfr_score}%

**Couleurs non conformes** :
- Slide {slide_num} : {color} → Remplacer par {dsfr_color}

**Contrastes insuffisants** :
- Slide {slide_num} : Ratio {ratio}:1 ❌ → Minimum 4.5:1

---

### Axe 5 : Visualisation de Données (Score: {dataviz_score}/10)
...

### Axe 6 : Storytelling (Score: {storytelling_score}/10)
...

### Axe 7 : Accessibilité (Score: {accessibility_score}/10)

**Conformité RGAA** : {rgaa_level}

**Critères non respectés** :
- [ ] Contraste couleur (3 slides)
- [ ] Texte alternatif images (2 slides)
- [ ] Information par couleur seule (4 graphiques)

---

## 📋 Détail par Slide

### Slide 1 : {title_1}

**Score** : {slide_1_score}/10
**Problèmes** : {issues_count}

**Commentaires** :
- 🟢 {positive_comment}
- ⚠️ {improvement_1}
- ⚠️ {improvement_2}

---

### Slide 2 : {title_2}
...

---

## 🚀 Plan d'Action Recommandé

### Phase 1 : Corrections Critiques (Aujourd'hui)

1. **Restructurer slides 7-9** (30 min)
   - Action : Inverser l'ordre pour respecter SCQA
   - Responsable : Auteur
   - Deadline : Aujourd'hui

2. **Corriger contrastes** (15 min)
   - Slides concernées : 3, 8, 11
   - Action : Utiliser Gris 1000 #161616 au lieu de Gris 600
   - Outil : PowerPoint > Format > Couleur du texte

3. **Réécrire 3 titres** (20 min)
   - Slides : 3, 5, 12
   - Passer de sujets à affirmations
   - Exemples fournis dans rapport ci-dessus

### Phase 2 : Améliorations Importantes (Demain)

4. **Ajouter slide de conclusion actionnée** (30 min)
5. **Simplifier slides denses** (45 min)
6. **Rendre graphiques accessibles** (30 min)

### Phase 3 : Peaufinage (Avant présentation)

7. **Vérifier conformité DSFR complète** (1h)
8. **Répétition et timing** (30 min)

**Temps total estimé** : 4h réparties sur 2-3 jours

---

## 📎 Annexes

### A. Configuration Utilisée

```json
{config_json}
```

### B. Scores Détaillés

| Slide | Titre | Mots | Bullets | Score | Problèmes |
|-------|-------|------|---------|-------|-----------|
| 1 | {title} | {words} | {bullets} | {score} | {issues} |
| 2 | {title} | {words} | {bullets} | {score} | {issues} |
...

### C. Analyse Framework Complète

{framework_detailed_analysis}

### D. Références

- Checklist complète : `references/checklist.md`
- Frameworks détaillés : `references/frameworks.md`
- Standards DSFR : `references/dsfr_standards.md`

---

**Rapport généré par** : presentation-reviewer skill
**Version** : 1.1
**Contact** : support@example.com
