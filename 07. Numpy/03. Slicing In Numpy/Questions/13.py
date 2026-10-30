# A company stores quarterly revenue and expenses:

import numpy as np
financials = np.array([
        [120, 80],
        [150, 90],
        [180, 110],
        [200, 130]
])

# Rows = Q1, Q2, Q3, Q4
# Columns = Revenue, Expense
# Tasks:
# Display Q2's complete financial data.
# Display all quarterly revenues.
# Display all quarterly expenses.
# Extract Q2 and Q3 data.
# Increase Q4 revenue by 15%.
# Reduce Q1 expense by 10%.
# Display the final financial matrix.

print(financials[1])

print(financials[: , 0])

print(financials[: , 1])

print(financials[1:3 , :])

financials[-1 , 0] = financials[-1 , 0]*1.15

financials[0 , 1] = financials[0 , 1]*0.90

print(financials)