data = {
    "A": 5,
    "B": 10,
    "C": 15
}
total = 0
for key in data:
    total += data[key]

print(total / len(data))   # Gives a float value 
print(total // len(data))   # Gives a int value 