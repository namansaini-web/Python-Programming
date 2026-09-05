text = "mississippi"
letters = set(text)
count = 0

for ch in letters:
    if ch in "aeiou":
        count += 1
print(count)
print(letters)