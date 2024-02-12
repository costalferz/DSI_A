# def get_mean(df)
# This function should return the mean value of the sepal length, sepal width, petal length,
#  and petal width respectively from the Iris Plants Database grouped by class. The Iris Plants Database is given as the DataFrame in the input df.
# The return value should be a DataFrame that contains 4 columns corresponding to the attributes and 3 rows 
# for each class: Iris-setosa, Iris-versicolor, and Iris-virginicia respectively.

# def get_std(df)
# This function should return the standard deviation of the sepal length, sepal width, petal length, and petal width respectively from the Iris Plants Database grouped by class.
#  The Iris Plants Database is given as the DataFrame in the input df. The return value should be a DataFrame that contains 4 columns corresponding to the attributes and 3 rows
#  for each class: Iris-setosa, Iris-versicolor, and Iris-virginicia respectively.

# def get_median(df)
# This function should return the median of the sepal length, sepal width, petal length, and petal width respectively from the Iris Plants Database grouped by class. 
# The Iris Plants Database is given as the DataFrame in the input df. The return value should be a DataFrame that contains 4 columns corresponding to the attributes and 
# 3 rows for each class: Iris-setosa, Iris-versicolor, and Iris-virginicia respectively.

# You should test these functions with the Iris Plant Dataset, which can be read using the readcsv in the Read CSV assignment.




import pandas as pd
def get_mean(df):
    return df.groupby(["class"]).mean()
def get_std(df):
    return df.groupby(["class"]).std()
def get_median(df):
    return df.groupby(["class"]).median()