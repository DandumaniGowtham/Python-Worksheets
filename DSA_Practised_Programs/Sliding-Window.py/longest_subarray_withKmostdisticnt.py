def longest_subarray(nums, k):
    left = 0
    max_length = 0
    window = {}

    for right in range(len(nums)):

        # Add current number
        window[nums[right]] = window.get(nums[right], 0) + 1

        # More than k distinct numbers
        while len(window) > k:
            window[nums[left]] -= 1

            if window[nums[left]] == 0:
                del window[nums[left]]

            left += 1

        # Current window is valid
        max_length = max(max_length, right - left + 1)

    return max_length


nums = [1, 2, 1, 2, 3, 2, 2]
k = 2

print(longest_subarray(nums, k))





