# 1.Identity operators are used to determine whether the value of a variable is of a certain type or not.
# 2.Identity operators can also be used to determine whether two variables are referring to the same object or not.

#is
num1 = 5
print(type(num1) is int)
# True

num2 = num1
print(id(num1))
# 140724673382968


print(id(num2))
# 140724673382968

print(num1 is num2)
# True (num1 and num2 refer to the same object)


# is not
num3 = 10
print(num1 is not num3)
# True (num1 and num3 refer to different objects)