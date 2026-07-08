class Animal:
    
    def __init__(self,name,is_alive):
        self.name = name
        self.is_alive = is_alive
        
    def eat(self):
        print(f"{self.name} is eating")
        
class Dog(Animal):
    pass
    
class Cat(Animal):
    pass
        
animals = [Dog("goofy",True),Cat("leo",False)]

for animal in animals:
    animal.eat()