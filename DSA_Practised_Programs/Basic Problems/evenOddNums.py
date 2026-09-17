nums = [ 1,5,2,7,9,4,5,]
even_count = 0
odd_count = 0
for i in nums:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1 
print(f"even_count :{even_count} and oddcount: {odd_count}")