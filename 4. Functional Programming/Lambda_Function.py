# lambda Function --> Anonymous Function.

# 1. 
def sq(x):
    return x*x
print(sq(5))
# 2. 
sq = lambda x: x*x
print(sq(5))

# Twice of a given nnumber:
twice = lambda x: 2*x
print(twice(3))

# Sum of two numbers:
sum = lambda a,b: a+b
print(sum(4,5)) 

# Max of two numbers:
    # 1.
mx = lambda x,y: max(x,y)
print(mx(7,8))
    # 2.
Mx = lambda x,y: x if x>y else y
print(Mx(7,8))

# Given number is odd or even:
odd_even = lambda x: "even" if x%2 == 0 else "odd"
print(odd_even(0))

# Return the last character of the given string:
last_character = lambda s: s[-1]
print(last_character("Python"))

# Write a code to return the product of the three numbers:
prod = lambda x,y,z: x*y*z
print(prod(3,4,5))

#