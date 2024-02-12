# Write Python code that take one input number n. Then, print out an isosceles triangle using the asterisk (*). E.g.,

# Input	Output
#   4	  *
#        ***
#       *****
#      *******
# NB: There are spacebars before the asterisk(s) but not after.
user = int(input())
j=0
for i in range(user):
    j=j+1
    print(' '*(user-i-1)+'*'*(i+j))