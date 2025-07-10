import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

#Writing to a file (creates the file if it doesn't exist)
file = open(filename, "w")
file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")

file.close()

print("✅ File written successfully.")






