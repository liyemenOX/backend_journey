class students:
    class_year = 2024
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def describe(self):
        print(f"{self.name} {self.age}")
        
student1 = students("spongebob",30)
student2 = students("patrick",28)

student1.describe()
student2.describe()

print(student1.class_year)


