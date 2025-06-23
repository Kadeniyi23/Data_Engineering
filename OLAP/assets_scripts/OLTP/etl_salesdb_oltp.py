# Import libraries
import pandas as pd 
import numpy as np
from sqlalchemy import create_engine
import os

# Establish the connection
conn = create_engine("mysql+pymysql://{user}:{pw}@localhost:{host}/{db}"
                       .format(user = "user",
                               pw = "password",
                               host = 42333,
                               db = "Brazilian_Supermarket_Sales"))

#pATH TO FILE
file_location = r'C:\Users\KabiratAdeniyi\Docker\E_commerce_Brazilian_Supermarket\OLAP\assets_files'

customers = pd.read_csv(os.path.join(file_location, 'df_Customers.csv'))
products = pd.read_csv(os.path.join(file_location, 'df_Product.csv'))
orders = pd.read_csv(os.path.join(file_location, 'df_Orders.csv'))
order_items = pd.read_csv(os.path.join(file_location, 'df_OrderItems.csv'))
payments = pd.read_csv(os.path.join(file_location, 'df_Payments.csv'))

Compiled_orders = orders.merge(order_items, how='left', on='order_id').merge(payments, how='left', on='order_id')


def customers_tbl(df):
    """The function saves customer details to mysql customers table"""

    #rename multiple column names by label
    df.rename(columns={'customer_zip_code_prefix':'zip_code'}, inplace = True)
    df.rename(columns={'customer_city': 'city'}, inplace=True)
    df.rename(columns={'customer_state': 'state'}, inplace=True)
    #save to database
    df = df[['customer_id', 'zip_code','city','state']]
    df.to_sql(name = 'CUSTOMER', con = conn, if_exists = 'append', index = False)
    
    return df





def products_tbl(df):
    """The function saves products details to mysql products table"""

    df=df[['product_id','product_category_name','product_weight_g','product_length_cm','product_height_cm','product_width_cm']]
    #save to database
    df.to_sql(name = 'PRODUCT', con = conn, if_exists = 'append', index = False)

    return df





def orders_tbl(df):
    """The function saves full order details to MySQL `ORDER` table."""

    # Rename columns if needed to match SQL schema exactly
    df = df[[
        'order_id',
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_timestamp',
        'payment_sequential',
        'payment_type',
        'payment_installments',
        'payment_value',
        'shipping_charges',
        'price',
        'order_status',
        'customer_id',
        'product_id',
        'seller_id'
    ]]

    # Write to MySQL table
    df.to_sql(name='ORDER', con=conn, if_exists='append', index=False)

    return df



def main():
    customers_tbl(customers)
    products_tbl(products)
    orders_tbl(Compiled_orders)
if __name__ == '__main__':
    main()