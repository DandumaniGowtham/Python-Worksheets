arr = [2, 4, 6, 8, 10, 12]
queries = [[1, 3], [0, 2], [2, 5]]
res = []

for query in queries:
    i = query[0]
    j = query[1]
    total = sum(arr[i:j+1])
    res.append(total)

print(res)




arr = [2, 4, 6, 8, 10, 12]
queries = [[1, 3], [0, 2], [2, 5]]
prefix = [0] * len(arr)
prefix[0] = arr[0]

res = []

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Prefix:", prefix)

# Answer queries
for left, right in queries:

    if left == 0:
        result = prefix[right]
    else:
        result = prefix[right] - prefix[left - 1]

    res.append(result)

print(res)