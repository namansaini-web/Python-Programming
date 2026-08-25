# CLASS VARIABLE AND INSTANCE VARIABLE:

class student:

    college = "UIET KUK"     # Class Variable.

    def __init__(self, name):
        self.name = name     # Instance Variable.

s1 = student("Naman")
s2 = student("Rahan")

print(s1.name, s1.college)
print(s2.name, s2.college)
