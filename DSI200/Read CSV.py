# def readcsv(url)
# This function should read the CSV file given in the input url and return as the DataFrame. 
# The given CSV has neither the header nor the index column so the columns should be call sepal length, sepal width, petal length, petal width, and class respectively 
# (the given CSV file is guaranteed to have exactly 5 columns).

# def get_stats(df)
# This function should return the descriptive statistics of the input DataFrame df. 
# The output should be a DataFrame that contains 8 rows: count, mean, std, min, 25%, 50%, 75%, and max (std = standard deviation; 25%, 50%, 75% are percentiles).
#  Each row contain 4 columns corresponding to sepal length, sepal width, petal length, and petal width respectively.

# Hint: Look at describe function, https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html.

# You should test the readcsv function with the Iris Plants Database using the following URL, 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data. 
# For more details, see https://archive.ics.uci.edu/ml/machine-learning-databases/iris/


import pandas as pd
def readcsv(url):
    column = ['sepal length','sepal width','petal length','petal width','class']
    data = pd.read_csv(url, names=column)
    return data
def get_stats(df):
    b = pd.DataFrame(df)
    return b.describe()