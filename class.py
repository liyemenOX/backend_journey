#creating a car class...
#. ->> attribute access operator
class car:
    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color
        
    def describe(self):
        print(f"{self.model} {self.year} {self.color}")

# adding the other objects also...
    def drive(self):
        print(f"{self.model} is driving!")

    def stop(self):
        print(f"{self.model} is stopped!")
    
car1 = car("mustang", 1984, "blue")
car1.describe()
car1.drive()
