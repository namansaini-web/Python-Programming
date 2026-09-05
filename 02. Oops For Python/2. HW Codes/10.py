class car:
    def __init__(self,brand):
        self.brand = brand

car1 = car("BMW")
car2 = car1   # After this both are refering to the same loctaion so, they will give same result.

car2.brand = "Audi"
print(car1.brand)