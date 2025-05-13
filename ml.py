import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Barre latérale de navigation ===
section = st.sidebar.radio("📂 Navigation", [
    "🏠 Introduction",
    "Random Forest",
    "GBM",
    "XGBOOST",
    "📝 Conclusion"
])

#introduction page
if section == "🏠 Introduction":

    st.title("Machine learning presentation")
    st.write("Léa Chapoton, Sophie Mainial, Julie Gabert, Diana Sarfati ")


    # --- SECTION 1 : Chargement ou simulation du DataFrame ---
    st.header("🔍 Présentation des données")
    st.markdown("""
    Ce jeu de données provient de la base de films TMDB. Il contient des informations sur des milliers de films, 
    dont le budget, les revenus, la popularité, le genre, la durée, les notes des utilisateurs, etc.
    """)

    st.markdown("""
    🎯 **Objectif du projet** : **Prédire les performances d’un film (la note) à partir de ses caractéristiques (budget, genre, popularité, etc.)**.
    """)

    # --- Chargement des données ---
    @st.cache_data
    def load_data():
        df = pd.read_csv("tmdb_movies_full_cleaned.csv")
        return df

    df = load_data()

    # --- Affichage conditionné dans un bouton déroulant ---
    with st.expander("🔎 Afficher le DataFrame"):
        st.dataframe(df)

    st.markdown("#### 1. 📊 analyses exploratoires")
    # a mettre analyse

    st.markdown("#### 2. autre analyses")
    # a mettre 

    st.markdown("#### 3. autre encore")
# a mettre 

# Model randomn forest page
if section == "Random Forest":
    st.header("Random Forest")


    if "show_explanation" not in st.session_state:
        st.session_state.show_explanation = False

    if st.button("💡 Pourquoi ce modèle ?"):
        st.session_state.show_explanation = not st.session_state.show_explanation

    if st.session_state.show_explanation:
        st.markdown("""
        Pourquoi : très robuste, pas sensible aux valeurs extrêmes ni à la colinéarité.
        
        Avantage : interprétable via l'importance des variables, fonctionne bien sans réglage fin.
        
        Résultat attendu : bon modèle de base, surtout utile si peu de données ou pour comparer.
        """)


    st.markdown("#### 1. pretraitement")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)


    st.markdown("#### 2. resultats")
    #mettre graphique ect
    st.markdown(""" a ecrire des explication
    """)
    
    st.markdown("#### 3. optimisation")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)

    st.markdown("#### 4. conclusion/resultat final")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)




if section == "GBM":
    st.header("GBM")


    if "show_explanation" not in st.session_state:
        st.session_state.show_explanation = False

    if st.button("💡 Pourquoi ce modèle ?"):
        st.session_state.show_explanation = not st.session_state.show_explanation

    if st.session_state.show_explanation:
        st.markdown("""
        Pourquoi : plus rapide que XGBoost sur grands datasets, particulièrement efficace quand les features sont nombreuses (comme ici avec les genres).
        
        Avantage : supporte les colonnes catégorielles natives, très optimisé en RAM et vitesse.
        
        Résultat attendu: prédiction rapide et scalable, très bon sur gros volumes.
        """)


    st.markdown("#### 1. pretraitement")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)


    st.markdown("#### 2. resultats")
    #mettre graphique ect
    st.markdown(""" a ecrire des explication
    """)
    
    st.markdown("#### 3. optimisation")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)

    st.markdown("#### 4. conclusion/resultat final")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)


if section == "XGBOOST":
    st.header("XGBOOST")


    if "show_explanation" not in st.session_state:
        st.session_state.show_explanation = False

    if st.button("💡 Pourquoi ce modèle ?"):
        st.session_state.show_explanation = not st.session_state.show_explanation

    if st.session_state.show_explanation:
        st.markdown("""
        Pourquoi : très robuste, pas sensible aux valeurs extrêmes ni à la colinéarité.
        
        Avantage : interprétable via l'importance des variables, fonctionne bien sans réglage fin.

        Résultat attendu : bon modèle de base, surtout utile si peu de données ou pour comparer.
        """)


    st.markdown("#### 1. pretraitement")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)

    st.markdown("#### 2. resultats")
    #mettre graphique ect
    st.markdown(""" a ecrire des explication
    """)
    
    st.markdown("#### 3. optimisation")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)

    st.markdown("#### 4. conclusion/resultat final")
    #mettre graphique etc
    st.markdown(""" a ecrire des explication
    """)