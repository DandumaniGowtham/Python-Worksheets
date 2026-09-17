def binary_search(num_list, target):
    low = 0
    high = len(num_list) - 1
    while(low <= high):
        mid = (low + high) // 2
        if num_list[mid] == target:
            return mid
        elif target > num_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return "Element not found!"

num_list = [20,45,67,3,66,76]
num_list.sort()
print(binary_search(num_list, 67))