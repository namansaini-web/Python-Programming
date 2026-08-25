# Return a list of the cube of every number in the given list:
print(list(map(lambda x: x**3, [1,2,3,4])))

# Return a list with the plus 5 of every number in the list:
    # 1.
l = [1,2,3,4,5]
plus = list(map(lambda x: x+5, l))
print(plus)
    # 2.
plus = list(map(lambda x: x+5, [1,2,3,4,5]))
print(plus)
    # 3.
print(list(map(lambda x: x+5, [1,2,3,4,5])))

# In a list of string, convert all strings to all uppercase and display the new list:
l = ["Naman", "Suraj", "Ishan", "Harsh", "Abhinav"]
print(list(map(lambda s: s.upper(), l)))

# List of prices is given, return a new list with 18% gst inlcude prices:
prices = [100,200,250,400]
gst_p = list(map(lambda x: (x + x*0.18), prices))
print(gst_p)

# First make a add function then use it to genrate a list to add 5 to each element of a list:
add = lambda a,b: a + b
numbers = [1,2,3]
result = list(map(lambda x: add(x,5), numbers))
print(result)

# Return a list with length of strings in a list:
words = ["AI", "Machine", "Python"]
result = list(map(len, words))
print(result)