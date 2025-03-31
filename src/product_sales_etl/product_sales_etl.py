from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, avg as _avg
import json

with open("./config/config.json", "r") as f:
    config = json.load(f)

spark = SparkSession.builder.appName("RetailSalesAnalysis").getOrCreate()

input_path = "./data/product_sales.csv"
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

print("Schema:")
df.printSchema()
print("Sample Data:")
df.show(5)

aggregated_df = df.groupBy("YEAR", "MONTH", "SUPPLIER", "ITEM TYPE") \
    .agg(
        _sum("RETAIL SALES").alias("total_retail_sales"),
        _sum("RETAIL TRANSFERS").alias("total_retail_transfers"),
        _sum("WAREHOUSE SALES").alias("total_warehouse_sales"),
        _avg("RETAIL SALES").alias("avg_retail_sales")
    )

print("Aggregated Data:")
aggregated_df.show(5)

storage_account_name = config["storage_account_name"]
storage_account_key = config["storage_account_key"]
container_name = config["container_name"]

spark.conf.set(f"fs.azure.account.auth.type.{storage_account_name}.dfs.core.windows.net", "SharedKey")
spark.conf.set(f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net", storage_account_key)

output_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/processed_retail_sales"

aggregated_df.write.mode("overwrite").option("header", True).csv(output_path)

print("Data export completed successfully.")
spark.stop()
