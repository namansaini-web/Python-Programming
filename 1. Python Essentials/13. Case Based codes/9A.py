string = input("Enter your string : ")
freq = {}

for i in string:
    if i == " ":
        continue
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(freq)

mx_v = 0
for k,v in freq.items():
    if v > mx_v:
        mx_v = v
        mx_k = k
print(mx_k)
