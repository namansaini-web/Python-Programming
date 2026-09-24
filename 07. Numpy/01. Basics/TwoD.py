import numpy as np

# Creating a 2D Array in Numpy:
a = [[2,4,6],
     [1,3,5],
     [7,8,9]]
print(type(a))
b = np.array(a)
print(b)
print(type(b))

# Excessing elements in 2D array :
marks = np.array([
    [70,80,90],
    [60,75,85]
])
print(marks[0,1])
print(marks[0][1])




