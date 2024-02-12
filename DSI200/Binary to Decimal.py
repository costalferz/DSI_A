# Write the following Python function,

# def binary2decimal(b)
# that takes one input string, b, which is a string of binary number. 
# The function should return an integer, which is the decimal number that is equivalent to the binary number b.

# Example

# Consider the following function call:

# >>> print(binary2decimal('1101'))
# This statement should return

# 13
# NB: 1101 in binary is equivalent to 13 in decimal.

def binary2decimal(b): 
    decimal,power = 0,0 
    b = list(str(b)) 
    b = b[::-1]  
    for number in b: 
        if number == '1': 
            decimal += 2**power     
        power += 1 
    return decimal