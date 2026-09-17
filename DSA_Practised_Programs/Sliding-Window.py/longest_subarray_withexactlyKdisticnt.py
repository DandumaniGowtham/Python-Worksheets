def long_subarray_exactKdistinct(nums, k):
    left = 0
    max_length = 0
    window = {}

    for right in range(len(nums)):
        window[nums[right]] = window.get(nums[right], 0) + 1
        while(len(window) > k):
            window[nums[left]] -= 1

            if window[nums[left]] == 0:
                del window[nums[left]]
            left += 1

        if len(window) == k:
            max_length = max(right-left+1, max_length)
    return max_length
nums = [1, 2, 3, 4, 5, 6]
k = 3
print(long_subarray_exactKdistinct(nums,k))