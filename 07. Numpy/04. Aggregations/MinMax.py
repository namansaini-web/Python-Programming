import numpy as np

sales = np.array([100, 20, 300, 400, 500])

# Finding minimum sale without numpy :
mn = sales[0]
for s in sales:
    if s < mn:
        mn = s
print("Minimum sales :", mn)

# Finding maximum sale without numpy :
mx = sales[0]
for s in sales:
    if s > mx:
        mx = s
print("Minimum sales :", mx)

# Finding minimum with numpy:
print(np.min(sales))

# Finding maximum with numpy:
print(np.max(sales))