# A restaurant stores prices of 6 menu items:

import numpy as np
prices = np.array([120, 180, 250, 300, 450, 600])

# The restaurant wants to run different pricing experiments.

# Tasks:
#   Add ₹20 to the first two items.
#   Give a 10% discount to items 3, 4 and 5.
#   Keep the last item unchanged.
#   Display the first 3 prices after modification.
#   Display the last 2 prices.
#   Create a separate array containing only the middle four prices.

prices[:2] += 20
print(prices[:2])

prices[2:5] = prices[2:5] * 0.90
print(prices[2:5])

print(prices[:3])

print(prices[-2:])

array = prices[1:5]
print(array)