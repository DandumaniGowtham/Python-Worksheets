def longest_subarray_disticnt_N(nums, k):
   left = 0
   length = 0
   freq = {}

   for right in range(len(nums)):
      freq[nums[right]] = freq.get(nums[right], 0) + 1

      while len(freq) > k:
         freq[nums[left]] -= 1

         if freq[nums[left]] == 0:
            del freq[nums[left]]
         left += 1

      length = max(length, right-left+1)
   return length

nums = [2,1,2,3,4,1,2,1,2,2,2,2,1]
k = 2
print(longest_subarray_disticnt_N(nums, k))