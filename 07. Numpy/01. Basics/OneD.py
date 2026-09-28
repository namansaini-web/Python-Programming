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

# Numpy with different datatype : --> every element is changed to a String.
h = [3,5,6,"naman",True]
h = np.array(h)
print(h)


# Creating a numpy from tupple :
num = (4,6,3,1)
a = np.array(num)
print(a)
print(type(a), type(num))

# Numpy for strings :
names = np.array(["Naman", "Saini"])
print(type(names), names)

# Changing dtype of an array : --> Lose of information
a1 = np.array([10,15,20,25], dtype = str)
print(a1)
b1 = np.array([10.5,4,7.7], dtype = int)
print(b1)
c1 = np.array([0,2,4,7,0], dtype = bool)
print(c1)

 