import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Finance", layout="wide")

st.title(" Vue Exécutive")

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

#  KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric(" Volume Total", f"{df['montant'].sum():,.0f}")
col2.metric("CA Total", f"{df[df['type_operation']=='Credit']['montant'].sum():,.0f}")
col3.metric(" Clients actifs", df["id_client"].nunique())
col4.metric("Marge moyenne", f"{df['montant'].mean():.2f}")

#  Graph ligne
st.subheader(" Évolution mensuelle")

#transforme en tableau pour graphique(unstack)

evolution = df.groupby(["mois", "type_operation"])["montant"].sum().unstack()

st.line_chart(evolution)

#  Graph bar
st.subheader(" CA par agence")

st.bar_chart(df.groupby("nom_agence")["montant"].sum())

#  Pie chart
st.subheader(" Répartition des segments")

fig, ax = plt.subplots()
df["nom_segment"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
st.pyplot(fig)

#  Export CSV
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(" Télécharger CSV", csv, "data_filtre.csv", "text/csv")