#duck_typing -> "if it looks like a duck, quacks like a duck then it must be a duck"

class Dog:
    def speak(self):
        print("WOOFF!")

class Cat:
    def speak(self):
        print("MEOW!")

class Car:
    def speak(self):
        print("HONK")
        
entities = [Dog(),Cat(),Car()]
for entity in entities:
    entity.speak()