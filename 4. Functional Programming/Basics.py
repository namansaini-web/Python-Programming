# Create a list to store the squares of each of the numbers in the list.

# 1. Normally:
n = [1,2,3,4,5]
sq = []
for i in n:
    sq.append(i**2)
print(sq)

# 2. Using Functional Programming:
sq = list(map(lambda x: x**2, n))
print(sq)