# A company has salary data for 4 employees:

import numpy as np
salary = np.array([
        [30000, 5000],
        [40000, 6000],
        [50000, 8000],
        [60000, 10000]
])
# Column 1 = Basic Salary
# Column 2 = Allowance

# Tasks:
# Display the complete information of the 2nd employee.
# Display all basic salaries.
# Display all allowances.
# Increase all allowances by ₹1,000.
# Increase the basic salary of the last two employees by 10%.
# Display the final salary matrix.

print(salary[1 , :])

print(salary[: , 0])

print(salary[: , 1])

salary[: , 1] += 1000

salary[-2: , 0] = salary[-2: , 0]*1.10

print(salary)