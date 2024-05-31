from matplotlib import pyplot as plt
import pandas as pd

df_sales = pd.read_excel("Week 12/linechart.xlsx")
# print(df_sales.head())

plt.figure(figsize=(12,4))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="blue", label="Fridge")
plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color="yellow", label="Dishwasher")
plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color="Red", label="Washing Machine")
plt.title("Sales Statistic")
plt.ylabel("Revenue in mln USD")
plt.xlabel("Quarter")
plt.legend()
plt.show()

total_sales = df_sales[["Fridge", "Dishwasher", "Washing Machine"]].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.2f%%', startangle=100, explode=(0.1,0.1,0.1), shadow=True)
plt.show()

df_sales.plot(kind="bar", x="Quarter")
plt.title("Sales Statistic")
plt.ylabel("Revenue in mln USD")
plt.xlabel("Quarter")

plt.xticks(rotation=45)
plt.show()

df_score = pd.read_excel("Week 12/histograms.xlsx")
plt.hist(df_score["Exam_Score"])
plt.show()