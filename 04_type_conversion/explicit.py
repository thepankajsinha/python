# 1. It is also called type casting.
# 2. It is used to convert one data type to another by the user.

#int to float conversion
num1 = 10
num2 = 20
sum = num1 + num2
print(sum) # Output: 30
print(type(sum)) # <class 'int'>


ans = float(sum)
print(ans) # Output: 30.0
print(type(ans)) # <class 'float'>







#The ord() function returns the ASCII value for a given character.
char = 'A'
ord_value = ord(char)
print(ord_value)  # Output: 65 (ASCII value of 'A')