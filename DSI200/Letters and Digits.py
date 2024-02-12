# Write Python code that counts the number of occurrences of the English alphabet and the digits in the given sentence.
#  The input consists of one line, which is the sentence. The output must consists of two lines. The first line show number of English letter frequency.
#  The second line show the digit frequency.

# E.g.,

# Input	       Output
# Sarun 1234	 5
#                4
s = input()
d,l=0,0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print(l)
print(d)
