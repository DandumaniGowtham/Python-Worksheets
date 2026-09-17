def count_subarray(nums, sm):
    add = 0
    count = 0
    left = 0
    for right in range(len(nums)):
        add = add + nums[right]
        while add > sm:
            add = add - nums[left]
            left = left + 1
        if add == sm:
            count = count + 1
    return count
nums = [1,2,4,3,1,4,5,6,4,3,9,4,2,5]
sm = 5
print(count_subarray(nums, sm))