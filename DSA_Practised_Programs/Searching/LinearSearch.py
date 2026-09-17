nums = [1,2,3,4,5,6]
target = 5
isFound = False
for i in range(len(nums)):
    if nums[i] == target:
        print(f"{target} found at index:", i)
        isFound = True
        break
else :
    print(f"{target} not found")
