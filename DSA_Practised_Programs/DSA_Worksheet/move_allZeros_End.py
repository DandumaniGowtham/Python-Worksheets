def move_zeros_toEnd(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] != 0:
            res.append(nums[i])
    while len(res) < len(nums):
        res.append(0)
    return res

nums = [1,2,0,3,5,0,3,0,5,0,0,6]
print(move_zeros_toEnd(nums))