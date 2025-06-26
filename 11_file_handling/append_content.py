import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

# Appending more content
with open(filename, "a") as f:
    f.write("This line is added later.\n")

print("✅ Content appended successfully.")