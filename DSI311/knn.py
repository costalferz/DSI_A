import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from math import sqrt

def distance(a, b):
    """
    Compute the distance between two vectors
    Input:  a = 1D array vector of the first vector
            b = 1D array vector of the second vector
    Output: the distance between the two vectors
    """
    return sqrt(np.sum((a - b)**2))

def knn(sample, data, target, k=1):
    """
    Make prediction using K-Nearest Neighbor technique
    Input:  sample = 1D array vector of the sample we want to predict its class
            data = 2D array of data, each row is the instance, each column is the attribute. X is the data matrix
            target = 1D array indicating the class of each row in data. Y is the target vector
            k = the parameter # k of K-Nearest Neighbor
    Output: the predicted class of the sample
    """

    distances = [distance(sample, row) for row in data]

    nearest = np.argsort(distances)[:k]

    votes = [target[i] for i in nearest]

    count = Counter(votes)

    winner = Counter(votes).most_common(1)[0][0]
    return winner


if __name__=='__main__':
    data = np.loadtxt('iris.data', delimiter=',', usecols=(0,1))
    target = np.loadtxt('iris.data', delimiter=',', usecols=(4), dtype='str')

    sample = np.array([4.5, 2.])
    print(knn(sample, data, target, k=3))
        
    classes = np.unique(target)
    plt.figure()
    for c in classes:
        plt.scatter(data[target==c,0],data[target==c,1], label=c)
    plt.scatter(sample[0], sample[1], color='r', marker='x')
    plt.legend()
    plt.title('Prediction = %s' % knn(sample, data, target, k=3))
    plt.axis('square')
    plt.show()