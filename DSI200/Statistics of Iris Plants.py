# Write the Python functions that compute the fundamental statistical values from the given data. Your code should contain the following functions.

# def get_mean(data)
# This function should return the mean value of the sepal length, sepal width, petal length, and petal width respectively 
# from the Iris Plants Database. The return value should be a 1D numpy array.

# def get_median(data)
# This function should return the median of the sepal length, sepal width, petal length, and petal width respectively 
# from the Iris Plants Database. The return value should be a 1D numpy array.

# def get_std(data)
# This function should return the standard deviation of the sepal length, sepal width, petal length, and petal width respectively 
# from the Iris Plants Database. The return value should be a 1D numpy array.

# def get_iris_data():
#     url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#     return np.genfromtxt(url, delimiter=',', usecols=(0,1,2,3))
# The code above is given for obtaining the Iris Plants Dataset in numpy array.

# More details about Iris Plants Database at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

import numpy as np

def get_iris_data():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    return np.genfromtxt(url, delimiter=',', usecols=(0,1,2,3))

def get_mean(data):
    return np.mean(data,axis=0)

def get_median(data):
    return np.median(data,axis=0)

def get_std(data):
    return np.std(data,axis=0)


if __name__=="__main__":
    iris = get_iris_data()
    print('Mean: ', get_mean(iris))
    print('Median: ', get_median(iris))
    print('STD: ', get_std(iris))