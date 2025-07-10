# 1. range(start, end, step)
# 2. default value of start =0, step = 1
# 3. start value is inclusive, end value is exclusive

# without start and step value
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4


# with start and step value
for i in range(2, 10, 2):
    print(i)  # Output: 2, 4, 6, 8


# with start and step value, iterating backwards
for i in range(10, 0, -2):
    print(i)  # Output: 10, 8, 6, 4, 2

    

# odd or even numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

