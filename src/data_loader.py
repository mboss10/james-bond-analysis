import pandas as pd

def load_data(file_path):
    """Load the James Bond movie dataset."""
    return pd.read_csv(file_path)
