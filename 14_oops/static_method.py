class Demo:
    count = 0

    def __init__(self):
        Demo.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        print("Hello from static method")

d1 = Demo()
d2 = Demo()
print(Demo.get_count())  # Output: 2
Demo.greet()             # Output: Hello from static method
