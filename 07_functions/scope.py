# scope of variables in python

# Global variable-
# A variable that is defined outside any function or any block is known as a global variable

# Local variable-
# A variable that is defined inside any function or a block is known as a local variable.




x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print("Inside function:", x, y)

my_function()  # Output: Inside function: 10 5

print(y)  # Output: NameError: name 'y' is not defined