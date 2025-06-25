#List methods:


#create a list
list_of_numbers = [1, 2, 3, 4, 5]



#Length of the list
print(len(list_of_numbers))  # Output: 5



#print a list
print(list_of_numbers)  # Output: [1, 2, 3, 4, 5]




#extend method- Adds all elements to the end of the list.
list_of_numbers.extend([7, 8, 9])
print(list_of_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



#remove method- Removes the first occurrence of the specified item
list_of_numbers.remove(10)
print(list_of_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



# pop method -
# Removes and returns the item at the specified index. If no index is specified, it removes and returns the last item.

element = list_of_numbers.pop()
print(element)  # Output: 9
print(list_of_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

#pop method with index
element = list_of_numbers.pop(3) # 3 is index
print(element)  # Output: 4
print(list_of_numbers)  # Output: [1, 2, 3, 5, 6, 7, 8]




#count method - Returns the number of times the specified item appears in the list.
count = list_of_numbers.count(5)
print(count)  # Output: 1



#reverse method - Reverses the order of the list.
list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers.reverse()
print(list_of_numbers)  # Output: [5, 4, 3, 2, 1]



#sort method

# sort in ascending order
list_of_numbers = [5, 3, 8, 2, 1]
list_of_numbers.sort()
print(list_of_numbers)  # Output: [1, 2, 3, 5, 8]

# sort in descending order
list_of_numbers.sort(reverse=True)
print(list_of_numbers)  # Output: [8, 5, 3, 2, 1]



#copy method
copied_list = list_of_numbers.copy()
print(copied_list)  # Output: [8, 5, 3, 2, 1]


#index method-Returns the index of the first occurrence of the specified item
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index) # Output: 1


#clear method - Removes all elements from the list, leaving it empty.
list_of_numbers.clear()
print(list_of_numbers)  # Output: []


