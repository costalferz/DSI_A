# Write the Python function that perform matrix multiplication between two 2D numpy array.

# def matrix_multiplication(A, B)
# The function should take two 2D numpy array inputs, A and B. Then, the function 
# should return the matrix multiplication of A and B. For more details about matrix multiplication, see https://en.wikipedia.org/wiki/Matrix_multiplication.

import numpy as np
def matrix_multiplication(A,B):
    a = np.array(A)
    b = np.array(B)
    c = np.dot(a,b)
    return c