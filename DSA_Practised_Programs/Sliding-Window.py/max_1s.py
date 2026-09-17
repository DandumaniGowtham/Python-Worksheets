def max_ones(nums, k):
    left = 0
    sum_curr = sum(nums[:k])
    max_sum = sum_curr
    
    for right in range(k, len(nums)):
        sum_curr -= nums[left]
        sum_curr += nums[right]
        max_sum = max(sum_curr, max_sum)

        left += 1
    return max_sum

nums = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
print(max_ones(nums, 5))