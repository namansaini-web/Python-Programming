# An organization stores employee information as:
# Salary | Experience
import numpy as np
employees = np.array([
        [30000, 2],
        [40000, 4],
        [50000, 6],
        [60000, 8]
    ])
# Perform the following:
# Display the information of the last employee using negative indexing.
# Display the salary of the second employee.
# Increase the salary of the third employee by 15%.
# Add 1 year of experience to the first employee.
# Display the final employee array.


print(employees[-1])

print("Salary of Second Employee: ", employees[1,0])

employees[2,0] = employees[2,0]*1.15
print(employees[2,0])

employees[0, 1] += 1
print(employees[0,1])

print(employees)