class Counter:

    def __init__(self):
        self.count = 0

    def increase(self):
        print(self.count)
        self.count += 1

c = Counter()

for i in range(5):
    c.increase()
    
print(c.count)