# A weather application stores temperatures for 3 cities.
# Columns: Morning, Afternoon, Evening
import numpy as np
temperature = np.array([
            [24, 35, 28],
            [22, 32, 26],
            [27, 38, 30]
        ])
# Perform the following:
# Display the complete temperature data of the first city.
# Display all afternoon temperatures.
# Display the evening temperature of the last city using negative indexing.
# Increase all morning temperatures by 2°C.
# The afternoon temperature of the second city was recorded incorrectly. Change it from 32 to 34.
# Display the final temperature array.

print(temperature[0])

print(temperature[:,1])

print(temperature[-1,-1])

temperature[:,0] += 2
print(temperature[:,0])

temperature[1,1] = 34
print(temperature[1,1])

print(temperature)