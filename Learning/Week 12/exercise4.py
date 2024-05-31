import pandas as pd

df = pd.read_csv("Week 12/fruits_data.csv")

# Task 1
print("Rows and Columns: ", df.shape)
print(df.columns)
print(df)

# Task 2
new_df = df.fillna(-1)
print(new_df)

# Task 3
# new_df = df
# new_df = new_df.rename(columns={
#     "apple(1kg)": "apples",
#     "banana(1 dozen)": "bananas",
#     "grapes(1kg)": "grapes",
#     "mango(1kg)": "mangos",
#     "Water Melons(1)": "Watermelons"
# })

# new_df = new_df.fillna({
#     "apples":  new_df.apples.mean(),
#     "bananas": new_df.bananas.mean(),
#     "grapes": new_df.grapes.median(),
#     "mangos": new_df.mangos.median(),
#     "Watermelons": "Not Available"
# })

new_df = df.fillna({
        'apple(1kg)': df['apple(1kg)'].mean(),
        'banana(1 dozen)': df['banana(1 dozen)'].mean(),
        'grapes(1kg)': df['grapes(1kg)'].median(),
        'mango(1kg)': df['mango(1kg)'].median(),
        'Water Melons(1)': "Not Available",
        
    })

print(new_df)

# Task 4
new_df = df.ffill()
# new_df = df.fillna(method="ffill")
print(df)
print(new_df)

# Task 5
new_df = df.dropna(thresh=4)
print(new_df)

# Task 6
new_df = df.dropna(how="any")
print(new_df)

new_df.to_csv("final_data.csv", index=False)