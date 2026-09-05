# Find the largest string in a list:

names = ["Naman", "Kunal", "Kavita", "Naresh"]
largest = ""
for name in names:
    if len(name) > len(largest):
        largest = name

print(largest)