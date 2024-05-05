import pandas as pd

movies_df = pd.read_csv("Week 12/movies2.csv")
languages_df = pd.read_csv("Week 12/languages.csv")
financials_df = pd.read_csv("Week 12/financials.csv")

print(movies_df.head(3))
print(languages_df.head(3))
print(financials_df.head(3))

# Task 2
movies_new_df = pd.read_csv("Week 12/new_movies.csv")

movies_df = pd.concat([movies_df, movies_new_df], ignore_index = True)

print(movies_new_df)
print(movies_df.tail(5))

# Task 3
movies_df = pd.merge(movies_df, languages_df, on="language_id")
print(movies_df.head(5))

# Task 4
movies_df = pd.merge(movies_df, financials_df, how="left", on="movie_id")
print(movies_df.tail(5))

# Task 5
movies_df.to_csv("final_complete_data.csv", index=False, columns=['movie_id', 'title', 'lang_name', 'budget', 'revenue', 'currency'])