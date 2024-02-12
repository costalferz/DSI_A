# Write the following Python decorator function,

# def output_decorator(f)
# that takes a function, f, and reformats the output. The function f find the area of the rectangle given the width and the height. The function definition of f is

# def find_rectangle_area(w, h)
# , where w and h is the width and height of the rectangle respectively just like in the Rectangle Area Finder II task.

# The output reformatting should have the following format

# Rectangle Area = <<rectangle_area>>
# The <<rectangle_area>> should be substituted by the result of the find_rectangle_area function without decimal points. 
# The number must be round up when having .5 or greater; and round down otherwise.

# Example

# Consider the following function call:

# >>> print(find_rectangle_area(3,4))
# This statement should return

# Rectangle Area = 12

def output_decorator(f):
    def wrap(w,h):
        func = f(w,h)
        ans = round(func)
        return f"Rectangle Area = {ans}"
    return wrap
@output_decorator
def find_rectangle_area(w,h):
    return w*h