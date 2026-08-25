num = {2,3,6,1,8,1}

print(type(num))
print(len(num))
#print(num[0])     --> No concept of indexing in set.

nums = {2,4,"Naman",True,"Naman"}
print(type(nums))
print(len(nums))

# Method to create an empty Set:
empty_dic = {}
empty_set = set()

# Inbuild function:
n = {2,3,6,1,8,1}

n.add(10)
print(n)

print(max(n))
print(min(n))

n.remove(1)
print(n)
# n.remove(4)     --> Gives an error because it is not in set --> "Key error"

item = n.pop()    # Removes a random element from the set 
print(item)
print(n)

n.clear()     # make the set empty.
print(n)


numbers = [10,20,30,20,10]
unique = set(numbers)
print(len(unique))


# String to Set:
text = "banana"

letters = set(text)
print(letters)
