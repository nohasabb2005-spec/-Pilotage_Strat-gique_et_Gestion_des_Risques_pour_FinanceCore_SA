# 📊 FinanceCore Dashboard — Analyse Financière & Risques

## 📌 Description

Ce projet consiste à développer un **dashboard interactif avec Streamlit** permettant d’analyser les données financières de **FinanceCore SA**.

Il offre aux décideurs une vision claire et en temps réel des performances financières ainsi qu’une analyse avancée des risques clients.

---

## 🎯 Objectifs

* Visualiser les performances globales (KPIs)
* Suivre l’évolution des transactions
* Analyser les risques clients
* Identifier les clients à fort risque
* Faciliter la prise de décision stratégique

---

## ⚙️ Technologies utilisées

* Python
* Streamlit
* Pandas
* Matplotlib
* Seaborn

---

## 📁 Structure du projet

```
Dashboard_FinanceCore/
│── app.py                # Page d'accueil (Bienvenue)
│── pages/
│   ├── 1_Vue_Executive.py
│   └── 2_Analyse_Risques.py
│── data/
│   └── data.csv
│── README.md
```

---

## 🚀 Fonctionnalités

### 🏠 Page d’accueil

* Présentation du dashboard
* Navigation vers les pages principales

---

### 📊 Vue Exécutive

* KPIs :

  * Volume total des transactions
  * Chiffre d'affaires (CA)
  * Nombre de clients actifs
  * Marge moyenne

* Visualisations :

  * 📈 Évolution mensuelle des transactions
  * 📊 CA par agence
  * 🥧 Répartition des segments clients

---

### ⚠️ Analyse des Risques

* 🔥 Heatmap de corrélation (score crédit, montant)
* 📍 Scatter plot (score crédit vs montant)
* 🚨 Top 10 clients à risque
* 📊 Distribution des scores crédit

---

### 🎛️ Filtres interactifs

* Agence
* Segment client
* Produit
* Période (année)

👉 Tous les graphiques se mettent à jour dynamiquement.

---

### 📥 Export des données

* Téléchargement des données filtrées en **CSV**

---

## ▶️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/nohasabb2005-spec/-Pilotage_Strat-gique_et_Gestion_des_Risques_pour_FinanceCore_SA.git
cd -Pilotage_Strat-gique_et_Gestion_des_Risques_pour_FinanceCore_SA
```



### 2. Lancer l'application

```bash
streamlit run app.py
```

---

## 📊 Données

Le projet utilise un fichier :

```
data/data.csv
```

### Colonnes principales :

* date_transaction
* montant
* type_operation
* score_credit
* nom_agence
* nom_segment
* nom_produit
* id_client

---

## 💡 Améliorations futures

* Connexion à une base de données (PostgreSQL)
* Intégration d’un modèle Machine Learning (scoring)
* Dashboard avec Plotly interactif
* Déploiement cloud (Streamlit Cloud / Docker)

---

## 👩‍💻 Auteur

Projet réalisé dans le cadre d’un apprentissage Data Engineering & Data Visualization.
Nouhaila Sabbar

---

