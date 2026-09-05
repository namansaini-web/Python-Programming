# Text File ==> 

# Methode 1: Closing a file is important.

# Writing in a file:
file = open("sample.txt", "w")
file.write("Naman\n")
file.write("Ishan\n")
file.write("Suraj\n")
file.close()

# Reading in a file:
file = open("sample.txt", "r")
data  = file.read()
print(data)
file.close()

# Appending in a file:
file = open("sample.txt", "a")
file.write("Abhinav")
file.close()

file = open("sample.txt", "r")
for line in file:
    print(line)
file.close()

# Creating a new file:
f = open("xyz.txt", "x")
f.close()


# Methode 2: No need for closing a file.

with open("sample.txt", "r") as file:
    print(file.read())

with open("xyz.txt", "w") as file:
    file.write("Hello!!\n")

with open("xyz.txt", "a") as file:
    file.write("Naman ")
