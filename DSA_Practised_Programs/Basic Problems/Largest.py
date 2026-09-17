nums = [1,2,3,4]
largest = 0
for num in nums:
    if(largest < num):
        largest = num
print(largest)

first_largest = 0
second_largest = 0
for i in nums:
    if i > first_largest:
        second_largest = first_largest
        first_largest = i
    elif i > second_largest and i != first_largest:
        second_largest = i
print(f"first_largest: {first_largest} and second largest : {second_largest}")

numbers = sorted(nums)
print(numbers[-2])

list_ok = [1,2,3,4,4]
uniq_nums = list(set(list_ok))
uniq_nums.sort()
print(uniq_nums[-2])