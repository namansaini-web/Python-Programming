for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i, end=" ")  

for i in range(1,6):
    print("hi") 


# Print 1 to 5 both inclusive 
for i in range(5) :
    print(i + 1)


# Print 10 to 1 both inclusive
for i in range(10):
    print(10 - i)  
for i in range(10 , 0 , -1) :
    print(i)   


# Print 0 to 10 , only even numbers 
for i in range(0 , 11, 2) :
    print(i)
for i in range(6) :
    print(i*2)

for i in range(11) :
    if i%2 == 0 :
        print(i)   


# Print 0 to 10 , only odd numbers 
for i in range(1, 10, 2) :
    print(i)
for i in range(11) :
    if i%2 != 0 :
        print(i)


# Print square of all numbers from 2 to 7 
for i in range(2,8) :
    print(i*i) #(or (i**2))

# Mltiplication table of 5  
for i in range(1,11) :
    print("5", " * " , i , " = ", i*5)  


# Print all the multiples of 5 from 1 to 5
for i in range(1,51) :
    if i%5 == 0 :
        print(i) 


# Print all the divisors of 5 from 1 to 50
for i in range(1,51) :
    if (i % 5 == 0) :
        print(i)


