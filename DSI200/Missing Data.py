# In this assignment, the CSV file is given, orders.csv, in the Google Classroom. 
# You need the file to complete this assignment. The file contains the details of orders such as order date and amount.

# Write the three following Python functions for handling missing data in different ways.

# def replace_mean(df)
# The input df is the DataFrame of orders.csv. This function should handle the missing data in the amount column by replacing with the mean value. 
# The mean value should computed by ignoring the missing data.

# def fill_gap_forward(df)
# The input df is the DataFrame of orders.csv. This function should handle the missing data in the amount column by propagating the last valid observation forward to the next.
#  E.g., if the amount in 6th row is missing but the amount in 5th row is available, then we fill the value in the 6th row by the value in the 5th row.

# def drop_row(df)
# The input df is the DataFrame of orders.csv. This function should handle the missing data in the amount column by removing the row that has missing data.

import pandas as pd
def replace_mean(df):
    df['amount'] = df['amount'].str.replace('$', '')
    df['amount'] = df['amount'].apply(float)
    df['amount'].fillna(df['amount'].mean(), inplace=True)
    return df
def fill_gap_forward(df):
    df['amount'].fillna(method='ffill',inplace=True)
    return df
def drop_row(df):
    return df.dropna(axis=0)