def left_rotate_arraybyOne(nums):
    bit = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]    
    nums[-1] = bit
    return nums
nums = [1,2,3,4,5]
print(left_rotate_arraybyOne(nums))