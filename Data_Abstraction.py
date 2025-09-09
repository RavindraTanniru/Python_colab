#Partial Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Class
    @abstractmethod
    def start(self):
        pass   # abstract method (must be overridden)

    def fuel_type(self):
        print("Petrol or Diesel")  # concrete method (already implemented)

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

obj = Car()
obj.start()       # Car starts with a key
obj.fuel_type()   # Petrol or Diesel


#Full Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

rect = Rectangle(5, 3)
print("Area:", rect.area())          # Area: 15
print("Perimeter:", rect.perimeter())  # Perimeter: 16

