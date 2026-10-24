# A college records marks of 5 students in 4 subjects.

import numpy as np
marks = np.array([
        [72, 85, 90, 78],
        [65, 70, 75, 80],
        [88, 92, 95, 90],
        [55, 65, 60, 70],
        [78, 82, 85, 88]
])
# Each row represents a student and each column represents a subject.

# Tasks:
# Determine the number of dimensions.
# Determine the number of students and subjects using shape.
# Determine the total number of marks using size.
# Display the complete marks of the 3rd student.
# Display marks of all students in the 2nd subject.
# Extract marks of the first 3 students in the first 2 subjects.
# Increase the marks of the last 2 students in the 4th subject by 5

print(marks.ndim)

print("No. of students : ", marks.shape[0])
print("No. of subjects : ", marks.shape[1])

print(marks.size)

print(marks[2 , :])

print(marks[: , 1])

print(marks[:3 , :2])

marks[-2: , -1] = marks[-2: , -1] + 5
print(marks)