#Function with default parameters

def greet(name="User", greeting="Hello"):
    print(f"{greeting}, {name}!")



greet() # Output: Hello, User!

greet("John Doe") # Output: Hello, John Doe!

greet("Jane Smith", "Hi") # Output: Hi, Jane Smith!