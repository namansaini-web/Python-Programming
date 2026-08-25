words = ["apple", "banana", "apple", "mango", "banana"]
unique = set(words)
result = ""

for word in unique:
    result += word[0]
print(len(result))
print(result)