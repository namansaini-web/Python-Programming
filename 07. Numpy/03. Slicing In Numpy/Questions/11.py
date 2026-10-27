# A startup expects its monthly users to grow from 
#   10,000 to 100,000.

# Tasks:
# Generate monthly user targets using np.linspace().
# Create month numbers using np.arange().
# Display users expected in Month 1 and Month 12.
# Display users expected from Months 4–8.
# Increase all targets by another 15%.
# Display the updated targets for the last 4 months.

import numpy as np

users = np.linspace(10000, 100000, 12, dtype = int)
print(users)

months = np.arange(1,13)
print(months)

print(users[0] , users[-1])

print(users[3:8])

target = users*1.15
print(target)

print(target[-4:])