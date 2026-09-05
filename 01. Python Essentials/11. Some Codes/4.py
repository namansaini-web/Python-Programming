# Finding Frequency of each and every character in a string:

text = "Mississppi"
count = {}
for ch in text:
    if ch not in count:
        count[ch] = 1
    else:
        count[ch] += 1
print(count)
print(count["s"])
