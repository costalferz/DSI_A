# Write the Python function that perform the normalization. Given the 2D array A, the normalization divide each cell by the sum of the corresponding row.

# def normalization(A)
# The function should take one 2D numpy array as an input. Then, it returns the 2D numpy array after the normalization.

# Example: Given the 2D array A as the following:

# [[1,3],
# [2,2],
# [1,4]]
# The result of the normalized array A is given below:

# [[0.25 0.75]
#  [0.5  0.5 ]
#  [0.2  0.8 ]]
# The sum of the first row is 1+3=4 so divide [1,3] by 4; therefore, the result is [0.25 0.75].

# The sum of the second row is 2+2=4 so divide [2,2] by 4; therefore, the result is [0.5 0.5].

# The sum of the third row is 1+4=5 so divide [1,4] by 5; therefore, the result is [0.2 0.8].
import numpy as np 
def normalization(A):
    B=np.sum(A,axis=1)
    C=B.reshape(-1,1)
    return A/C