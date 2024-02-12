# Write Python code that take one input number n. Then, print out a right triangle with equal sides using the asterisk (*)
# , whose sides lie on the left and the bottom of the screen. E.g.,

# Input	Output
# 5	    *
#       **
#       ***
#       ****
#       *****
user_input = int(input())
for i in range(user_input):
    print("*"*(i+1))