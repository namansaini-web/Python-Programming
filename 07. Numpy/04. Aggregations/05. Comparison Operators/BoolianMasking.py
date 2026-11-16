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
print(prices[(prices<=600) | (prices>=1000)])
