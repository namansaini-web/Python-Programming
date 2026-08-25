# [ __int__() ] --> Initialization an object when it is created.
# self --> Reference to the current object.

# Default Initialization:
class student:
    def __init__(self):
        print("Student object has got created!")

s1 = student()


# Initialization with Code reusability:
    # 1:
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Naman")
print(s1.name)
s2 = Student("Rahul")
print(s2.name)

    # 2:
class STUDENT:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

a1 = STUDENT("Naman", 17, "Chandigarh")
print(a1.name , a1.age , a1.city)

    # 3:
class students:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def display_profile(self):
        print(self.name, self.age , self.city)

b1 = students("Naman", 17, "Chandigarh")
b2 = students("Naman" , 18 , "kuk")
b1.display_profile()
b2.display_profile()

