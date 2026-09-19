# Importing Numpy :
import numpy as np 
Marks1 = np.array([55,90,78,70,90])
bonus = 10

Marks2 = Marks1 + bonus
print(Marks2)  
Marks3 = np.append(Marks1, bonus)
print(Marks3)


# Diff Between Lists and Numpy :
a = [1,2,3,4,5]
print(type(a), a)
a = np.array(a)
print(type(a), a)


# Write a code to make every number twice :

# Using Python :
a = [3,6,1,9]
l = []
for i in a :
    l.append(i*2)
print(l)

# Using Numpy :
b = [3,6,1,9]
b = np.array(b)
b = b*2
print(b)


# Creating a 2D Array in Numpy:
x = [1,3,5,7,9]
y = [2,4,6,8,10]
arr = np.array(x+y)
print(arr)