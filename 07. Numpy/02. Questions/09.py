import numpy as np
  # 1.
# A college wants to initialize a marks table for 5 students and 4 subjects.Initially,
#  every student's marks are set to zero. Create this using NumPy.
#  Then create another 5 × 4 array containing a default value of 50.

marks = np.zeros((5,4))
print(marks)

print(marks + 50)
# or 
updated = np.full((5,4), 50)
print(updated)

  # 2.
# Five students have scores:
# [45, 56, 67, 78, 89]
# The teacher gives everyone 3 grace marks.
# After that, the college applies a 10% scaling factor to the adjusted scores.
# Calculate the final scores.

scores = np.array([45, 56, 67, 78, 89])
print("Original Socres : ", scores)

Updated_scores = scores + 3
print("Updated Scores : ", Updated_scores)

adjustment = Updated_scores*0.10
print("Adjustment : ", adjustment)

final_scores = Updated_scores + adjustment
print(final_scores)

  # 3. 
# A company wants to set targets from ₹20,000 to ₹1,00,000.
# Generate exactly 9 target values, equally spaced.
# Then create actual sales:
# [18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000]
# Calculate the difference between actual and target.

target = np.linspace(20000, 100000, 9)
print(target)

actual_sales = np.array([18000, 28000, 39000, 47000, 57000, 66000, 76000, 90000, 105000])
print(actual_sales)

Difference = target-actual_sales
print("Difference : ", Difference)

  # 4.
# A dataset contains:
# [10, 20, 30.5, 40, 50.75]
# Create a NumPy array and display its data type.
# Then create an integer version of the array.
# Finally, multiply the integer array by 3.

arr = np.array([10, 20, 30.5, 40, 50.75])
arr_int = arr.astype(int)
print("Original Array : ", arr)
print("final Array : ", arr_int*3)

  # 5. 
# A company has product prices:
# [499, 799, 1299, 1999, 2499]
# The company wants to:
# Increase all prices by 12%.
# Add ₹50 packaging charges.
# Calculate the final customer price.

prices = np.array([499, 799, 1299, 1999, 2499])
New_prices = prices*1.12
final_prices = New_prices + 50

print("Original Prices : ", prices)
print("New Prices : ", New_prices)
print("Final charges : ", final_prices)