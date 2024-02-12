# Write Python code that counts the number of the odd number in the given list. 
# The first line of the input consists of one number, n, which is the length of the list. 
# The following n lines contain an integer, which is an element of the list. The output must consists only one number, which is the number of odd number in the list.

# E.g.,

# Input	    Output
# 5	          2
# 2	
# 4	
# 5	
# 1	
# 4	
x,y = [],[]
user = int(input())
for i in range(user):
    u = int(input())
    x.append(u)
for j in range(user):
    if x[j]%2 != 0:
        y.append(x[j])
print(len(y))