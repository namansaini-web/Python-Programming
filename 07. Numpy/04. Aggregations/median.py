import numpy as np
sales = np.array([50,30,10,190,100])
arr =  np.array([50,30,10,190,100])

# Finding median without using numpy :
arr = np.sort(arr)
n = len(arr)
if n % 2 == 0:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
else:
    median = arr[n//2]
print(median)

# Finding median using numpy :
print(np.median(sales))  