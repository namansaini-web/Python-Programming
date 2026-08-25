# METHOD 1
s = input()
names = s.split()
print(names)
unique_names = []
for Name in names:
    if Name not in unique_names:
        unique_names.append(Name) 
print(unique_names)


# METHOD 2
Names = []
while True:
    name = input("Enter your name : ")
    Names.append(name)
    if name == "stop":
        break
print()
Names.remove("stop")

print(Names)
n = list(dict.fromkeys(Names))
print(n)