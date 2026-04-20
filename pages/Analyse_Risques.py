import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(" Analyse des Risques")

#  Charger CSV
df = pd.read_csv(r"C:\Users\nouha\Desktop\Dashboard_Gestion_des_Risques_pour_FinanceCore_SA\data\data.csv")

#  Préparation
df["date_transaction"] = pd.to_datetime(df["date_transaction"], errors="coerce")

#  Sidebar filtres
st.sidebar.header("Filtres")

agence = st.sidebar.multiselect("Agence", df["nom_agence"].dropna().unique())
segment = st.sidebar.multiselect("Segment", df["nom_segment"].dropna().unique())
produit = st.sidebar.multiselect("Produit", df["nom_produit"].dropna().unique())
annee = st.sidebar.slider("Année", 2022, 2024, (2022, 2024))

#  Filtrage
if agence:
    df = df[df["nom_agence"].isin(agence)]

if segment:
    df = df[df["nom_segment"].isin(segment)]

if produit:
    df = df[df["nom_produit"].isin(produit)]

df = df[(df["date_transaction"].dt.year >= annee[0]) &
        (df["date_transaction"].dt.year <= annee[1])]

#  Heatmap
st.subheader("Corrélation")

corr = df[["score_credit", "montant"]].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)

#  Scatter
st.subheader(" Score crédit vs Montant")

fig2, ax2 = plt.subplots()
ax2.scatter(df["score_credit"], df["montant"])
st.pyplot(fig2)

#  Top clients à risque
st.subheader(" Top 10 clients à risque")

risk_df = df.sort_values("score_credit").head(10)

def color(val):
    return "color:red" if val < 400 else "color:green"

st.dataframe(risk_df.style.map(color, subset=["score_credit"]))