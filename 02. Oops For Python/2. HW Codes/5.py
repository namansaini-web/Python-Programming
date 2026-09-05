class Laptop:

    def __init__(self, brand):
        self.brand = brand
        
    def display(self):
        print(self.brand)

l = Laptop("Dell")

l.display()
l.display()