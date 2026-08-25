class Mobile:
    def __init__(self, brand):
        self.brand = brand
        
m = Mobile("Samsung")
print(hasattr(m, "brand"))

class Movie:
    def __init__(self, name):
        self.name = name 

movie = Movie("Avatar")
print(hasattr(movie, "rating"))

# hasattr --> gives true or false.