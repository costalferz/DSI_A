# Write the following Python function,

# def kth_largest_element(arr, k)
# that takes two input parameters. The first parameter arr is the list of numbers. The second parameter is the value of k. 
# The function should return the element in the list that is the $k$-th largest element.

# Example

# Consider the following function call:

# >>> print(kth_largest_element([1,5,9,3,7], 2))
# This statement should return

# 7
# NB: 7 is the second largest value in the list

def kth_largest_element(arr, k):
    arr.sort()
    if k ==1:
        return arr[-1]
    return arr[len(arr)-k]
print(kth_largest_element([1,5,9,3,7],2))