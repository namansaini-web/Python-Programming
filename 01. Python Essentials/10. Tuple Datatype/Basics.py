days = ("Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday")
day = ()

print(type(days))
print(len(days))
print(len(day))
print(days.index("Monday"))

# Accessing a element (Indexing): 
print(days[3])
print(days[-2])

# Tuple with one element:
a =(1)
print(type(a)) # int seems to be tuple
b = (1,)
print(type(b)) # one elem tuple

# Slicing a tuple:
print(days[1:3])
print(days[1:6:2])

# Membership operator in tuple:
x = ("A", "B", "C", "D")
print("P" in x)
print("X" not in x)

# Pre-defined Operators:
num = (2,4,6,8,10,6)
print(sum(num))
print(num.count(6))
print(num.index(10)) #gives the first index of occurence of the provided elem.

numbers = (15, 46, 78, 85, 11)
print(max(numbers))
print(min(numbers))

h = (1,2,3)
print(h*2)