def smallest_sub_array(nums, target):
    curr_sum = 0
    left = 0
    size = float("inf")
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            size = min(right-left+1, size)
            curr_sum -= nums[left]
            left += 1
            
    if size == float("inf"):
        return 0
    return size


nums = [3,2,3,5,3,10,5,2,4,3]
target = 15
print(smallest_sub_array(nums, target))