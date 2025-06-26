#List is a built in data structure that is used to store multiple items in a single variable.
#List items can be of any data type.
# list is mutable, ordered, and allows duplicate elements.
# list can grow or shrink in size dynamically.


# Creating a list of string
fruits = ['apple', 'banana', 'cherry']

# Creating a list of number
num = [1, 2, 3, 4, 5]


# Creating a list of mixed data types
mixed_list = ['apple', 1, True, 3.14]



my_list = [1, 2, 3, 4, 5]

# print  the entire list using loop range
for i in range(len(my_list)):
    print(my_list[i], end=' ')  # Output: 1 2 3 4 5


# Accessing elements in a list
print(my_list[0])  # Output: 1 (first element)


# Accessing elements from the end of the list
print(my_list[-1])  # Output: 5 (last element)


# Modifying an element in a list
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]


# Adding elements to a list
my_list.append(6)  # Adds 6 to the end of the list
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]


# Inserting an element at a specific position
my_list.insert(1, 20)  # Inserts 20 at index 1
print(my_list)  # Output: [1, 20, 2, 10, 4, 5, 6]


# Popping an element from a list
popped_element = my_list.pop()  # Removes and returns the last element
print(popped_element)  # Output: 6
print(my_list)  # Output: [1, 20, 2, 10, 4, 5]


# Slicing a list
print(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)

