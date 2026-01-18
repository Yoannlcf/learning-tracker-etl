# Notion Learning Tracker ETL 📊

Ce projet automatise l'extraction, la transformation et la visualisation de mes données d'apprentissage stockées dans Notion. Il s'inscrit dans ma spécialisation en **Data Engineering** avant d'intégrer la majeure Big Data & ML à l'**Efrei Paris**.

## 🏗️ Architecture du Projet

Le pipeline suit une architecture ETL classique :
1. **Extract** : Récupération des données brutes via l'API Notion (notion-client).
2. **Transform** : Nettoyage, normalisation des colonnes et typage des dates avec **Pandas**.
3. **Load** : Stockage des données transformées dans une base **SQLite** locale.
4. **Visualize** : Dashboard interactif via **Metabase** déployé sous **Docker**.



## 🛠️ Stack Technique

| Technologie | Usage |
| :--- | :--- |
| **Python 3.11** | Langage principal du pipeline |
| **Pandas** | Transformation et manipulation de données |
| **SQLite** | Base de données relationnelle légère |
| **Docker** | Conteneurisation de l'outil de BI (Metabase) |
| **Notion API** | Source de données |

## 🚀 Installation et Utilisation

### Prérequis
- Docker Desktop (avec virtualisation activée)
- Python 3.x et un environnement virtuel (`venv`)

### Exécution
1. Cloner le dépôt et installer les dépendances :
   ```bash
   pip install -r requirements.txt

2. Configurer le fichier .env avec vos accès Notion.
3. Lancer l'extraction :
   ```bash
   python main.py
4. Lancer Metabase via Docker :
   ```bash
   docker run -d -p 3000:3000 -v "${PWD}:/notion_project" metabase/metabase

### 📊 Visualisation & Business Intelligence
Le dashboard permet de suivre en temps réel la répartition de mes apprentissages (Data Engineering, IA, Jazz Manouche) et l'état d'avancement des objectifs.

### 💡 Logique SQL :
Pour plus de détails sur les indicateurs de performance (KPIs) et les requêtes analytiques utilisées (comme le calcul de stagnation days_stuck), consultez le dossier ./metabase/queries.md.

## 👨‍💻 Yoann Lehong Cheffson
### Diplômé BUT Informatique & Bachelor Science des données et IA (UQAC)
- Consultez mon [profil LinkedIn](https://www.linkedin.com/in/yoann-lehong-cheffson/)
- Consultez mon [Mon GitHub](https://github.com/Yoannlcf/My-Data-Journey/tree/main")
