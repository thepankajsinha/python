import os
import sys

print(os.getcwd())  # Output: C:\Users\momda\OneDrive\Desktop\python

#create new folder
os.mkdir("test_directory")

#check if folder exists
print(os.path.exists("test_directory"))  # Output: True


#rename folder
os.rename("test_directory", "renamed_directory")


#remove folder
os.rmdir("renamed_directory")


#list all folders in current directory
print(os.listdir())  


print(sys.version)  # Output: 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)]