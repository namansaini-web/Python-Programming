# A company has recorded its monthly revenue for the first 6 months:

import numpy as np
revenue = np.array([120000, 135000, 142000, 150000, 165000, 172000])

# Write a NumPy program to:
# Display the revenue of the third month.
# Display the revenue of the last month using negative indexing.
# Select the revenue from Month 2 to Month 5 using slicing.
# Increase the revenue of the last 3 months by 10%.
# Display the final revenue array

print(revenue[2])

print(revenue[-1])

print(revenue[1:5])

revenue[3:] = revenue[3:]*1.10
print(revenue[3:])

print(revenue)