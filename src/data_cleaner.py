import pandas as pd

def clean_data(df):
    """Clean and preprocess the dataset."""
    # Remove any rows with missing values
    df = df.dropna()
    
    # Convert 'year' to datetime
    df['year'] = pd.to_datetime(df['year'], format='%Y')
    
    # Ensure numeric columns are of the correct type
    numeric_columns = ['runtime_minutes', 'bond_kills', 'imdb_rating', 'rotten_tomatoes_rating']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    return df
