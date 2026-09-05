sentence = input("Enter your sentence : ")
words = sentence.split(" ")
print(words)

freq = {}
count = 0
for word in words:
    if word not in freq:
        freq[word] = 1
    else :
        freq[word] += 1
        
print(freq)