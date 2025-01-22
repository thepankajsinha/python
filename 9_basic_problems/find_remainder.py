# Write a python program to find remainder when a number is divided by z.

a = input("Enter number 1: ")
b = input("Enter number 2: ")

# Convert input strings to integers
a = int(a)
b = int(b)
remainder = a % b

print(f"The remainder of {a} divided by {b} is", remainder)

#Output
# Enter number 1: 20
# Enter number 2: 6
# The remainder of 20 divided by 6 is 2