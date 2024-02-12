# Write Python code that counts the number of occurrences of each English alphabet in the given sentence. 
# The input consists of one line, which is the sentence. The output should show only the alphabets that appear in the sentence in the alphabetical order. 
# Each line of the output consists of only one letter and a number indicating the letter frequency, separated by a single space bar.


# Input	            Output
# a b c dd	        a 1
#                   b 1
#                   c 1
#                   d 2
# Hints: Use ord and chr functions to convert between character and number.

s = input()
count = {}
s_word = [' ','.','@','!','0','1','2','3','4','5','6','7','8','9','$','^']
for char in s:
    if char in s_word:
        i=0
    elif char not in count:
        count[char] = 1
    else:
        count[char] +=1
new_count = dict((k.lower(),v) for k,v in count.items())
for i in sorted(new_count.keys()):
    print(i,new_count[i])