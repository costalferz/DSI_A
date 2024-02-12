# Write Python code that find the maximum discount that can be achieved by using the given coupons. 
# Each coupon can be used at most once and each one has two numbers, the minimum purchase amount and the discount. You can use the coupon 
# if and only if the total minimum purchase amount of the selected coupons is not greater than the total price.

# Input/Output: The first line of the input consists of one integer, m, which is the total price. The second line contains one integer, 
# n, which is the number of coupons. The following n lines contain two integers, which are the minimum purchase amount and the discount of each coupon.
#  The output must display one integer which is the maximum discount from these coupons.

# E.g.,

# Input	    Output
# 1700	     166
# 3	
# 500 55	
# 1000 111	
# 1500 155	
# The result is achieved by selecting the 1st coupon whose discount is 55 and the 2nd coupon whose discount is 111 so the total discount is 166. 
# The minimum purchase amount of these coupons are 500 and 1000 respectively so the total is 1500, which is less than the total price at 1700, so these coupons are valid.

# NB: You can use NumPy Library

import numpy as np
cost = int(input())
n = int(input())
price = 0
if (0<=cost<=100000) and (1<=n<=50):
    coupons = np.empty((n,2),dtype=int)
    for i in range(len(coupons)): 
        coupons[i][0],coupons[i][1]= map(int, input().split())
    for k in range(0,50):
        if(coupons[0][0]>=cost):
            break
        cost = cost-coupons[k][0]
        price = price+coupons[k][1]
print(price)