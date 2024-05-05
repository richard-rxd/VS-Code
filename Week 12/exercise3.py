import pandas as pd

def classify_year(year):
    if year < 2000:
        return "Before 2000"
    return "From 2000"

df = pd.read_csv("Week 13/movies.csv")

print(df.head(5))

df["year_classify"] = df["release_year"].apply(classify_year) # ODER MIT LAMBDA: = df.apply(lambda x: 'Before 2000' if x['release_year'] < 2000 else 'From 2000', axis=1)

print(df.head(5))

df.to_csv("final_movie_data.csv", index=False, columns=['title', 'budget', 'revenue', 'year_classify'])