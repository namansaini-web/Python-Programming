# Problem Statement
# The following array contains marks of 5 students in 4 subjects:
import numpy as np
marks = np.array([
[72, 85, 90, 78],
[65, 70, 75, 80],
[88, 92, 95, 90],
[55, 60, 58, 65],
[78, 82, 85, 88]
])
# Assume each row represents a student and each column represents a subject.
# Find:
# Shape and size of the array.
print(np.shape(marks), np.size(marks))

# Marks obtained by the third student.
print(marks[2,:])

# Marks obtained in the second subject by all students.
print(marks[:,1])

# Average marks of every student.
print(np.mean(marks, axis=1)) # Row wise

# Average marks of every subject.
print(np.mean(marks, axis=0)) # Column wise

# Students whose average is above 75.
print(marks[np.mean(marks, axis=1) > 75])

# Highest mark obtained in each subject.
print(np.max(marks, axis=0))

# The complete row of the student with the highest average
print(marks[np.argmax(np.mean(marks, axis=1))])
