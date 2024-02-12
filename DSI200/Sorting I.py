# Write Python code that sort the given list of integers. The first line of the input consists of one number, n, 
# which is the length of the list. The following n lines contain an integer, which is an element of the list. 
# The output must display one element of the list per line in the ascending order.

# E.g.,

# Input	       Output
#   5	        1
#   1	        2
#   3	        3
#   5	        4
#   2	        5
#   4	
# Hints: Use sorted function

x,y = [],[]
user_input = int(input())
for i in range(user_input):
    u = int(input())
    x.append(u)
x.sort()
for j in range(user_input):
    print(x[j])