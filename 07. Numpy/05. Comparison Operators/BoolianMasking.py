import numpy as np

marks = np.array([70,80,65,90,75])
# If elem is greater then 75 returns True otherwise return False.
print(marks>75)
# Return the actual elements
print(marks[marks>75 ])

temperature = np.array([24,28,31,35,29,22,37,30,32])
# Temperature atleast 32
print(temperature[temperature>=32])

prices = np.array([499,799,1299,3999,599])
# Prices less then 1000 or greater than 600 :
# print(prices[(prices>=600) and (prices<=1000)]) , ValueError 
print(prices[(prices>=600) & (prices<=1000)]) 
# Prices less then 600 or greater than 1000 :
# print(prices[(prices<=600) or (prices>=1000)]) , ValueError 
print(prices[(prices<=600) | (prices>=1000)])
# Show prices not greater then 900 :
print(prices[prices<=900])

marks = np.array([
    [72,84,90],
    [55,60,65],
    [88,93,95],
    [15,25,35]
])
print(marks>70)
print(marks[marks>70]) # Gives 1D array

sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [150, 250, 350]
])
# Find values greater then 200 only in first row :
print(sales[0][sales[0] > 200])


product = np.array([
    [101, 500],
    [102, 1200],
    [103, 800],
    [104, 1500]
])
# We want products whose price is greater than 1000
price = product[:, 1]
print(price[price > 1000])
