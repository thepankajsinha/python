class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

d = Demo()
del d  # Output: Object destroyed
