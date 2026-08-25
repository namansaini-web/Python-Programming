# 1:
password = input("Enter your password : ")

flag_1 = False
flag_2 = False
flag_3 = False
flag_4 = False
for i in password :
    if (len(password) >= 8):
        flag_4 = True
    if (ord(i) >= 65 and ord(i) <= 90):
        flag_1 = True
    if (ord(i) >= 97 and ord(i) <= 122):
        flag_2 = True
    if (ord(i) >= 48 and ord(i) <= 57):
        flag_3 = True

if((flag_1 and flag_2) and (flag_3 and flag_4)):
    print("Strong Password")
else:
    print("Weak Password")



# 2:
password = "Adityazzz007"
upper = False
lower = False
digit = False
n = len(password)
for c in password:
    if c.islower():
        lower = True
    elif c.isupper():
        upper = True
    elif c.isdigit():
        digit = True

if n >= 8 and upper and lower and digit:
    print("Strong Password")
else:
    print("Weak Password")
    
