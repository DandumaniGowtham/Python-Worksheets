def subArray_sum_equalsK(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0 : 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in freq:
            count += freq[prefix_sum-k]
    
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1 
            
    return count

nums = [2,5,2,1,6,5,2,6,9,]
k = 7
print(subArray_sum_equalsK(nums, k))