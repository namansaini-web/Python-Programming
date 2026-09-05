class Book:
    def __init__(self, title):
        self.title = title
        
b = Book("Python Basics")
print(len(b.title))