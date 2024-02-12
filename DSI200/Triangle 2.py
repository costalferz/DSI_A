# Write Python code that take one input number n. Then, print out a right triangle with equal sides using the asterisk (*)
# whose sides lie on the right and the bottom of the screen. E.g.,

# Input	   Output
# 5	           *
#             **
#            ***
#           ****
#          *****

user = int(input())
for i in range(user):
    print(' '*(user-i-1)+'*'*(i+1))