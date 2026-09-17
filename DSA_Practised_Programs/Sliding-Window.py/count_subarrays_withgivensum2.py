def count_subarrays(nums, summ):
    cur_sum = 0
    count = 0
    seen = {0: 1}
    for num in nums:
        cur_sum += num
        count += seen.get(cur_sum - summ, 0)
        seen[cur_sum] = seen.get(cur_sum, 0) + 1
    return count

         
nums =[1, 2, 4, 3, 1, 4, 5, 6, 4, 3, 9, 4, 2, 5]
summ = 5
print(count_subarrays(nums, summ))