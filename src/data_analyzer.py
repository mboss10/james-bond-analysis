import pandas as pd
import numpy as np

def analyze_ratings_correlation(df):
    """Analyze correlation between IMDb and Rotten Tomatoes ratings."""
    return df['imdb_rating'].corr(df['rotten_tomatoes_rating'])

def analyze_movie_lengths(df):
    """Analyze movie lengths over time."""
    return df.groupby(df['year'].dt.decade)['runtime_minutes'].mean()

def analyze_kills_vs_ratings(df):
    """Analyze relationship between Bond's kills and movie ratings."""
    return df[['bond_kills', 'imdb_rating', 'rotten_tomatoes_rating']].corr()
