# An electricity company wants to estimate the monthly electricity consumption
# of a household for 6 months.

# The expected consumption is the following units:
[180, 220, 195, 250, 280, 240] 

# The company expects consumption to increase by 8% during the next billing cycle.

# Tasks
# Create a NumPy array for the consumption.
# Find the consumption in the 4th month.
# Extract the consumption of the last 3 months.
# Create a new array containing the expected consumption after an 8% increase.

import numpy as np
consumption = np.array(
    [180, 220, 195, 250, 280, 240] 
)

print(consumption[5])

print(consumption[3:])

predicted = np.array([], dtype = float)
predicted = consumption * 1.08

print(consumption)
print(predicted)