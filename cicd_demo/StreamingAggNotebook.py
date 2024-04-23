# Databricks notebook source
# MAGIC %md Sample notebook showing a spark streaming job

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum
import pandas as pd
import time

spark = SparkSession.builder.appName("Streaming Agg").getOrCreate()

df = spark.readStream.format("rate") \
  .option("rowsPerSecond", 1000) \
  .load()

def pandasAggregateByMs(pdf):
  pdf['timestamp'] = pd.to_datetime(pdf['timestamp'])
  pdf['first_millisecond_digit'] = pdf['timestamp'].dt.microsecond // 1000 % 10
  pdf['first_millisecond_digit'] = pdf['first_millisecond_digit'].astype('int64')
  return pdf.groupby('first_millisecond_digit')['value'].sum().reset_index().rename(columns={'value': 'total_value'})

def aggregateByMs(df, epochId):
  if epochId == 1:
    result = pandasAggregateByMs(df.toPandas())
    print(result)

writeQuery = df.writeStream \
  .format("console") \
  .trigger(processingTime="2 seconds") \
  .foreachBatch(aggregateByMs) \
  .start()

time.sleep(8)

writeQuery.stop()