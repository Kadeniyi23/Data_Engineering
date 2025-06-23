# Import libraries
import pandas as pd 
import numpy as np
from sqlalchemy import create_engine

# Establish the connection
conn = create_engine("mysql+pymysql://{user}:{pw}@localhost:{host}/{db}"
                       .format(user = "user",
                               pw = "password",
                               host = 42333,
                               db = "Sales_Data_US"))

# Change the path if you have your xls dataset somewhere else
file_location = r'C:\Users\KabiratAdeniyi\Docker\Sales_Data_US\assets_files\Super_store_sales.xlsx'

basic = pd.read_excel(file_location, sheet_name = 0)


def customers_tbl(df):
    """The function saves customer details to mysql customers table"""
    #split the full name column to first name & last name
    df[['customer_first_name', 'customer_last_name']] = df['Customer Name'].str.split(' ', expand = True)
    
    #rename multiple column names by label
    df.rename(columns={'Customer ID':'customer_id'}, inplace = True)
    df.rename(columns={'Segment':'segment'}, inplace = True)
    df.rename(columns={'Country': 'country'}, inplace=True)
    df.rename(columns={'City': 'city'}, inplace=True)
    df.rename(columns={'State': 'state'}, inplace=True)
    df.rename(columns={'Region': 'region'}, inplace=True)

    #save to database
    df = df[['customer_id', 'customer_first_name', 'customer_last_name','segment','country','city','state','region']]
    df.to_sql(name = 'CUSTOMER', con = conn, if_exists = 'append', index = False)
    
    return df





def products_tbl(df):
    """The function saves products details to mysql products table"""

    #rename multiple column names by label
    df.rename(columns={'Product ID':'product_id', 'Product Name':'product_name','Sub-Category':'sub_category','Category':'category'}, inplace = True)

    df=df[['product_id','product_name','sub_category','category']]
    #save to database
    df.to_sql(name = 'PRODUCT', con = conn, if_exists = 'append', index = False)

    return df





def orders_tbl(df):
    """The function saves orders details to mysql salesorders table"""
    df.rename(columns={'Order ID':'order_id','Order Date':'order_date','Ship Date':'ship_date','Ship Mode':'ship_mode','Customer ID':'customer_id','Product ID':'product_id'}, inplace = True)

    df= df[['order_id','order_date','ship_date','ship_mode','customer_id','product_id']]

    df.to_sql(name = 'sales_order', con = conn, if_exists = 'append', index = False)

    return df


def main():
    customers_tbl(basic)
    products_tbl(basic)
    orders_tbl(basic)
if __name__ == '__main__':
    main()