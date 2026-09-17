def max_consecutive_ones(nums, k):
    max_count = 0
    for i in range(len(nums) - k + 1):
        count = 0
        for j in range(i, i + k):
            if nums[j] == 1:
                count += 1
            else:
                count = 0
            max_count = max(count, max_count)

    return max_count

nums = [1,1,1,1,2,3,1,1,1,2,0,10,10,0,1,1,0,10,1,3,1,1,1]
k = 5
print(max_consecutive_ones(nums, k))




def max_con_ones(num_list, size):
    cur_ones = 0
    max_ones = 0
    left = 0
    for right in range(len(num_list)):
        if num_list[right] == 1:
            cur_ones += 1
        else:
            cur_ones = 0

        if right-left+1 > size:
            left = left + 1

        max_ones = max(max_ones, cur_ones)

        
    return max_ones


nums_list = [2,3,4,1,1,1,4,5,2,1,43,1,2,1,1,1,1,1,1,1,4]
k = 5
print(max_con_ones(nums_list, k))