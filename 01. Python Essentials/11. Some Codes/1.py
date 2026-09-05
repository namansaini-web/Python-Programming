# Write a code convert a string to lower case without lower():

# logic :
print(ord('a') - ord('A'))

Str = ""
string = input("Enter your string : ")
Str = (string)

new_s = ""
for ch in Str:
    if ch <= 'Z' and ch >= 'A' :
        new_s += chr(ord(ch)+32)
    else :
        new_s += ch

print(new_s)



