def count_items(items_list):
    frequency = {}
    for item in items_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
  
n = int(input("Enter size of list:"))
fruits = []
for i in range(n):
  fruits.append(input())
print(count_items(fruits))
