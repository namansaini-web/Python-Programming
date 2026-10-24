# A store has the following product prices:
import numpy as np
prices = np.array([500, 750, 1200, 1500, 2000, 2500])

# Write a program to:
# Display the first three prices.
# Display the last two prices.
# Apply a 15% discount only to products at indexes 2 through 4.
# Add ₹50 to the price of the first product.
# Display the updated prices

print(prices[:3])

print(prices[-2:])

prices[2:5] == prices[2:5]*0.85
print(prices[2:5])

prices[0] == prices[0]+50

print(prices)