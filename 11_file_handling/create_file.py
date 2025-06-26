import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

#Writing to a file (creates the file if it doesn't exist)
with open(filename, "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("This is the second line.\n")

print("✅ File written successfully.")






