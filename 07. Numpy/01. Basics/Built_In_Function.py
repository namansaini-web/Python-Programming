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

# create an array of even numbers using linspace, and arange :
a = np.arange(0,11,2) # Gives int array
print(a, "datatype : ", a.dtype)
b = np.linspace(0,10,6) # Gives float array
print(b, "datatype : ",  b.dtype)

