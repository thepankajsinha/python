class Pigeon:
    def fly(self):
        print("Pigeon flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def lift_off(entity):
    entity.fly()

lift_off(Pigeon())     # Output: Pigeon flies
lift_off(Airplane())   # Output: Airplane flies
