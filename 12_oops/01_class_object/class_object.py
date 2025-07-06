#class creation
class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Branch: {self.branch}")


#creating object of class Student
Student1 = Student("Alice", 20, "CSE")
Student1.display()
