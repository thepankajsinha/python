student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE"
}

#returns all keys
print(student.keys())
# Output: dict_keys(['name', 'age', 'branch'])


# returns all values
print(student.values())
# Output: dict_values(['Rahul', 20, 'CSE'])


# returns all key-value pairs
print(student.items())
# Output: dict_items([('name', 'Rahul'), ('age', 20), ('branch', 'CSE')])


#get method
print(student.get("name"))
# Output: Rahul

#update method
student.update({"GPA": 9.0})
print(student)
# Output: {'name': 'Rahul', 'age': 20, 'branch': 'CSE', 'GPA': 9.0}
