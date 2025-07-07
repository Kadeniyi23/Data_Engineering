#Importing libraries

import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#Creating the connection
conn=create_engine("mysql+pymysql://{user}:{pw}@localhost:{host}/{db}"
                   .format(user= "KABIRAT",
                           pw = "password",
                           host = 42333,
                           db = "Car_sales"))

#The path to the file
Path= r'C:\Users\KabiratAdeniyi\Docker\Apache_pyspark\data\car_prices.csv'

Cars_df=pd.read_csv(Path)

#Creating a table with the function table
def cars(df):
    """This function saves the data into the Car sales table"""
    df = df[["year","make","model","trim","body","transmission","vin","state","condition","odometer",
             "color","interior","seller","mmr","sellingprice","saledate"]]

    df.tosql(name="Car_Sales", con=conn,if_exists="replace",index=True)

    return df



