#import the databricks session
from pyspark.sql import SparkSession
from sqlalchemy import Select

#generate the session
spark= SparkSession.builder.getOrCreate()

#to view all the restaurant_data
df = spark.sql('Select * from pizza_sales')

display(df)

#print the Schema
df.printSchema()

#show the description of the numerical values
df.describe().show()

#creating a table for the orders
order_columns=["pizza_id","order_id","quantity","order_date","order_time","total_price"]
df_orders = df.select(order_columns).drop_duplicates()
display(df_orders)



#finding the number of rows and columns
f"n_rows = {df_orders.count()}, n_cols = {len(df_orders.columns)}"

# Create table with path using DataFrame's schema and raise error if exist
df_orders.write.format("delta").saveAsTable("default.Orders")

#creating a table for the pizza items
item_columns = ["pizza_id","pizza_name_id","pizza_name","unit_price","pizza_size","pizza_category","pizza_ingredients"]
df_items=df.select(item_columns)
display(df_items)

#finding the number of rows and columns

f"n_rows = {df_items.count()}, n_cols = {len(df_items.columns)}"

# Create table with path using DataFrame's schema and raise error if exist

df_items.write.format("delta").saveAsTable("default.Items")