#Write a python program to find an average of two numbers entered by the user.

a = input("Enter number 1: ")
b = input("Enter number 2: ")

# Convert input strings to integers
a = int(a)
b = int(b)
avg = (a + b) / 2

print(f"The avg of {a} and {b} is", avg)

#Output
# Enter number 1: 10
# Enter number 2: 20
# The avg of 10 and 20 is 15.0