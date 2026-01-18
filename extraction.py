import os
from dotenv import load_dotenv
from notion_client import Client
import json
import pandas as pd
import sqlite3

def fetch_datasource(datasourceId:str):
    try:
        notion_token = os.getenv("NOTION_TOKEN")
        datasource_id = os.getenv("DATA_SOURCE_ID")
        notion = Client(auth=notion_token)
        response = notion.data_sources.query(data_source_id = datasource_id)

    except Exception as e:
        print("Erreur de connexion à notion API",e)
        return None
    
    print("Learnings Fetched")
    return response.get('results')

def extract_value(prop):
    """Extrait la valeur brute selon le type de propriété Notion."""
    prop_type = prop.get('type')
    
    if prop_type == 'title':
        titles = prop.get('title', [])
        return titles[0].get('plain_text') if titles else None
    elif prop_type == 'date':
        date_data = prop.get('date')
        return date_data.get('start') if date_data else None
    elif prop_type == 'select':
        select_data = prop.get('select')
        return select_data.get('name') if select_data else None
    elif prop_type == 'status':
        status_data = prop.get('status')
        return status_data.get('name') if status_data else None
    elif prop_type == 'url':
        return prop.get('url')
    return None

def sqlWrite(df_lesson):
    conn = sqlite3.connect('notion.db')
    df_lesson.to_sql('learnings', conn, if_exists='replace', index=False)
    conn.close()  
    print("✅ Base de données notion.db mise à jour.")


def main():
    load_dotenv()
    datasource_id = os.getenv("DATA_SOURCE_ID")
    
    learnings = fetch_datasource(datasource_id)
    
    if learnings:
        entries = []
        for lesson in learnings:
            properties = lesson.get('properties', {})
            row = {name: extract_value(obj) for name, obj in properties.items()}
            entries.append(row)
        
        df = pd.DataFrame(entries)

        # Transformation et Nettoyage
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        df['date_started'] = pd.to_datetime(df['date_started'])

        # Vérification
        print(df.info())
        print("\n--- Aperçu des données nettoyées ---")
        print(df.head())

        sqlWrite(df)
        
    else:
        print("Le script n'a récupéré aucune donnée.")

if __name__ == "__main__":
    main()