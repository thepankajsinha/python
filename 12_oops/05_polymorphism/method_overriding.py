# Same method name behaves differently in different classes.

class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")

b = Bird()
s = Sparrow()
b.fly()  # Output: Some birds can fly
s.fly()  # Output: Sparrow flies high
