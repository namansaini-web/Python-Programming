numbers = [2, 4, 6, 8, 16]
total = 0

i = 0
n = len(numbers)
while i < n:
    total += numbers[i]
    i += 2
print(total)