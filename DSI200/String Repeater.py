# Write Python code that take one input string s and one integer n. Then, print out string s for n times. E.g.,

# Input	Output
#  Ha	HaHaHaHa
#  4	


s = str(input())
n = int(input())
for i in range(n):
    print(s ,end="")