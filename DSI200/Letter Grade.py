# Write Python code that converts from a numerical grade (1-100) to a letter grade (A, B+, B, C+, C, D+, D, F) using the following criteria,

# Numerical Grade	Letter Grade
#       A	            90-100
#       B+	            85-89
#       B	            80-84
#       C+	            75-79
#       C	            70-74
#       D+	            65-69
#       D	            60-64
#       F	            0-59

# Input	Output
#  84	  B
user_input = int(input())
if 90<=user_input:
    print("A")
elif user_input>=85 and user_input<=89:
    print("B+")
elif user_input>=80 and user_input<=84:
    print("B")
elif user_input>=75 and user_input<=79:
    print("C+")
elif user_input>=70 and user_input<=74:
    print("C")
elif user_input>=65 and user_input<=69:
    print("D+")
elif user_input>=60 and user_input<=64:
    print("D")
else:
    print("F")