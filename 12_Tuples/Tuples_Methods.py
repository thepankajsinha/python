#create a new tuple
tuple_example = (1, 2, 3, 4, 5)


#print the tuple
print(tuple_example) #output: (1, 2, 3, 4, 5)


#length of the tuple
print(len(tuple_example))  # Output: 5


#slice the tuple
print(tuple_example[0:3])  # Output: (1, 2, 3)

print(tuple_example[2:])  # Output: (3, 4, 5)

print(tuple_example[1:3])  # Output: (2, 3)



#access elements of the tuple
print(tuple_example[0])  # Output: 1



#convert the tuple to a list
list_example = list(tuple_example)
print(type(list_example))  # Output: <class 'list'>



#modify elements of the list
list_example[0] = 10
print(list_example) # Output:[10, 2, 3, 4, 5]



#convert the list back to a tuple
tuple_example = tuple(list_example)
print(type(tuple_example)) # Output: <class 'tuple'>



print(tuple_example) #Output: (10, 2, 3, 4, 5)


