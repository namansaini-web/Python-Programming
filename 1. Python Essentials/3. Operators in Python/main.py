#Arthmetic Operators:

a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))
print( "a + b", "=" , a + b )
print( "a - b", "=" , a - b)
print( "a * b", "=" , a * b)
print( "a / b", "=" , a / b)
print( "a // b", "=" , a // b)
print( "a ** b", "=" , a ** b)
print( "a % b", "=" , a % b)


# These methods are same to use arthmetic operators
x = 10

x = x + 10
print(x)

x += 10
print(x)


# Comparison Operators:
   # Examples:
x = 10<5
print(x)

x = 10>5
print(x)

x = 5==5
print(x)

x = 3!=3
print(x)

#Logical Operators:
  # { and , or , not }

x = (4<5) and (4>10)
print(x)

x = (4>2) or (4<2)
print(x)

x = not(4<3)
print(x)

  # Examples:

x = not( (3>3) and (4>5))
print(x)

x = (4>5) and ( not((3<4) or ((6>3) and (not(4<7) ))) )
print(x)

# Membership Operators 

x = "a" in "naman"
print(x)
y = "b" in "naman"
print(y)

x = "a" not in "naman"
print(x)
y = "b" not in "naman"
print(y)
