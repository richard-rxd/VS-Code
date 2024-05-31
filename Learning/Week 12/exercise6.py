import pandas as pd

df = pd.read_csv("Week 12/movies_data.csv")
print(df)

# Task 2
g = df.groupby("industry")
print(g.size())
print(g.get_group("Bollywood"))

# Task 3
def grouper(df, idx, col):
    if 1 <= df[col].loc[idx] <= 3.9:
        return 'Poor'
    elif 4 <= df[col].loc[idx] <= 7.9:
        return 'Average'
    elif 8 <= df[col].loc[idx] <= 10:
        return 'Good'
    else:
        return "others"

g = df.groupby(lambda x: grouper(df, x, 'imdb_rating'))

for x, y in g:
    print("Rating: ", x)
    print("Movies: \n", y)