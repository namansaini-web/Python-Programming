num = [1,2,3,4,5,6,7,8]

# Return a list which has only even number from the given list:
even_num = list(filter(lambda x: x%2 == 0, num))
print(even_num)

# filtre numbers greater then 10:
numbers = [5,10,15,25,8]
result = list(filter(lambda x: x>10, numbers))
print(result)

# Example: Nested mapping and filering.
n = [3,6,12,9]
result = list(map(lambda x: x+1, filter(lambda x: x%6 == 0, n)))
print(result)
