class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

s = Student("Ravi", 101)
s.display()

# Name: Ravi, Roll: 101