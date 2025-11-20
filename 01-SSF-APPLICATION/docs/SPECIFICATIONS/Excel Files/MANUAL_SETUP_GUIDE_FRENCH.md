# 📝 Guide de Configuration Manuelle pour Microsoft 365 Online (FRANÇAIS)

**Temps Total:** ~35 minutes  
**Résultat:** Tracker fonctionnel avec PI Progress et graphiques  
**Compatible:** 100% Microsoft 365 Online (version française)

---

## 🎯 Vue d'ensemble

**IMPORTANT:** Ce guide utilise les **noms de fonctions Excel en FRANÇAIS**

---

## 📂 Partie 1: Mettre à jour JIRA DATA (5 minutes)

### Étape 1.1: Ajouter colonne Labels

1. Ouvrir `DG_MARE_TEAMS_SSF_Refinement_Tracker.xlsx` dans Excel Online
2. Aller sur **JIRA DATA**
3. Clic droit sur l'en-tête colonne **H**
4. Cliquer **Insertion** → **Insérer des colonnes à gauche**
5. Cliquer cellule **H2**
6. Taper: `Labels`
7. Format: Gras, Texte blanc, Fond bleu

### Étape 1.2: Ajouter colonne PI

1. Clic droit sur l'en-tête colonne **J**  
2. Cliquer **Insertion** → **Insérer des colonnes à gauche**
3. Cliquer cellule **J2**
4. Taper: `PI`
5. Format: Gras, Texte blanc, Fond bleu

### Étape 1.3: Importer données

1. Ouvrir `SSF_BACKLOG_EXPORT_10_11.xlsx` dans un **deuxième onglet**
2. Sélectionner lignes 5-95 (91 lignes de données)
3. Copier (Ctrl+C)
4. Retour au tracker, onglet JIRA DATA
5. Cliquer cellule **A3**
6. Coller (Ctrl+V)

### Étape 1.4: Extraire les labels PI

1. Cliquer cellule **J3**
2. Coller cette formule **FRANÇAISE**:
   ```excel
   =SI(ESTNUM(CHERCHE("SSF_PI#";H3));STXT(H3;CHERCHE("SSF_PI#";H3);10);"")
   ```
3. Appuyer sur Entrée
4. Cliquer cellule **J3** à nouveau
5. Faire glisser vers le bas jusqu'à la ligne 93
6. La colonne J contient maintenant les labels PI!

**✅ Partie 1 Terminée!**

---

## 📊 Partie 2: Corriger EPIC PROGRESS (2 minutes)

### Étape 2.1: Mettre à jour les noms d'epics

1. Aller sur **EPIC PROGRESS**
2. **Taper manuellement** ces noms dans Colonne A (à partir ligne 3):

```
Ligne 3:  App Menu
Ligne 4:  Data Exchange w/FMC
Ligne 5:  Departure Declaration
Ligne 6:  Gear Management
Ligne 7:  Hauls
Ligne 8:  Home Screen
Ligne 9:  INFRA
Ligne 10: Language Management
Ligne 11: Login
Ligne 12: Logs
Ligne 13: Map Integrations
Ligne 14: TECH REQUIREMENTS
Ligne 15: Vessel Tracking
```

3. Les formules se recalculent automatiquement!

**✅ Partie 2 Terminée!**

---

## 📈 Partie 3: Créer PI PROGRESS (5 minutes)

### Étape 3.1: Créer nouvelle feuille

1. Cliquer **+** en bas pour ajouter feuille
2. Renommer: `PI PROGRESS`
3. La glisser en position 3 (après DASHBOARD)

### Étape 3.2: Ajouter titre

1. Cliquer cellule **A1**
2. Taper: `PI PROGRESS TRACKER`
3. Format: Gras, Taille 16, Texte blanc, Fond bleu
4. Fusionner cellules A1:H1

### Étape 3.3: Ajouter en-têtes (Ligne 2)

```
A2: PI Label
B2: Total Stories
C2: Refined (Ready)
D2: To Refine (Open)
E2: Other Status
F2: % Complete
G2: Progress
H2: Status
```

Format: Gras, Texte blanc, Fond vert

### Étape 3.4: Ajouter données PI

**Ligne 3 - SSF_PI#01** (formules FRANÇAISES):

```
A3: SSF_PI#01
B3: =NB.SI('JIRA DATA'!J:J;A3)
C3: =NB.SI.ENS('JIRA DATA'!J:J;A3;'JIRA DATA'!E:E;"Ready")
D3: =NB.SI.ENS('JIRA DATA'!J:J;A3;'JIRA DATA'!E:E;"Open")
E3: =B3-C3-D3
F3: =SI(B3=0;0;C3/B3)
G3: =C3&"/"&B3
H3: =SI(F3>0,7;"🟢";SI(F3>0,3;"🟡";"🔴"))
```

**Ligne 4 - SSF_PI#02** (formules FRANÇAISES):

```
A4: SSF_PI#02
B4: =NB.SI('JIRA DATA'!J:J;A4)
C4: =NB.SI.ENS('JIRA DATA'!J:J;A4;'JIRA DATA'!E:E;"Ready")
D4: =NB.SI.ENS('JIRA DATA'!J:J;A4;'JIRA DATA'!E:E;"Open")
E4: =B4-C4-D4
F4: =SI(B4=0;0;C4/B4)
G4: =C4&"/"&B4
H4: =SI(F4>0,7;"🟢";SI(F4>0,3;"🟡";"🔴"))
```

**⚠️ IMPORTANT:** Notez que les points-virgules (;) remplacent les virgules (,) en français!

### Étape 3.5: Formater colonne F

1. Sélectionner cellules F3:F4
2. Clic droit → Format de cellule
3. Choisir: Pourcentage, 1 décimale

**✅ Partie 3 Terminée!**

---

## 📝 Partie 4: Ajouter colonne PI à SESSION LOG (2 minutes)

1. Aller sur **SESSION LOG**
2. Cliquer cellule **K2**
3. Taper: `PI(s) Worked`
4. Format: Gras, Texte blanc, Fond vert

**✅ Partie 4 Terminée!**

---

## 📊 Partie 5: Créer PI SESSION LOGS (10 minutes par PI)

### Étape 5.1: Créer SSF_PI#01 SESSION LOG

1. Cliquer **+** pour nouvelle feuille
2. Renommer: `SSF_PI#01 SESSION LOG`

**Titre:**
```
A1: SSF_PI#01 REFINEMENT SESSION LOG
Fusionner A1:I1, Gras, Taille 14, Texte blanc, Fond bleu
```

**En-têtes:**
```
A2: Session #
B2: Sprint
C2: Date
D2: PI(s) Worked
E2: Target Stories
F2: Stories Refined
G2: Cumulative
H2: Remaining
I2: Velocity
```

**Formules FRANÇAISES (Ligne 3):**
```
A3: 1
B3: ='SESSION LOG'!B3
C3: ='SESSION LOG'!C3
D3: ='SESSION LOG'!K3
E3: ='SESSION LOG'!E3
F3: =SI(ESTNUM(CHERCHE("SSF_PI#01";'SESSION LOG'!K3));'SESSION LOG'!F3;0)
G3: =SOMME($F$3:F3)
H3: =NB.SI('JIRA DATA'!J:J;"SSF_PI#01")-G3
I3: =F3
```

**Formules FRANÇAISES (Ligne 4):**
```
A4: 2
B4: ='SESSION LOG'!B4
C4: ='SESSION LOG'!C4
D4: ='SESSION LOG'!K4
E4: ='SESSION LOG'!E4
F4: =SI(ESTNUM(CHERCHE("SSF_PI#01";'SESSION LOG'!K4));'SESSION LOG'!F4;0)
G4: =SOMME($F$3:F4)
H4: =NB.SI('JIRA DATA'!J:J;"SSF_PI#01")-G4
I4: =MOYENNE($F$3:F4)
```

**Copier ligne 4 jusqu'à ligne 19** (ajuster numéros)

### Étape 5.2: Créer SSF_PI#02 SESSION LOG

Répéter 5.1, mais remplacer `"SSF_PI#01"` par `"SSF_PI#02"` dans formules

**✅ Partie 5 Terminée!**

---

## 📉 Partie 6: Créer PI BURNDOWN avec graphiques (15 minutes par PI)

### Étape 6.1: Créer SSF_PI#01 BURNDOWN

1. Cliquer **+** pour nouvelle feuille
2. Renommer: `SSF_PI#01 BURNDOWN`

**Configuration:**
```
A1: TARGET SESSIONS:
B1: 15
Format B1: Gras, Texte rouge, Fond jaune

A2: TOTAL STORIES:
B2: =NB.SI('JIRA DATA'!J:J;"SSF_PI#01")
Format: Gras
```

**Titre:**
```
D1: SSF_PI#01 BURNDOWN DATA
Fusionner D1:H1, Gras, Taille 14, Texte blanc, Fond bleu
```

**En-têtes (Ligne 4):**
```
A4: Session #
B4: Sprint
C4: IDEAL Remaining
D4: ACTUAL Remaining
E4: Variance
```

**Formules FRANÇAISES (Ligne 5):**
```
A5: 0
B5: ='SSF_PI#01 SESSION LOG'!B3
C5: =$B$2-($B$2/$B$1)*A5
D5: ='SSF_PI#01 SESSION LOG'!H3
E5: =D5-C5
```

**Formules FRANÇAISES (Ligne 6):**
```
A6: 1
B6: ='SSF_PI#01 SESSION LOG'!B4
C6: =$B$2-($B$2/$B$1)*A6
D6: ='SSF_PI#01 SESSION LOG'!H4
E6: =D6-C6
```

**Continuer jusqu'à ligne 21** (ajuster références)

### Étape 6.2: Créer le graphique

1. **Sélectionner** cellules **C4:D21**
2. Cliquer onglet **Insertion**
3. Cliquer **Graphiques** → **Graphique en courbes**
4. Le graphique apparaît!

**Formater:**
1. Titre: `SSF_PI#01 - Idéal vs Réel`
2. Axes: X = "Session #", Y = "Stories restants"
3. Légende: IDEAL et ACTUAL
4. Couleurs: Bleu (IDEAL), Rouge (ACTUAL)

### Étape 6.3: Créer SSF_PI#02 BURNDOWN

Répéter 6.1-6.2, remplacer `"SSF_PI#01"` par `"SSF_PI#02"`

**✅ Partie 6 Terminée!**

---

## 🔑 DIFFÉRENCES CLÉS - EXCEL FRANÇAIS

### Noms de Fonctions:

| Anglais | Français |
|---------|----------|
| COUNTIF | NB.SI |
| COUNTIFS | NB.SI.ENS |
| IF | SI |
| SUM | SOMME |
| AVERAGE | MOYENNE |
| SEARCH | CHERCHE |
| ISNUMBER | ESTNUM |
| MID | STXT |

### Séparateurs:

| Anglais | Français |
|---------|----------|
| Virgule (,) | Point-virgule (;) |
| Point (.) décimale | Virgule (,) décimale |

**Exemple:**
- Anglais: `=IF(A1=0,0,B1/A1)`
- Français: `=SI(A1=0;0;B1/A1)`

---

## ✅ Vérification

Après avoir terminé:

- [ ] JIRA DATA a 91 lignes
- [ ] Colonne H (Labels) remplie
- [ ] Colonne J (PI) a les labels PI
- [ ] PI PROGRESS montre 2 PIs avec nombres
- [ ] EPIC PROGRESS montre nombres (pas #NOM?)
- [ ] SESSION LOG a colonne K
- [ ] 2 PI SESSION LOG créées
- [ ] 2 PI BURNDOWN créées
- [ ] Graphiques s'affichent

---

**Ce guide utilise les fonctions Excel FRANÇAISES!**
