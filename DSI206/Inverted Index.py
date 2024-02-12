# Write a program to compute the inverted index of the given words from a set of sentences. 
# The first line is a number of sentences, n. The next n lines are n sentences in the set. 
# At line n+2 is the number of words k that we want to compute the inverted index. Then,
#  the next k lines are the words that you need to compute the inverted index. For output, print the sentence numbers (start from 1) 
# corresponding to the inverted index of each word, separated by space.

# Input     	         
# 3	                    
# This is a book.	      
# That is a good book.	
# You are a good person	
# 2	
# book	
# good	
# Output
# 1 2
# 2 3
# NB: The first line of output is 1 2 because the word book appears in sentence number 1 and 2, while the second line is 2 3 because the word good appears in sentence number 2 and 3.


n = int(input()) # 3
text = []
text_check = []
for i in range(n):
    word = str(input()).replace(".","")
    word = word.split()
    text.append(word)

time = int(input())
for o in range(time):
    text_check.append(str(input()))

ans = ""
for j in text_check:
  for i in text:
    if j in i:
      ans += str(text.index(i) + 1) + " "
  print(ans.rstrip())
  ans = ""