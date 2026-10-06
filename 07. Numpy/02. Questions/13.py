# A company has inventory information for 4 products across 3 warehouses.
# Columns: Warehouse A, Warehouse B, Warehouse C

import numpy as np
inventory = np.array([
        [100, 120, 150],
        [80, 90, 110],
        [200, 180, 160],
        [50, 70, 90]
    ])
# Perform the following:
# Display the inventory of Product 3 across all warehouses.
# Display the inventory of Warehouse B for all products.
# Warehouse A receives 20 additional units of every product. Update the array.
# The inventory of Product 4 in Warehouse C is incorrect. Change it to 100.
# Display the final inventory.

print(inventory[2])

print(inventory[:,1])

inventory[:,0] += 20
print(inventory[:,0])

inventory[3,2] = 100
print(inventory[3,2])

print(inventory)