import numpy as np 

# Default methode to create 1D numpy of floating zeros and ones:
x = np.zeros(5)
print(x)
y = np.ones(5)
print(y)

# Default methode to create 2D numpy of floating zeros and ones:
x1 = np.zeros((3,4))
print(x1)
y1 = np.ones((3,4))
print(y1)

# Arrange methode :
arr = np.arange(5)
print(arr)
Arr = np.arange(1,11)
print(Arr)
    
brr = np.arange(2,11,2) 
print(brr)  

# Linsapce Methode : --> creates equally spaced value between two numbers.
Brr = np.linspace(0,10,5)
print(Brr)


# Other methode for creating an array :

# Gives Flaot values
print(np.ones(5)*5)

# For int values :
# In 1D array :
print(np.full(5,5))
# In 2D array :
print(np.full((3,5), 5))

# Shape Concept : --> gives the dimensions of the array.
crr = np.array([
    [[3,5],[4,6]],
    [[4,5],[9,8]]
])
print(crr.shape)
print(arr.shape)

# Size Concept : --> Gives total number of elements.
print(crr.size)

# astype Concept :
Crr = np.array([10.5, 20.7, 30.9])
Crr_int = arr.astype(int)
print(Crr)
print(Crr_int)

# Conclusion :
data = np.array([
    [1,2,3,4],
    [2,3,4,5],
    [4,5,6,7]
])
print("len : ", len(data))
print("size : ", data.size)
print("shape : ", data.shape)
print("ndim : ", data.ndim)

student_marks = np.array([
[78, 85, 90, 88, 76],
[92, 81, 85, 89, 95],
[67, 72, 70, 75, 68],
[88, 91, 94, 90, 87],
[76, 80, 79, 82, 85]
])
    # The array
    # Number of dimensions
    # Shape
    # Total number of values
    # Data type
    # Number of students
    # Number of subjects
print(student_marks)
print(student_marks.ndim)
print(student_marks.shape)
print(student_marks.size)
print(student_marks.dtype)
print(student_marks.shape[0])
print(student_marks.shape[1])



