import numpy as np

sales = np.array([100, 20, 300, 400, 500])

# Calculating mean of an array without using numpy :
n = len(sales)
sum = 0
for i in sales:
    sum += i

print(sum/n)

# Calculating with using numpy:
print(np.mean(sales))
   # OR
print(np.sum(sales) / len(sales))

