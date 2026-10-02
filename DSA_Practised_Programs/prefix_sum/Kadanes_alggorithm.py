arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sum = 0
max_sum = 0
for num  in arr:
    sum += num
    if sum < 0:
        sum = 0
    max_sum = max(max_sum, sum) 

print(max_sum)



current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)