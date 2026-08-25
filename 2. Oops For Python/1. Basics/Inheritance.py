# Inheritance --> 
#     1. Parent/Base Class: The class we are inheriting from.
#     2. Child/Derived Class: class which inherit from another class.

class parent:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def show_name(self):
        print(self.first_name , self.last_name)

p1 = parent("Naman" , "Saini")
p1.show_name()

class child(parent):
    pass

s1 = child("Naman" , "Saini")   # Proves that child class inherit all the properties of parent class. 
s1.show_name()

# --------------------------------------------------------------------------------------------------------------------

# Create a parent class Vehicle with an __init__ method that takes brand as input.
# Add a method display_brand() that prints the vehicle's brand.
# Create a child class Car that inherits from Vehicle.

class vehicle:

    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand of car : ", self.brand)

class car(vehicle):
    pass

c1 = car("BMW")
c1.display_brand()


class Car(vehicle):
    car_engine = "Thar"

c2 = Car("Mahendra")
c2.display_brand()
print("Car engine is : ", c2.car_engine)
                      