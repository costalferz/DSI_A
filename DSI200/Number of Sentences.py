
# def number_of_sentences(text_filename)
# that takes one input parameter, which is the text file name. The function should return the number of sentences in the text file. 
# It is guarantee that every sentence ends with a full stop (.), all abbreviations omit the full stop, and no decimal points exist in the text file.

# Example

# Consider the following function call:

# >>> print(number_of_sentences('text.txt'))
# This statement should return

# 8
# NB: text.txt file contains 8 sentences.

def number_of_sentences(text_filename):
    f = open(text_filename, "r").read()
    return f.count(".")