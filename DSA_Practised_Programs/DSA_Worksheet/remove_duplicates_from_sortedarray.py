def remove_duplicates(nums):
    # return list(set(nums))  # does not gaaurantee order
    return list(dict.fromkeys(nums))

nums = [1,1,2,3,4,4,5,6]
print(remove_duplicates(nums))