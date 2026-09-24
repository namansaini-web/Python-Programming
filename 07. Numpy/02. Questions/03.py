# A shop has five products with prices:
# 100, 250, 400, 550, 800
# Create a NumPy array
# calculate the price after applying a 10% discount to every product.

import numpy as np 

prices = np.array([100, 250, 400, 550, 800])
discount = prices*0.10
new_prices = prices - discount
print(new_prices)