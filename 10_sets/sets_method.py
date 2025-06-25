#create a sets
set_example = {1, 2, 3, 4, 5}

#add an element to the set
set_example.add(6)
print(set_example)  # Output: {1, 2, 3, 4, 5, 6}


#remove an element from the set
set_example.remove(4)
print(set_example)  # Output: {1, 2, 3, 5, 6}


#check if an element is in the set
print(6 in set_example)  # Output: True
print(7 in set_example)  # Output: False


#union of two sets
set_example2 = {4, 5, 6, 7, 8}
union_set = set_example.union(set_example2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

#pop method
union_set.pop()
print(union_set)
# {2, 3, 4, 5, 6, 7, 8}


#intersection method
intersection_set = set_example.intersection(set_example2)
print(intersection_set)  # Output: {4, 5, 6}