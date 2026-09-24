# A company records sales for four quarters:
# Q1 = 125000
# Q2 = 148000
# Q3 = 135000
# Q4 = 172000
# Create a NumPy array.
# The company expects next year's sales to be 15% higher than this year's sales.
#Calculate the expected sales for each quarter.
# Then calculate the additional sales expected in each quarter

import numpy as np

sales = np.array([125000, 148000, 135000, 172000])
exp_sales = sales*1.15
add_sales = exp_sales - sales 
print("original Sales : ", sales)
print("Expected Sales : ", exp_sales)
print("Additional Sales : ", add_sales)
