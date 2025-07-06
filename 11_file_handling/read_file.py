import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

# Reading the content of the file
file = open(filename, "r")
content = file.read()
print(content)

file.close()


# Hello, this is the first line.
# This is the second line.