# Hides internal details and shows only necessary parts.
# Use abc module to create abstract classes.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

c = Car()
c.start_engine()  # Output: Car engine started
