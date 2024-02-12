from os import pread
import numpy as np
import matplotlib.pyplot as plt


def distance(a, b):
    """
    Find Euclidian distance between two vectors
    Input:  a = 1D array vector
            b = another 1D array vector
    Output: Euclidian distance between vectors a and b
    """
    dist = np.sqrt(np.sum((a - b)**2))
    return dist

def knn(sample, data, target, k=1):
    """
    Make prediction using K-Nearest Neighbor technique
    Input:  sample = 1D array vector of the sample we want to predict its class
            data = 2D array of data, each row is the instance, each column is the attribute.
            target = 1D array indicating the class of each row in data
            k = the parameter
    Output: the predicted class of the sample
    """
    distances = []
    for r in data:
        dist = distance(sample, r)
        distances.append(dist)
    neighbors = list(enumerate(distances))
    idx = sorted(neighbors, key=lambda x: x[1])[:k]
    nb = [data[idx[i][0]] for i in range(k)]
    output = []
    for i in range(len(nb)):
        for j in range(data.shape[0]):
            if nb[i][0] == data[j][0] and nb[i][1] == data[j][1]:
                output.append(target[j])
    predict = max(set(output), key=output.count)
    return predict

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