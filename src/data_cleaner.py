import pandas as pd

def clean_data(df):
    """Clean and preprocess the dataset."""
    # Remove any rows with missing values
    df = df.dropna()
    
    # Convert 'year' to datetime
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    
    # Ensure numeric columns are of the correct type
    numeric_columns = ['Film_Length', 'Kills_Bond', 'Avg_User_IMDB','Avg_User_Rtn_Tom']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    return df
