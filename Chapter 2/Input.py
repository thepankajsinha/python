# This function allows the user to take input from the keyboard as a string.


#Without typecasting the input in interger
a = input("Enter number 1: ")
b = input("Enter number 2: ")
print(a+b)
# Enter number 1: 10
# Enter number 2: 20
# 1020




# With typecasting the input in integer
a = input("Enter number 1: ")
b = input("Enter number 2: ")

a = int(a) # convert input string a to integer
b = int(b) # convert input string b to integer
print(a+b)

# Enter number 1: 10
# Enter number 2: 20
# 30