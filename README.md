# 🎬 Prédiction de la Popularité des Films avec Machine Learning

## 📌 Objectif du Projet

Développer un modèle de machine learning capable de prédire la popularité d’un film à partir de ses caractéristiques.

## 📊 Données Utilisées

- **Source** : Données extraites via l'API de The Movie Database (TMDB).
- **Volume** : Environ 2800 films collectés initialement, avec 500 lignes supprimées en raison de l'absence de données sur le budget ou les revenus.
- **Colonnes principales** :
  - Informations générales : `release_date`, `genres`, `popularity`, `vote_count`, `vote_average`, `runtime`, `budget`, `revenue`.
  - Genres détaillés : `Action`, `Adventure`, `Animation`, `Comedy`, `Crime`, `Documentary`, `Drama`, `Family`, `Fantasy`, `History`, `Horror`, `Music`, `Mystery`, `Romance`, `Science Fiction`, `TV Movie`, `Thriller`, `War`, `Western`.
  - Informations sur la production : `production_companies`, `production_countries`, `prod_company_1`, `prod_company_2`, `prod_country_1`, `prod_country_2`.
  - Caractéristiques dérivées : `release_year`, `release_month`, `profit`, `score_minmax`, `score_quantile`, `score_log`, `score_bayesian`, `genre_impact_score`, `genre_weighted_score`, `prod_company_freq`, `prod_country_freq`.

- **Nettoyage et enrichissement** :
  - Suppression des lignes avec des valeurs manquantes critiques.
  - Encodage des variables catégorielles telles que les genres, les pays de production et les compagnies de production.
  - Création de nouvelles variables pour améliorer la performance du modèle.

## 🧠 Objectif de la Modélisation

- **Variables cibles** :
  - `score_log` : Transformation logarithmique du score de popularité.
  - `score_bayesian` : Score de popularité ajusté selon une approche bayésienne.

- **Métriques d'évaluation** :
  - Coefficient de détermination (R²).
  - Erreur quadratique moyenne (RMSE).

## 🤖 Modèles Utilisés

- **Algorithmes testés** :
  - Random Forest
  - LightGBM
  - XGBoost

- **Comparaison des performances** :
  - Les modèles ont été évalués sur les deux variables cibles (`score_log` et `score_bayesian`).
  - Le modèle Random Forest a obtenu les meilleurs résultats en termes de R² et de RMSE.

## 🛠️ Caractéristiques Créées

- **Variables dérivées** :
  - `profit` : Calculé comme la différence entre `revenue` et `budget`.
  - `release_month` : Mois de sortie du film, extrait de `release_date`.
  - `prod_company_freq` : Fréquence d'apparition des compagnies de production.
  - `prod_country_freq` : Fréquence d'apparition des pays de production.
  - `genre_impact_score` : Score mesurant l'impact du genre sur la popularité.
  - `genre_weighted_score` : Score pondéré basé sur les genres du film.

## 📁 Organisation du Dépôt

- ML-JDSL/
- ├── notebooks/ # Notebooks Jupyter pour l'exploration et la modélisation
- ├── models/ # Modèles entraînés et fichiers associés
- ├── streamlit/ # Application Streamlit pour la visualisation des résultats
- ├── README.md # Documentation du projet

  
- **Branches Git** :
  - `main` : Version stable du projet.
  - `data-cleaning` : Scripts et notebooks pour le nettoyage des données.
  - `feature-engineering` : Création et sélection des caractéristiques.
  - `modeling` : Entraînement et évaluation des modèles.
  - `streamlit-app` : Développement de l'interface utilisateur avec Streamlit.

## 🖥️ Interface Utilisateur

- **Environnement de développement** :
  - Visual Studio Code pour le codage.
  - Git pour la gestion des versions et des branches.

- **Application Streamlit** :
  - Visualisation interactive des résultats des modèles.
  - Exploration des données et des prédictions.

- **Formulaire utilisateur** :
  - Non implémenté dans cette version du projet.

## 👥 Équipe et Contexte

- **Membres de l'équipe** :
  - Julie Gabert
  - Léa Chapoton
  - Diana Sarfati
  - Sophie Mainial

- **Contexte** :
  - Projet réalisé dans le cadre du cours de Machine Learning.
  - Travail collaboratif visant à appliquer les techniques de machine learning à un cas concret.
