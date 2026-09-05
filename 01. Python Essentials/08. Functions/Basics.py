def main_fun():
    print("hello!")

main_fun()    


#def naman():
#    print("hello Naman!")
#def kavita():
#    print("hello Kavita!")
#def naresh():
#    print("hello Naresh!")
#def kunal():
#    print("hello Kunal!")  
          
#while (True):
#name = input("Enter your name: ")
#    if name == "naman":
#       naman()
#    elif name == "kavita":
#       kavita()
#    elif name == "naresh":  
#       naresh()
#    elif name == "kunal":
#       kunal()  
#    else:
#       print("invald name!")      
         

def greet(name):
    print("Hello", name, "!")
name = input("enter your name : ")
greet(name)             


def show(Name,age):
    print("Name is", Name )
    print("Age is ", age)
Name = input("enter your name : ")
age = int(input("enter your age : "))
show(Name, age)


#Keyworded arguments :
def info(name, age):
    print("Name is ", name)
    print("Age is ", age)
NAME = input("Enter your name : ")
AGE = int(input("Enter your age : "))
info(age = AGE, name = NAME)


#Default argument :
def display(name="Raj"):
    print(name)
display()    