while True :
    num = int(input("Enter your number : "))

    if( ( num % 3 == 0 ) and ( num % 5 == 0 )) :
        print(" Divisible by both 3 and 5 ") 

    elif ( num % 3 == 0 ) :
        print(" Divisible by 3 ")

    elif( num % 5 == 0 ) :
        print(" Divisible by 5 ")
        
    else:
        print(" Not divisible by 3 and 5 ")    


# while True :
    # n = int(input("Enter your number : "))
     
    # if (( num % 3 == 0 ) and ( num % 5 != 0)) :
    #     print(" Divisible by 3 ")

    # elif(( num % 5 == 0 ) and (num % 3 != 0)):
    #     print(" Divisible by 5 ")

    # elif( ( num % 3 == 0 ) and ( num % 5 == 0 )) :
    #     print(" Divisible by both 3 and 5 ")     
        
    # else:
    #     print(" Not divisible by 3 and 5 ")             
 