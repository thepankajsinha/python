num1 = int(input("Enter a number 1:"))
num2 = int(input("Enter a number 2:"))
num3 = int(input("Enter a number 3:"))

if(num1 >= num2 and num1 >= num3):
    print(f"Largest number is : {num1}")
elif(num2 >= num3):
    print(f"Largest number is : {num2}")
else:
    print(f"Largest number is : {num3}")

# Enter a number 1:10
# Enter a number 2:15
# Enter a number 3:2
# Largest number is : 15
