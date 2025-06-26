# Dictonary is used to store data in key: value pairs
# Dictonary is unordered, changeable and dont allow duplicate keys

# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE"
}

# Accessing values using keys
print(student["name"])  # Output: Rahul


#Updating values
student["age"] = 21
print(student["age"])  # Output: 21


# Adding new key-value pairs
student["GPA"] = 9.0
print(student)  # Output: {'name': 'Rahul', 'age': 21, 'branch': 'CSE', 'GPA': 9.0}


# check if a key exists in dictionary
if "branch" in student:
    print("Branch exists in the dictionary")  # Output: Branch exists in the dictionary


# delete key-value pair
del student["GPA"]
print(student)  # Output: {'name': 'Rahul', 'age': 21, 'branch': 'CSE'}