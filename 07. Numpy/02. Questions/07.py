# Two branches of a company have inventory for five products.
# Branch A = [120, 150, 180, 100, 200]
# Branch B = [80, 130, 170, 120, 150]
# Create two NumPy arrays.

# Calculate:
# Total inventory for each product.
# Difference between Branch A and Branch B.
# Combined inventory after receiving an additional 20 units of every product

import numpy as np 
a = np.array([120, 150, 180, 100, 200])
b = np.array([80, 130, 170, 120, 150])

print("Total Inventory : ", a+b)
print("Difference : ", a-b)
print("New Total Inventory : ", a+b+20)