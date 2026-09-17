def longest_subarray(nums, k):
    summ = 0
    left = 0
    max_length = 0

    for right in range(len(nums)):
        summ += nums[right]

        while summ > k:
            summ -= nums[left]
            left += 1

        max_length = max(max_length, right-left+1)


    return max_length


nums = nums = [2,4,2,4,5,5,24,42]
k = 10
print(longest_subarray(nums, k))