import requests
import pandas as pd
from pandas import json_normalize

API_KEY = "YOUR_API_KEY" # mettre l'API KEY ici


LEAGUE_ID = 1625  # selection de la ligue souhaitée, ici Premier League saison 2018-2019

url = f"https://api.footystats.org/league-matches?key={API_KEY}&league_id={LEAGUE_ID}"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    data = json_data.get("data", [])

    if data:
        # Aplatir les structures imbriquées
        df = json_normalize(data)

        # Sauvegarde du df dans un .csv
        df.to_csv("matches_premier_league2019.csv", index=False)

        print("Import données ok")
        print(df.head())  # Check de l'import
    else:
        print("Aucune donnée reçue.")
else:
    print(f"Erreur : {response.status_code} : {response.text}")
