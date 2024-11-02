# break
count = 1
while(count <= 5):
    print(count)
    if(count == 3):
        break
    count = count + 1


# 1
# 2
# 3


# continue
count = 1
while(count <= 5):
    if(count == 3):
        count = count + 1
        continue
    print(count)
    count = count + 1


# 1
# 2
# 4
# 5