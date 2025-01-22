#String slicing allows you to extract a substring from a given string
#Note: end index is not included
#string[start:end]


text = "Hello, World!"

# Basic slicing
print(text[0:5])   # Output: 'Hello'
print(text[7:12])  # Output: 'World'

# Omitting start or end
print(text[:5])    # Output: 'Hello' (from start to index 5)
print(text[7:])    # Output: 'World!' (from index 7 to end)