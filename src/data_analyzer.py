import pandas as pd
import numpy as np

def analyze_ratings_correlation(df):
    """Analyze correlation between IMDb and Rotten Tomatoes ratings."""
    return df['Avg_User_IMDB'].corr(df['Avg_User_Rtn_Tom'])

def analyze_movie_lengths(df):
    """Analyze movie lengths over time."""
    #group = df['Year']//10*10  # or df['year'].round(-1)
    #grouped = df.groupby([group])['Film_Length'].mean()
    #return grouped
    return df.groupby(df['Year'].round(-1))['Film_Length'].mean()

def analyze_kills_vs_ratings(df):
    """Analyze relationship between Bond's kills and movie ratings."""
    df_renamed = df.rename(columns={"Kills_Bond": "Bond's Kills", "Avg_User_IMDB": "IMDB rating","Avg_User_Rtn_Tom":"Rotten Tomatoes rating"})
    return df_renamed[["Bond's Kills", "IMDB rating", "Rotten Tomatoes rating"]].corr()
