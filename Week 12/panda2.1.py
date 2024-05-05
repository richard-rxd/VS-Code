import pandas as pd

df = pd.read_csv("/Users/richardwittich/VS Code/Week 13/stock_data.csv", skiprows=2, names=["Ticker", "EPS", "Revenue", "Price", "People"], nrows=3, na_values=["n.a.", -1]) # List oder Dic möglich Beispiel: na_values={"People": ["n.a."]}

print(df)

df["PE"] = df.apply(lambda x: x["Price"] / x["EPS"], axis = 1)
df["P/E"] = df["Price"] / df["EPS"]
print(df)

df.to_csv("pe.csv", index=False, header=False)