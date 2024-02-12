# In this assignment, two CSV files are given, orders.csv and customers.csv in the Google Classroom. 
# You need these files to complete this assignment. The first one contains the details of orders such as order date and amount; 
# while the latter contains the details about the customers such as name and address.

# Write the two following Python functions.

# def get_order_details()
# This function should merge the orders and customers DataFrames together. The merge should be done with orders as 
# the left DataFrame and customers as the right DataFrame. All orders must be preserved even if there are no matches on customers.
#  The two DataFrames should be merged based on customer_id.

# def get_customer_total_order()
# This function should return the customers DataFrame with an extra column, named count, which indicates the number of orders corresponding to the customers. 
# The customers who don't have any orders should have value 0 in the count column.

# Submit your code in main.py

import pandas as pd
def get_order_details():
    order = pd.read_csv('orders.csv')
    customer = pd.read_csv('customers.csv')
    return order.merge(customer,on = 'customer_id',how ='left')
def get_customer_total_order():
    df = get_order_details()
    customer = pd.read_csv('customers.csv')
    count = df[['customer_id','order_id']].groupby(['customer_id']).count()
    data = customer.merge(count,on='customer_id',how='left')
    data = data.rename(columns={'order_id':'count'})
    data['count'] = data['count'].fillna(0)
    return data