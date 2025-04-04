import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql import SparkSession

processed_path = "./data/processed_retail_sales"
df = pd.read_csv(f"{processed_path}/part-00000.csv")

subset = df[(df["SUPPLIER"] == "REPUBLIC NATIONAL DISTRIBUTING CO") & 
            (df["ITEM TYPE"] == "WINE")]

subset["date"] = pd.to_datetime(subset["YEAR"].astype(str) + "-" + subset["MONTH"].astype(str) + "-01")

plt.figure(figsize=(10, 6))
plt.plot(subset["date"], subset["total_retail_sales"], marker="o")
plt.title("Total Retail Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Retail Sales (USD)")
plt.grid(True)
plt.show()
