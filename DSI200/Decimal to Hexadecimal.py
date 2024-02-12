
# def decimal2hex(d)
# that takes one input integer, d, which is a decimal number. The function should return the hexadecimal number in string that is equivalent to the number d.

# Example

# Consider the following function call:

# >>> print(decimal2hex(255))
# This statement should return

# ff
# NB: 255 in decimal is equivalent to ff in hexadecimal.

def decimal2hex(d):
    return hex(d)[2::]