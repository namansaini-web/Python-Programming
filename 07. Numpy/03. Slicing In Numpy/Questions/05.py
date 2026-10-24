# A factory operates for 30 days and wants to create a production schedule
# starting from 500 units per day and gradually increasing to 1,500 units per day.

# Tasks :
# Create day numbers from 1 to 30 using np.arange().
# Display the first 5 production targets.
# Display the last 5 production targets.
# Increase every production target by 10%.
# Display the first 5 updated targets

import numpy as np
production = np.linspace(500, 1500, 30, dtype = int)
print(production)

days = np.arange(1,31)
print(days)

print(production[:5])

print(production[-5:])

production = production * 1.10
print(production)
