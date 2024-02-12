# Write the following Python function,

# def mean(*arr)
# that takes any number of input parameters. The function should return the mean value of all input parameters.

# Example

# Consider the following function call:

# >>> print(mean(1,2,3))
# This statement should return

# 2

def mean(*arr):
    n = len(arr)
    return sum(arr)/n
print(mean(1,2,3))