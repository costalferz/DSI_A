# def pixel2img(fn)
# The function should take one string input, fn, which is a file name. The file stores the image as a list of pixel 
# (for more details, see https://simple.wikipedia.org/wiki/Pixel). The function should return the numpy arrary of size h x w x 3, which is the original image.
#  The file has the following structure:

# h
# w
# P1,1_r P1,1_g P1,1_b
# P1,2_r P1,2_g P1,2_b
# ...
# P1,w_r P1,w_g P1,w_b
# P2,1_r P2,1_g P2,1_b
# ...
# Ph,w_r Ph,w_g Ph,w_b
# The first line contains one integer, h, which is the height of the image. The second line contains one integer, w,
#  which is the width of the image. The next h x w lines contain the pixel value as a list of three values corresponding to red, green, 
# and blue color of the pixel. The list of pixels are arranged in the top-to-bottom then left-to-right order.

# Hint: np.genfromtxt is a useful function for loading text file into a numpy array.

import numpy as np

def pixel2img(fn):
    text = open(fn,'r').read()
    text101=text.split()

    return np.genfromtxt(fn, dtype=np.float32, delimiter=" ", skip_header=2).reshape(int(text101[0]),int(text101[1]),3)