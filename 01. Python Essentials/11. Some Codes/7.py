text = "Python Programming"
count = 0

for ch in text:
    if ch == " ":
        continue
    if ch.lower() in "aeiou":
        count += 1
print(count)

