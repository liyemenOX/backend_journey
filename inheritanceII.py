class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print("the animal is eating")
        
class Prey(Animal):
    def flee(self):
        print(f"the {self.name} is running away!")
        
class Predator(Animal):
    def hunt(self):
        print(f"the {self.name} is hunting ")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("peter")
hawk = Hawk("gogy")
fish = Fish("biby")

animal_list = [rabbit,hawk,fish]

rabbit.eat()
rabbit.flee()
hawk.hunt()
fish.flee()