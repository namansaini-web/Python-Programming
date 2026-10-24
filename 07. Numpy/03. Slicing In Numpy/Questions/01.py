import numpy as np

# Product 3-5 receives a 10% discount 
prices = np.array([
    1000,2000,1500,2500,3000,3500
])

print(prices[2:] * 0.9)