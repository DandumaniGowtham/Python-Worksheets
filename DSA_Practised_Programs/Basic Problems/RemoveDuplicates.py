nums = [2,1,4,2,1,3,5,6,3,3,5]
uniq = list(set(nums))
print(uniq)

uniq2 = []
for i in nums:
    if i not in uniq2:
        uniq2.append(i)
print(uniq2)

nums[:] = list(set(nums))
print(nums)

numbers = [1,1,2,2,3,4,5,6,6,7]
count = 0
while(count < len(numbers)):
    if numbers[count] in numbers[:count]:
        numbers.pop(count)
    else:
        count = count + 1
print(numbers)


###############

numbs = [1,1,2,2,3,4,5,3,4,5]
nums = sorted(numbs)
print(numbs)
i = 0
while(i < len(nums) -1):
    if nums[i] == nums[i+1]:
        nums.pop(i)
    i = i + 1
print(nums)

for i in range(len(nums) -2,-1,-1):
    if nums[i+1] == nums[i]:
        nums.pop(i)
print("second", nums)

