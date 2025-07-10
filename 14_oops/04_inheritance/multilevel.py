class Grandparent:
    def legacy(self):
        print("Heritage")

class Parent(Grandparent):
    def profession(self):
        print("Doctor")

class Child(Parent):
    def ambition(self):
        print("Engineer")

c = Child()
c.legacy()
c.profession()
c.ambition()

# Heritage
# Doctor
# Engineer
