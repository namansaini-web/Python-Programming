# An electricity board records the monthly electricity consumption of a household for one year:
import numpy as np
consumption = np.array([
        180, 220, 195, 250,
        280, 310, 295, 270,
        240, 210, 190, 230
])
# Perform the following:

# Find the total annual consumption.
sum = 0
for i in consumption:
    sum += i
print("Total Annual consumption: ", sum)
    # OR
print(np.sum(consumption))

# Calculate average monthly consumption.
print(np.mean(consumption))

# Find the highest and lowest consumption.
print(np.max(consumption))
print(np.min(consumption))

# Find the month index with the highest consumption.
print(np.argmax(consumption))

# Extract the first 6 months using slicing.
print(consumption[:6])

# Extract alternate months.
print(consumption[::2])

# Find all months where consumption was greater than the annual average.
print(consumption[consumption > np.mean(consumption)])

# Calculate the new monthly projections if next year's consumption is expected to be 8% higher.
next = consumption*1.08
print(next)