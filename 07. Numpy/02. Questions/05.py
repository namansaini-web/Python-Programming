#A student's marks are stored in a tuple:
#(78, 85, 92, 67, 88)
#Convert the tuple into a NumPy array and add 3 marks to every value.

import numpy as np

marks = np.array((78, 85, 92, 67, 88))
new_marks = marks + 3 
print(new_marks)