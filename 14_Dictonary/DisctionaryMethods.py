studentInfo = {
    "name": "John Doe",
    "age": 21,
    "GPA": 8.9,
    "is_Pass": True,
}

#returns all keys
print(studentInfo.keys()) 
# Output: dict_keys(['name', 'age', 'GPA', 'is_pass'])


# returns all values
print(studentInfo.values())
# Output: dict_values(['John Doe', 21, 8.9, True])


# returns all key-value pairs
print(studentInfo.items())
# dict_items([('name', 'John Doe'), ('age', 21), ('GPA', 8.9), ('is_Pass', True)])


#get method
print(studentInfo.get("name"))
#John Doe

#update method

studentInfo.update({"name": "Jane Doe"})
print(studentInfo)
#{'name': 'Jane Doe', 'age': 21, 'GPA': 8.9, 'is_Pass': True}