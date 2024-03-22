import requests
import pandas as pd

# Liste des catégories avec leurs identifiants
categories = {
    "Absence d'aménagement": '8',
    "Aménagement mal conçu": '3',
    "Défaut d'entretien": '4',
    "Absence d'arceaux de stationnement": '5',
    "Véhicule ou objet gênant": '2',
    "Accident, chute, incident": '9',
    "Signalisation, marquage": '6',
    "Incivilité récurrente sur la route": '7',
    "Vol ou dégradation de vélo": '10',
    "Autre": '100',
    "Éclairage public insuffisant": '11'
}

def data_collection(start_date, end_date, url, category_filter=None, location_filter=None,
                    status_filter=None, approval_filter=None, scope_filter=None,
                    keyword_search=None, data_limit=None):
    try:
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'category_filter': category_filter,
            'location_filter': location_filter,
            'status_filter': status_filter,
            'approval_filter': approval_filter,
            'scope_filter': scope_filter,
            'keyword_search': keyword_search,
            'data_limit': data_limit
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        df = pd.DataFrame(resp.json())
        return df[df['categorie'] == categories["Absence d'aménagement"]]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None

def main():
    start_date = '2018-01-01'
    end_date = '2018-12-31'
    url = 'https://vigilo.bapav.org/get_issues.php'
    category_filter = categories["Absence d'aménagement"]
    location_filter = None
    status_filter = None
    approval_filter = None
    scope_filter = None
    keyword_search = None
    data_limit = None

    df = data_collection(start_date, end_date, url, category_filter, location_filter,
                         status_filter, approval_filter, scope_filter, keyword_search, data_limit)
    if df is not None:
        print(df)

if __name__ == '__main__':
    main()
