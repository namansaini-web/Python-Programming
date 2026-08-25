# Write a code to only store the unique occurences of the elements in the list:

Lis = [2,3,4,4,5,6,5,2,4]
lis = []

for i in Lis:
    if i not in lis:
        lis.append(i)
print(lis)