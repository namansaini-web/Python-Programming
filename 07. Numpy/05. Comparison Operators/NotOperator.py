import numpy as np

# Not operator => '~'
prices = np.array([499,799,1299,3999,599])
print(prices[~(prices > 900)])