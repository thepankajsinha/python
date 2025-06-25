# String is a data type.
# String is a sequence of characters enclosed in quotes.

#How to create a string
# Single quoted string
str1 ='Hello World'


# Double quoted string
str2 = "Hello World"

# Triple quoted string is used to create multiline string
str3 = '''
Hello
World
    ''' 



#characterstics of string
# 1. Strings are immutable: Once created, the characters in a string cannot be changed.
str = 'Hello World'
str[0] = 'h'  # This will raise an error because strings are immutable

# 2. Strings can be indexed: Each character in a string has a position, starting from 0.
print(str[0])  # Output: H

# 3. Strings can be sliced: You can extract a substring from a string using slicing
print(str[0:5])  # Output: Hello

# 4. Strings can be concatenated: You can combine two or more strings using the + operator.
str4 = str1 + ' ' + str2  # Concatenation
print(str4)  # Output: Hello World Hello World

# 5. Strings can be repeated: You can repeat a string multiple times using the * operator.
str5 = str1 * 3  # Repetition
print(str5)  # Output: Hello WorldHello WorldHello World

