import pandas as pd

df = pd.read_csv("Week 12/food_db.csv")

# Task 1
print(df.shape)
print(df)

# Task 2
new_df = df.replace({"discount":{"10%": "13%", "5%": "13%"}})
new_df = df.replace(to_replace=['5%', '10%'], value='13%')
print(new_df)

# Task 3
new_df = df.replace({"rating": {"Excellent": "4", "Very Good": "3", "Good": "2", "Average": "1"}})
new_df = df.replace(['Excellent', 'Very Good', 'Good', 'Average'], [4,3,2,1])
# new_df['rating'] = new_df['rating'].astype(int)

print(new_df)