# Write the following Rectangle class in Python,

# class Rect(object)
# The constructor function of Rect class should have two parameters, width and height, to initialize the instance variables, width and height,

# The Rect class has two member functions: area and circumference.

# def area(self)
# The member function area should return the area of the rectangle.

# def circumference(self)
# The member function circumference should return the circumference of the rectangle.

# Example

# Consider the following function call:

# >>> a = Rect(3,4)
# >>> print(a.area())
# >>> print(a.circumference())
# This statement should return

# 12
# 14
class Rect(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def circumference(self):
        return (2*self.width)+(2*self.height)