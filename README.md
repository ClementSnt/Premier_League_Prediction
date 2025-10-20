# ⚽ **Football Data Extraction API**

## 🎯 Objectif
Ce projet illustre comment extraire et structurer automatiquement des données de football via l’API **Footystats**.  
Il constitue une base pour des futures analyses  : modélisation, visualisation, suivi de performances d’équipes, etc.

## ⚙️ Fonctionnement
Le script interroge l’API publique de Footystats pour récupérer les données d’une ligue donnée (ici la **Premier League 2018-2019**), puis les convertit en un fichier csv

## 🧩 Contenu
- **`data_extraction.py`** : script principal d’appel API et d’enregistrement des données.  
- **`matches_premier_league2019.csv`** : exemple de fichier de sortie généré contenant les matchs, équipes, scores, statistiques, etc.

## 🚀 Utilisation
1. Crée un compte sur [Footystats.org](https://footystats.org/api) pour obtenir une **API key**.  
2. Remplace la valeur `YOUR_API_KEY` dans le script.  
3. Exécute le script :
   ```bash
   python data_extraction.py

