numbs = [1,2,2,4,5,3,4,5]
print(numbs)
for i in numbs:
    count = 0
    for j in numbs:
        if i == j:
            count = count + 1
    print(f"count of {i} : {count}")


list = []
for i in numbs:
    if i not in list:
        count = 0
        for j in numbs:
            if i == j:
                count = count + 1
        list.append(count)
print(list)


numbs = [1,1,2,2,3,4,5,3,4,5]
visited = []

i = 0
while i < len(numbs):
    if numbs[i] not in visited:
        count = 0
        j = 0
        while j < len(numbs):
            if numbs[i] == numbs[j]:
                count += 1
            j += 1
        print(numbs[i], ":", count)
        visited.append(numbs[i])
    i += 1


numbers = [1,2,3,1,2,3,4,5,6,3,3,3,3,5]
coppy = numbers.copy()
print(numbers)
for i in range(len(coppy)):
    count = 0
    for j in coppy:
        if coppy[i] == j:
            count = count + 1
    numbers[i] = count
print(numbers)