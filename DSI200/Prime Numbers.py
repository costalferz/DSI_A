# Write Python code that find all the prime numbers whose value is less than the given threshold. The input consists of only one number,
#  n, which is the threshold. The output must display one prime number per line in the ascending order.

# E.g.,

# Input	  Output
# 10	    2
#           3
#           5
#           7


num_int = int(input())
x = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
j = 0
if num_int>1:
    for i in range(2,num_int):
        if (num_int>=x[j]):
            print(x[j])
        j=j+1