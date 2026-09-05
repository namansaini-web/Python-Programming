string = input("Enter your line : ")
l_string = string.lower()

count_v = 0
count_d = 0
count_s = 0
count_c = 0

for ch in l_string:
    if(ch in "aeiouAEIOU"):
        count_v += 1
    elif(ch in "0123456789"):
        count_d += 1
    elif((ch >= "a") and (ch <= "z")):
        count_c += 1
    elif(ch == " "):
        count_s += 1

print("Number of vowels: ", count_v)
print("Number of consonants: ", count_c)
print("Number of spaces: ", count_s)
print("Number of digits: ", count_d)

# We can also use 'ch.isalpha()' for consonants.
# And, 'ch.isdigit()' for digits.