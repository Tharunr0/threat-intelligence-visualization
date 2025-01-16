import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def combine_data(local_data, api_data):
    """Combine local and API data."""
    combined = pd.concat([local_data, api_data], ignore_index=True)
    return combined
