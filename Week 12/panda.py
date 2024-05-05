import pandas as pd

df = pd.read_csv("/Users/richardwittich/VS Code/Week 13/movies.csv")

print(df.language.value_counts())
print(df[df.studio == "Marvel Studios"])

df["age"] = df["release_year"].apply(lambda x: 2023 - x)
print(df.head(5))
df["profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis = 1)
print(df.head(5))
df.set_index("title", inplace=True)
#print(df.head(5))
print(df.loc["Avengers: Infinity War"])
print(df.iloc[7])
df.reset_index(inplace=True)
