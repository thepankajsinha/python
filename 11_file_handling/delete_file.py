import os

filename = r"C:\Users\momda\OneDrive\Desktop\python\11_file_handling\sample.txt"

# Deleting the file
if os.path.exists(filename):
    os.remove(filename)
    print("🗑️ File deleted successfully.")
else:
    print("❌ File does not exist.")