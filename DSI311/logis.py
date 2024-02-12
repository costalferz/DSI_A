import numpy as np
import math

def one_hot_encoder(target):

    target_name, y = np.unique(target, return_inverse=True)
    one_hot = np.zeros((y.size, y.max()+1))
    one_hot[np.arange(y.size),y] = 1
    return target_name, one_hot

def add_intercept(X):

    intercept = np.ones((X.shape[0], 1))
    return np.concatenate((intercept, X), axis=1)

def softmax(x):

    softmax = np.exp(x)
    softmax /= np.sum(softmax, axis=1, keepdims=True)
    return softmax

def loss_func(h, y):

    loss = - np.sum(y * np.log(h)) / y.shape[0]
    return loss
def find_gradient(X, h, y):

    g = np.dot(X.T, (h - y)) / y.shape[0]
    return g

def fit(X, y, lr, num_iter):

    X = add_intercept(X)
    
    # weights initialization
    theta = np.zeros((X.shape[1], y.shape[1]))

    for i in range(num_iter):
        z = np.dot(X, theta)
        h = softmax(z)
        loss = loss_func(h, y)
        gradient = find_gradient(X, h, y)
        theta -= lr * gradient
            
        if(i % 1000 == 0):
            print(f'Iter {i:4d} \t loss: {loss:.4f} \t')
    print(f'Iter {i:4d} \t loss: {loss:.4f} \t')
    return theta

def predict_prob(X, theta):

    X = add_intercept(X)
    return softmax(np.dot(X, theta))

def predict(X, theta):

    return predict_prob(X, theta).argmax(axis=1)

def find_accuracy(y, prediction):

    acc = sum(y.argmax(axis=1) == prediction) / len(y)
    return acc

if __name__ == "__main__":
    data = np.loadtxt('iris.data', delimiter=',', usecols=(0,1))
    target = np.loadtxt('iris.data', delimiter=',', usecols=(4), dtype='str')

    # hyperparameters
    lr = 0.1
    num_iter=10000

    # preprocessing data
    X = data
    target_name, y = one_hot_encoder(target)
    
    # fit Logistic Regression model
    theta = fit(X, y, lr, num_iter)
    preds = predict(X, theta)

    print(f'Accuracy = {find_accuracy(y, preds):.3f}')
    print(f'Predictions  = {preds}')
    print(f'Groudn Truth = {y.argmax(axis=1)}')