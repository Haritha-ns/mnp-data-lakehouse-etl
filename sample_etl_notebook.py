# Databricks PySpark Sample ETL Script

from pyspark.sql.functions import col, to_date

# Load raw data from the bronze layer
df_bronze = spark.read.option("header", True).csv("/mnt/bronze/client_data.csv")

# Data transformation: filter nulls and convert date
df_silver = df_bronze     .filter(col("invoice_amount").isNotNull())     .withColumn("invoice_date", to_date(col("invoice_date"), "yyyy-MM-dd"))

# Write to silver layer
df_silver.write.mode("overwrite").parquet("/mnt/silver/client_cleaned_data")
