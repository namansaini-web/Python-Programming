while True :
    bmi = float(input("Enter your BMI value : "))
    if ( bmi <= 18.5 ) :
        print(" You are underweight ")
    elif ( bmi <= 24.9 ) :
        print(" You have normal weight ")
    elif ( bmi <= 29.9 ) :
        print(" You are overweight ")
    elif ( bmi >= 30.0 ) :
        print(" You are obese ")          
