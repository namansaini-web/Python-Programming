# A classroom has 6 rows and 5 seats per row.
# Initially, all seats are empty.

# 0 = Empty
# 1 = Occupied 

# Task: 
# Create a 6x5 array filled with zeroes.
# Mark the first seat of the first row as occuiped.
# Mark all seats in the 3rd row as occupied.
# Mark all seats in the last row as occupied.
# Display the first 3 rows.
# Display the first rows.
# DIsplay the last 2 columns.
# Display the complete seating matrix.

import numpy as np
seats = np.full((6,5), 0)

seats[0,0] = 1

seats[2 , :] = 1

seats[-1 , :] = 1

print(seats[:3 , :])

print(seats[: , -2:])

print(seats)