num = {2,3,6,1,8,1}

for n in num:
    print(n, end= " ")
print()

total = 0
for ele in num:
    total += ele  # Add all the unique elements.
print(total)


colors = {"Red", "Green", "Blue"}
count = 0
for col in colors:
    if "e" in col:
        count += 1
print(count)
