import numpy as np 


# 1-Dimensional arrays:
marks = np.array([70, 30, 57, 67, 33, 55, 90])

# Print elements from 70 to 67
print(marks[0:4])

# Print elements from 67 to 55
print(marks[3:6])

# Print all the elements at even places
print(marks[0:7:2]) 

# Printing elements without starting attribute and ending attribute
print(marks[:3])
print(marks[1:])
print(marks[::])  # Shortcut to print full array

# Printing elements with negative indexing 
print(marks[-4:])


# 2-Dimensional arrays
mark = np.array([
    [20,34,54,67,89],
    [45,67,78,98,99],
    [45,34,54,68,79],
    [32,25,62,87,12]
])

print(mark[:2])
print(mark[2:4])
print(mark[1:3])

# Printing specific columns and rows element
print(mark[1:3 , 1:3])
print(mark[: , :2])
print(mark[: , -1:])

# Using operations
print(mark[: , 1:3] * 1.10)