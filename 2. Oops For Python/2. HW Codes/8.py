class Student:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

s = Student("Rahul")
print(s.name)

s.change_name("Amit")
print(s.name)