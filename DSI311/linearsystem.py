import numpy as np
n= int(input())
arr,b = [[0]* n ] * n,[[0]* n] * n
for i in range(n):
    lst = list(map(int, input().split()))
    arr[i] = lst[:n]
    b[i] = lst[n:]
print(arr,"b is \n",b)
result = np.linalg.solve(arr,b)
for i in range(n):
    print("{0:.2f}".format(result[i][0]))  