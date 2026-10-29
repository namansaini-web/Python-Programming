# An e-commerce company stores order information:

import numpy as np
orders = np.array([
[1000, 2, 500],
[1001, 3, 750],
[1002, 1, 1200],
[1003, 4, 300],
[1004, 2, 900]
])
# Columns:
# Column 1 → Order ID
# Column 2 → Quantity
# Column 3 → Price per item

# Tasks:
# Display the complete information of Order 1002.
# Display all quantities.
# Display all prices.
# Display the first 3 orders.
# Display the last 2 orders.
# Increase the price of the last 2 products by 10%.
# Increase the quantity of the first order by 1.
# Display the final dataset.
# Create a separate array containing only the quantity and price columns.
# Display the shape and size of the dataset.


print(orders[2])

print(orders[: , 1])

print(orders[: , 2])

print(orders[:3 , :])

print(orders[-2: , :])

orders[-2: , -1] = orders[-2: , -1]*1.10
print(orders[-2: , 2])

orders[0 , 1] += 1
print(orders[0 , 1])

print(orders)

Data = orders[: , 1:]
print(Data)

print("Shape: ", orders.shape, " , Size: ", orders.size)

    