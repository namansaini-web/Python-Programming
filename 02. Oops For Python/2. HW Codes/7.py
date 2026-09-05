class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")
            
s = Student("Rahul", 35)
s.result()