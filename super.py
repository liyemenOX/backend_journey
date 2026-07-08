
from abc import ABC,abstractmethod
class Shapes(ABC):
    def __init__(self,color,exists):
        self.is_color = color
        self.exists = exists
    
    @abstractmethod
    def area(self):
        pass
    
class circle(Shapes):
    def __init__(self,radius,color,exists):
        super().__init__(color,exists)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
    
shapes = [circle(3,"blue",True)]
for shape in shapes:
    print(f"{shape.area()}")
    