arr = [1,2,4,6,10]
pre_sum = []
total = 0

for num in arr:
    total += num
    pre_sum.append(total)

print(pre_sum)


def prefix_sum(nums):
    prefix_sum = [0] * len(nums)

    prefix_sum[0] = nums[0]

    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    return prefix_sum


nums = [1,2,4,6,10]
print(prefix_sum(nums))