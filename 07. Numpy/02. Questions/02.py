# A student has scored:
# 65, 72, 80, 88, 91
# Create a NumPy array containing these marks.
# Add 5 bonus marks to every subject and display the original marks and updated marks.

import numpy as np

marks = np.array([65, 72, 80, 88, 91])
bonus = 5
new_marks = marks + bonus
print(marks, new_marks)