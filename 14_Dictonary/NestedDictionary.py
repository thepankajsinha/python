#create a nested dictionary

studentInfo = {
    "name": "John Doe",
    "marks": {
        "math": 85,
        "science": 90,
        "english": 88
    }
}

print(studentInfo)
#{'name': 'John Doe', 'marks': {'math': 85, 'science': 90, 'english': 88}}

print(studentInfo["marks"]["math"])  #85