try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Invalid input! Not a number.")
else:
    print("Result is:", result)
finally:
    print("This block runs no matter what.")


# Enter a number: 0
# Can't divide by zero!
# This block runs no matter what.