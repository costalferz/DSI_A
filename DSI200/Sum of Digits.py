# Write Python code that take one input number and find the sum of the digits of this number until there is only one digit left.


# Input	Output
# 7864	  7

# First, 7+8+6+4 = 25. Then, 2+5=7.

user_input = int(input())
sum = 0
while user_input>0:
    digit = user_input%10
    sum = sum+digit
    user_input = user_input//10
total = 0
while sum>0:
    n = sum%10
    total = total+n
    sum = sum//10
if total!=18:
    print(total)
else:
    print(total/2)