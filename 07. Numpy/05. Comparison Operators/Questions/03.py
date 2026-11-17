# An online store has the following product prices:
import numpy as np
prices = np.array([
    499.50, 799.90, 1299.75,
    2499.50, 3999.90, 599.25,
    899.80, 1599.40
])

# Perform:
# Round prices to the nearest whole number.
print(np.round(prices))

# Find products costing more than ₹1,000.
print(prices[prices > 1000])

# Calculate a 15% discount only on products costing more than ₹1,000.
print(prices[prices > 1000]*0.15)

# Calculate the average discounted price of those products.
discount = np.round(prices[prices > 1000]*0.85)
print(np.mean(discount))

# Find the most expensive original product.
print(np.max(prices))

# Extract the last 4 products.
print(prices[-4:])

# Calculate the square root of the prices and round them to 2 decimal places.
print(np.round(np.sqrt(prices)))

