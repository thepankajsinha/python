#create a nested dictionary
# Nested dictionary is a dictionary inside another dictionary

# Creating a nested dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE",
    "subjects": {
        "semester1": ["Math", "Physics", "Chemistry"],
        "semester2": ["Data Structures", "Algorithms"]
    }
}

# Accessing values in a nested dictionary
print(student["name"])  # Output: Rahul

print(student["subjects"]["semester1"])  # Output: ['Math', 'Physics', 'Chemistry']

# Adding a new subject to semester1
student["subjects"]["semester1"].append("English")
print(student["subjects"]["semester1"])  # Output: ['Math', 'Physics', 'Chemistry', 'English']

# Adding a new semester
student["subjects"]["semester3"] = ["Operating Systems", "Computer Networks"]
print(student["subjects"]["semester3"])  # Output: ['Operating Systems', 'Computer Networks']
