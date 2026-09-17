def left_rotateby_kplaces(nums, k):
    newlist = []
    j = 0
    for i in range(k, len(nums)):
        newlist.insert(j, nums[i])
        j += 1
    for i in range(0, k):
        newlist.insert(j, nums[i])
        j += 1
    return newlist
    
nums = [1,2,3,4,5,6]
k = 3
print(left_rotateby_kplaces(nums, k))



def left_rotateby_kplaces(nums, k):
    for _ in range(k):
        first = nums[0]

        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]

        nums[-1] = first

nums = [1, 2, 3, 4, 5, 6]
k = 3

left_rotateby_kplaces(nums, k)
print(nums)


def left_rotateby_kplaces(nums, k):
    nums[:] = nums[k:] + nums[:k]

nums = [1, 2, 3, 4, 5, 6]
k = 3

left_rotateby_kplaces(nums, k)
print(nums)