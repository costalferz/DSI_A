# Write Python code that convert temperature in Celsius to Fahrenheit. The answer must have 0 decimal places. 
# The decimal point that is equal or higher than .5 must be rounded up, otherwise round down. (Use F = (C * 9 / 5) +32) E.g.,

# Input	Output
#   0	 32
import math
C = int(input())
F = (C*9/5)+32
print(math.ceil(F))