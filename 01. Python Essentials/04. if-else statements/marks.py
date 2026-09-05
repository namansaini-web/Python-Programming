# Using if-elif-else only:

marks = int(input("Enter your marks : "))
if marks <= 32 : 
    print("Low")
elif ( marks >= 33) and ( marks <= 70 ) :
    print("Average")
else :
    print("High")  

# Using if-else only : 

mark = int(input("Enter your mark : "))
if mark <= 32 :
    print("Low")
else:
    if ( mark >= 33) and ( mark <= 70 ):
        print("Average")
    else:
        print("High")   

# Shortest way to write this code :

Marks = int(input("Enter your marks : "))
if Marks < 33 :
    print("Low")
elif ( Marks <= 70 ) :
    print(" Average ")
else:
    print(" High ")    
