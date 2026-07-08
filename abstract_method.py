#abstract_method = a class that cannot be instantiated on it's own and need to be subclassed..
from abc import ABC,abstractmethod

class Vehicle:
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def __init__(self,name,year):
        self.name = name
        self.year = year
    
    def go(self):
        print(f"the vehicle {self.name} {self.year} is driving")
        
    def stop(self):
        print(f"the vehicle {self.name} {self.year} is stopping")
        
car1 = Car("mustang",1984)
car2 = Car("cla",2024)

cars = [car1, car2]
car1.go()
car1.stop()