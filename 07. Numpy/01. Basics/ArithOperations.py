import numpy as np
  
# In Python:
x = [3,5,7]
y = [2,4,6]
z = []
n = len(x) 
for i in range(n):
    z.append(x[i]+y[i])
print(z)

# In Numpy:
a = np.array([3,5,7])
b = np.array([2,4,6])
c = np.array(a+b)
print(c)

print(a*b)
print(a-b)
print(a**2)


# Given a list of prices, update them with GST included prices :
prices = [20,40,100,50]

# In Python : 
GST_prices = [] 
for i in prices:
    GST_prices.append(i + 0.18*i)
print(GST_prices)

# In numpy :
new_prices = np.array(prices)
GST_np = new_prices*1.18
print(GST_np)

# Opertions for 2D array :
marks  = np.array([
    [70,80,90],
    [60,75,85]
])
print(marks + 5)
print(marks * 2)
print(marks - 10)

