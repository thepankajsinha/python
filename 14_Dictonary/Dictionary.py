# Dictonary is used to store data in key: value pairs
# Dictonary is unordered, changeable and dont allow duplicate keys

# Creating a dictionary
studentInfo = {
    "name": "John Doe",
    "age": 21,
    "GPA": 8.9,
    "is_Pass": True,
}


# print disctronary 
print(studentInfo)
# Output: {'name': 'John Doe', 'age': 21, 'GPA': 8.9, 'is_pass': True}


# Accessing values using keys
print(studentInfo["name"])  # Output: John Doe
print(studentInfo["age"])   # Output: 21
print(studentInfo["GPA"])   # Output: 8.9
print(studentInfo["is_Pass"]) # Output: True

#update values
studentInfo["GPA"] = 9.0  
print(studentInfo["GPA"]) # 9.0


# check if a key exists in dictionary
print("is_pass" in studentInfo) # Output: True


# add new key-value pair
studentInfo["major"] = "Computer Science"
print(studentInfo) 
# {'name': 'John Doe', 'age': 21, 'GPA': 9.0, 'is_Pass': True, 'major': 'Computer Science'}

# delete key-value pair
del studentInfo["major"]
print(studentInfo)
#{'name': 'John Doe', 'age': 21, 'GPA': 9.0, 'is_Pass': True}