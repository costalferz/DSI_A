# Write Python code that find the area of a circle given the radius Output only the first 3 decimal places. (Use pi = 22/7) E.g.,

# Input	Output
#  3	28.286

radius = (float(input()))
pi = 22/7
Area = radius*radius*pi
print("{:,.3f}".format(Area))