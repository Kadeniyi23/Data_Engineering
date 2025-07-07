# Databricks notebook source
# DBTITLE 1,Start Spark Session
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print("Spark session created")

# COMMAND ------
#Checking the contents of both dataframes

orders_df=spark.sql("select * from df_orders")

orders_df.show()

items_df=spark.sql("select * from df_items")

items_df.show()

# COMMAND ------
#Checking the 10 most popular pizza
most_pop_pizza=spark.sql("select pizza_name as Pizza,\
                           sum(quantity) as Total_requested \
                           from items_df \
                           join orders_df on items_df.pizza_id = orders_df.pizza_id\
                           group by pizza_name \
                           order by Total_requested desc\
                           limit 10")

display(most_pop_pizza)

#using seaborn to visualize
import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(data=most_pop_pizza,x="Pizza",y="Total_requested")
plt.show()

#checking the most popular categories
most_pop_cat= spark.sql("select pizza_category as Category,\
                         count(*) as Total_requested\
                         from items_df \
                         join orders_df on items_df.pizza_id = orders_df.pizza_id\
                         group by pizza_category \
                         order by Total_requested desc")

sns.catplot(data=most_pop_cat,x="Category",y="Total_requested")
plt.show()

#importing functions to categorize the year month and date
from pyspark.sql.functions import year, date_format, dayofmonth, hour, when, col


#categorizing the dates and times
more_complex_df= orders_df.withColumn("year", year("order_date")) \
       .withColumn("month_name", date_format("order_date", "MMMM")) \
       .withColumn("day_of_month", dayofmonth("order_date")) \
       .withColumn("time_of_day", when((hour("order_date") >= 9) & (hour("order_date") <= 12), "Morning")
                                    .when((hour("order_date") >= 12) & (hour("order_date") <= 15), "Afternoon")
                                    .when((hour("order_date") >= 15) & (hour("order_date") <= 18), "Evening")
                                    .otherwise("Night"))

# Count frequencies
month_counts = more_complex_df['month_name'].value_counts().reset_index()
month_counts.columns = ['month', 'count']

time_counts = more_complex_df['time_of_day'].value_counts().reset_index()
time_counts.columns = ['time_of_day', 'count']

# ✅ Create Seaborn plots side by side
plt.figure(figsize=(14, 6))

# Plot 1: Popular Months
plt.subplot(1, 2, 1)
sns.barplot(x='month', y='count', data=month_counts, palette='Blues_d')
plt.title('Most Popular Months')
plt.xticks(rotation=45)

# Plot 2: Popular Time of Day
plt.subplot(1, 2, 2)
sns.barplot(x='time_of_day', y='count', data=time_counts, palette='Oranges_d')
plt.title('Most Popular Times of Day')

plt.tight_layout()
plt.show()
