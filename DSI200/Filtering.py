# Write the following Python function:

# def filtering(arr, low=-np.inf, high=np.inf)
# The function should take 3 inputs: a N-D numpy array, arr, and two numbers, low and high.
# The function should return a 1D numpy array that contains the members of arr whose value is within the range of [ low, high ].

import numpy as np 
def filtering(arr, low=-np.inf, high=np.inf):
    arr=arr.reshape(-1)
    b=arr[(arr>=low)&(arr<=high)]
    return b