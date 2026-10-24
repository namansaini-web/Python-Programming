# A machine records temperature every hour:

import numpy as np
temp = np.array([
        28, 29, 30, 31, 33, 35,
        36, 35, 34, 32, 30, 29
])

# Tasks:
#   Extract readings from the first 6 hours.
#   Extract readings from the last 6 hours.
#   Extract readings from every alternate hour.
#   Extract readings from every third hour.
#   Reverse the complete temperature sequence.
#   Extract the last 4 readings in reverse order.

print(temp[:6])

print(temp[-6:])

print(temp[::2])

print(temp[::3])

RevTemp = temp[::-1]
print(RevTemp) 

print(temp[-1:-5:-1])