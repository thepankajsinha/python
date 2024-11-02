str = "Hello World"

# len() function: This function returns the length of the strings
print(len(str)) # Output: 11


# count(): counts the total number of occurrences of any character.
print(str.count("l")) # Output: 3


#upper(): Converts all characters to uppercase.
print(str.upper()) # Output: HELLO WORLD


#lower(): Converts all characters to lowercase.
print(str.lower()) # Output: hello world


# strip(): Removes leading and trailing whitespace
print(str.strip()) # Output: Hello World


#replace(old, new): Replaces occurrences of a substring with another.
print(str.replace("World", "Python")) # Output: Hello Python


#find(substring): Returns the index of the first occurrence of the substring or -1 if not found.
print(str.find("World")) # Output: 6


#isalpha(): Checks if all characters are alphabetic.
print(str.isalpha()) # Output: False


#isdigit(): Checks if all characters are digits.
print(str.isdigit()) # Output: False


#format(): Formats strings with placeholders.
name = "John Doe"
age = 30
print("My name is {} and I am {} years old.".format(name, age)) # Output: My name is John Doe and I am 30 years old.