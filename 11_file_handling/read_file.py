import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

# Reading the content of the file
with open(filename, "r") as f:
    content = f.read()
    print(content)


# Hello, this is the first line.
# This is the second line.
# This line is added later.