# Write a program to store seven fruits in a list entered by the user

fruits = []

for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print(fruits)


# Output:
# Enter fruit 1: Apple
# Enter fruit 2: Mango
# Enter fruit 3: Guava
# Enter fruit 4: Grapes
# Enter fruit 5: Banana
# Enter fruit 6: pineapple
# Enter fruit 7: Coconut
# ['Apple', 'Mango', 'Guava', 'Grapes', 'Banana', 'pineapple', 'Coconut']