# ⚽ **Projet Prédiction de Résultats de la Premier League**

⚠️⚠️ PROJET NON TERMINE / EN COURS DE REALISATION ⚠️⚠️

## Description  
Ce projet vise à construire un modèle prédictif pour anticiper les résultats des matchs de la Premier League anglaise, en s’appuyant sur des données historiques extraites via l’API FootyStats. L’objectif est de démontrer mes compétences en extraction et traitement de données, analyse, clustering, modélisation prédictive et visualisation avec Streamlit.

---

## Structure du projet

### 1. Extraction des données  
- Utilisation de l’API FootyStats pour récupérer les données des matchs (scores, statistiques d’équipe, possession, xG, etc.)  
- Stockage des données par saison dans des fichiers CSV

### 2. Nettoyage & Analyse exploratoire (EDA)  
- Nettoyage des données (gestion des valeurs manquantes, formats)  
- Ajout de variables temporelles (ex : découpage en demi-saisons)  
- Analyse descriptive et visualisations

### 3. Profilage des équipes par clustering  
- Calcul des statistiques agrégées par équipe et par demi-saison  
- Application d’algorithmes de clustering pour regrouper les équipes selon leur profil de jeu

### 4. Construction du dataset d’apprentissage  
- Association des profils d’équipes aux matchs selon la période (H1/H2)  
- Ajout des variables contextuelles (match à domicile/extérieur, forme récente)

### 5. Modélisation prédictive  
- Mise en place d’un modèle de classification pour prédire le résultat d’un match (victoire domicile, nul, victoire extérieur)  
- Évaluation des performances et optimisation

### 6. Visualisation  
- Création d’un dashboard interactif avec Streamlit pour visualiser les données et les prédictions
