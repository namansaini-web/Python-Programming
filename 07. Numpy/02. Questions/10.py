#A college stores marks of 4 students in 3 subjects: Maths, Science, and English.
import numpy as np
marks = np.array([
        [72, 85, 90],
        [65, 78, 82],
        [88, 91, 84],
        [70, 76, 80]
    ])
#Perform the following:
#Display the marks of the third student.
#Display the Science marks of the second student.
#Add 5 bonus marks to every student's English marks.
#Change the Maths marks of the fourth student to 75.
#Display the final marks array.

print(marks[2])
print(marks[1,1])

marks[:,2] = marks[:,2] + 5
print(marks)

marks[3,1] = 75
print(marks[3,1])

print(marks)