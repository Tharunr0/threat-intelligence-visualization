import requests
import pandas as pd

API_URL = "https://api.threatintel.com/data"

def fetch_data():
    """Fetch data from a threat intelligence API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error fetching API data: {e}")
        return pd.DataFrame()
