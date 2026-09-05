# Methode 1 :
try:
    n = int(input("enter n : "))
    print(100/n)
except:
    print("error")

# Methode 2 :
try:
    a = int(input("Enter your number : "))
    b = int(input("Enter your number : "))
    print(a/b)
except Exception as e:
    print(e)

# Methode 3 :
try:
    num = int(input("enter num : "))
    print(100/num)
    a = [3,6]
    print(a[4])
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except ValueError:
    print("Only numbers are allowed!")
except Exception as e: 
    print("Some error occured!")

# else only runs when there is no error:
else :
    print("no error")

# finally block always exectues irrespective whether there is an error or not:
finally:
    print("Program Finished!")


# Example Code:
try:
    marks = 120
    if marks > 100:
        raise ValueError("Marks Invalid!")
    print(marks)
except ValueError as e:
    print(e)
print("Completed")


