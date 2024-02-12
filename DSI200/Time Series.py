# In this assignment, the CSV file is given, orders.csv, in the Google Classroom. You need the file to complete this assignment. 
# The file contains the details of orders such as order date and amount.

# Write the two following Python functions for handling time series data.

# def index_by_date(df)
# The input df is the DataFrame of orders.csv. This function should set the order_date of the orders DataFrame, 
# the input df, as the index using the pandas.DatetimeIndex and sort by date in the descending order.

# def filter_by_date(df, st, en)
# The input df is the DataFrame of orders.csv. st and en is the start date and the end date. 
# The function should return the DataFrame of orders whose order_date is within the start and the end date. 
# It is guaranteed that the start date always precedes the end date.


import pandas as pd
def index_by_date(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df.sort_values('order_date',ascending=False).set_index('order_date')
def filter_by_date(df,st,en):
    st,en=pd.to_datetime(st),pd.to_datetime(en)
    return df[(df.index>=st)&(df.index<=en)]