def sum_k_consecutive(nums, k):
    left = 0
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for right in range(k, len(nums)):
        curr_sum -= nums[left]
        curr_sum += nums[right]
        max_sum = max(curr_sum, max_sum)
        left += 1
    return max_sum / k

nums = [2,4,5,8,3,9,5,8,1,4]
k = 3
print(sum_k_consecutive(nums, k))