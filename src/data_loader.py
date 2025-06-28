import pandas as pd

def load_data(url):
    """Loads dataset from the provided URL"""
    df = pd.read_csv(url)
    return df
