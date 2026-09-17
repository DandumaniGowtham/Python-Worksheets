list = [3,22,4,5,3]
smallest = float('inf')
largest = float('-inf')
for i in list:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print(smallest , largest)
