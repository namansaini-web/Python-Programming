# A warehouse has 4 storage sections and 5 products.
# Initially, every product has a stock level of 100 units.

# Tasks:
#   Create a 4 × 5 array where every value is 100.
#   Increase the stock of the first two sections by 20 units.
#   Reduce stock of the last two products by 10%.
#   Display only the middle two sections.
#   Display only the first three products.
#   Display the bottom-right 2 × 2 portion of the matrix.

import numpy as np
inventory = np.full((4,5),100)
print(inventory)

inventory[:2 , :] += 20
print(inventory[:2])

inventory[: , -2:] = inventory[: , -2:]*0.90
print(inventory[:  , -2:])

print(inventory[1:3 , :])

print(inventory[:3 , :])

print(inventory)
print(inventory[-2: , -2:])