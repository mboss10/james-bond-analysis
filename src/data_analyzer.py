import pandas as pd
import numpy as np

def analyze_ratings_correlation(df):
    """Analyze correlation between IMDb and Rotten Tomatoes ratings."""
    return df['Avg_User_IMDB'].corr(df['Avg_User_Rtn_Tom'])

def analyze_movie_lengths(df):
    """Analyze movie lengths over time."""
    return df.groupby(df['Year'])['Film_Length'].mean()

def analyze_kills_vs_ratings(df):
    """Analyze relationship between Bond's kills and movie ratings."""
    return df[['Kills_Bond', 'Avg_User_IMDB', 'Avg_User_Rtn_Tom']].corr()
