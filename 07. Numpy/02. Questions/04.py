# A company has five employees with salaries:
# 30000, 35000, 40000, 45000, 50000
# Create an array and give every employee a 10% salary increment.

import numpy as np

salaries = np.array([30000, 35000, 40000, 45000, 50000])
increment = salaries*0.10
new_salaries = salaries + increment
print(new_salaries)