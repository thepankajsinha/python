import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

# Appending more content
file = open(filename, "a")
file.write("This line is added later.\n")

file.close()

print("✅ Content appended successfully.")