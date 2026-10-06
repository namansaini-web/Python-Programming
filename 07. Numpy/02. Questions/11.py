#A company records monthly sales for 3 branches.
#he columns represent January, February, and March.
import numpy as np
sales = np.array([
        [120, 150, 180],
        [100, 130, 160],
        [200, 220, 250]
   ])
#Perform the following:
#Display the complete sales data of Branch 2.
#Display the sales of all branches in February.
#Increase the March sales of every branch by 10%.
#The January sales of Branch 1 were entered incorrectly. Change them from 120 to 135.
#Display the updated sales array.

print(sales[1])

print(sales[:,1])

sales[:,2] = sales[:,2]*1.10
print(sales[:,2])

sales[0,0] = 135
print(sales[0,1])

print(sales)