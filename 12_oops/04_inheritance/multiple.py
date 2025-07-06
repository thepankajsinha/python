class Father:
    def skills(self):
        print("Gardening, Coding")

class Mother:
    def hobbies(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    def own(self):
        print("Playing guitar")

c = Child()
c.skills()
c.hobbies()
c.own()

# Gardening, Coding
# Cooking, Painting
# Playing guitar
