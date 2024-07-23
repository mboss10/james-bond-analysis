import matplotlib.pyplot as plt
import seaborn as sns

def plot_ratings_correlation(df):
    """Plot correlation between IMDb and Rotten Tomatoes ratings."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Avg_User_IMDB', y='Avg_User_Rtn_Tom', data=df)
    plt.title("IMDb vs Rotten Tomatoes Ratings")
    plt.xlabel("IMDb Rating")
    plt.ylabel("Rotten Tomatoes Rating")
    plt.savefig('results/figures/ratings_correlation.png')
    plt.close()

def plot_movie_lengths_over_time(df):
    """Plot average movie lengths over decades."""
    avg_lengths = df.groupby(df['Year'])['Film_Length'].mean()
    plt.figure(figsize=(10, 6))
    avg_lengths.plot(kind='bar')
    plt.title("Average James Bond Movie Length by Year")
    plt.xlabel("Year")
    plt.ylabel("Film_Length")
    plt.savefig('results/figures/movie_lengths_over_time.png')
    plt.close()

def plot_kills_vs_ratings(df):
    """Plot heatmap of correlation between kills and ratings."""
    corr = df[['Kills_Bond', 'Avg_User_IMDB', 'Avg_User_Rtn_Tom']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation: Bond's Kills vs. Ratings")
    plt.savefig('results/figures/kills_vs_ratings_heatmap.png')
    plt.close()
