# A teacher has recorded marks of 10 students:

import numpy as np
marks = np.array([72, 85, 91, 64, 78, 88, 95, 70, 82, 76])

# Find:
# Total marks
# Average marks
# Highest marks
# Lowest marks
# Difference between highest and lowest marks
# Index of the student with the highest marks

print("Total marks : ", np.sum(marks))

print("Avg marks : ", np.mean(marks))

print("Highest marks : ", np.max(marks))

print("Lowest marks : ", np.min(marks))

print(np.max(marks) - np.min(marks))

# Finding index without numpy :
mx = marks[0]
mxi = 0
n = len(marks)
for i in range(n):
    if mx < marks[i]:
        mx = marks[i]
        mxi = i
print("Index of highest element : ", mxi)

# Finding index with numpy:
print("Index of highest element : ", np.argmax(marks))