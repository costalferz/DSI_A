# def number_of_words(text_filename)
# that takes one input parameter, which is the text file name. The function should return the number of words in the text file. 
# Sentences are defined as a list of words separated by white spaces.

# Example

# Consider the following function call:

# >>> print(number_of_words('text.txt'))
# This statement should return

# 224
# NB: text.txt file contains 224 words.

def number_of_words(text_filename):
    file = open(text_filename, "r").read().split()
    return len(file)