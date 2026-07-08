# polymorphism ==> greek work means poly -> "many" and morph ->"forms"
#polymorphism is achieved using two ways -->> duck typing + inheritance
import math
from abc import ABC,abstractmethod

class Shapes:
    
    def __init__(self,color,is_valid):
        self.color = color
        self.is_valid = is_valid
        
    @abstractmethod
    def area(self):
        pass    

class Circle(Shapes):
    
    def __init__(self,radius,color,is_valid):
        self.radius = radius
        super().__init__(color,is_valid)
    
    def area(self):
        return math.pi * self.radius **2 
    
class Square(Shapes):
    
    def __init__(self,width,color,is_valid):
        self.width = width
        super().__init__(color,is_valid)
        
    def area(self):
        return self.width ** 2
    
class triangle(Shapes):
    def __init__(self,width,height,color,is_valid):
        self.width = width
        self.height = height
        super().__init__(color,is_valid)
    
    def area(self):
        return 0.5 * self.width * self.height
    
class Pizza(Circle):
    def __init__(self,topping,radius,color,is_valid):
        super().__init__(radius,color,is_valid)
        self.topping = topping
    
shapes = [Circle(3,"blue",True),Square(4,"yellow",False),Pizza("margherita", 4.3, "golden", True),triangle(3,4,"white",True)]
for shape in shapes:
    print(shape.area())