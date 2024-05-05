import pandas as pd

def standardize_currency(curr):
    if curr == "$$" or curr == "Dollars":
        return "USD"
    return curr

df_movies = pd.read_excel("/Users/richardwittich/VS Code/Week 13/movies_db.xlsx", "movies")
print(df_movies.head(5))

df_financial = pd.read_excel("/Users/richardwittich/VS Code/Week 13/movies_db.xlsx", "financials", converters = {"currency": standardize_currency })
print(df_financial.head(5))

df_merged = pd.merge(df_movies, df_financial, on="movie_id")
print(df_merged.head(5))