import numpy as np

# Changing datatype of an array : --> Lose of information
a1 = np.array([10,15,20,25], dtype = str)
print(a1)
b1 = np.array([10.5,4,7.7], dtype = int)
print(b1)
c1 = np.array([0,2,4,7,0], dtype = bool)
print(c1)

arr = np.array([10.5, 20.7, 30.9], dtype = int)
print(arr, "Datatype : ", arr.dtype)

# create an array of even numbers in linspace and arange :
a = np.arange(0,11,2) # Gives int array
print(a, "datatype : ", a.dtype)
b = np.linspace(0,10,6) # Gives float array
print(b, "datatype : ",  b.dtype)

# Bool dtype :
arr1 = np.array([0,1,2,0,5], dtype = bool)
print(arr1, arr1.dtype)
arr2 = arr1*1
print(arr2, arr2.dtype)  
