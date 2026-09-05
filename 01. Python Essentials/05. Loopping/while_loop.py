i = 1
while i < 6 :
    print(i)
    i = i + 1    
    
i = 1
while i <= 7 :
    print(i , "hi")
    i = i + 1    

#Print all even numbers between 0 to 10 :
i = 0 
while i <= 10 :
        print(i) 
        i = i + 2
i = 0
while i <= 10 :
    if (i % 2 == 0) :
        print(i)
    i = i + 1    

# Print all odd numbers betwwen 0 to 10 :
i = 1
while i <= 9 :
    print(i)
    i += 2
i = 0
while i <= 10 :
    if (i % 2 != 0) :
        print(i)
    i = i + 1
    
# Print the sum of all the numbers between 1 to 10 :
sum = 0
for i in range(1 ,11) :
     sum += i
     print(sum)
s = 0
i = 1
while i <= 10 : 
    s += i
    i += 1
    print(s)    
   
# Multiplication table of 5 :
i = 0
while i < 10 :
    i = i + 1
    n = 5*i
    print("5"," * ", i , " = " , n)

# Write a code that keep asking for a password until the correct password id 
while True :
    password =input("Enter your password : ")
    if password == "pass123" :
        print("You are welcomed!")
        break

p = ""
password1 = "pass1234"
while p != password1 :
    p = input("enter your password : ")  
print("You are welcomed!")      
    

