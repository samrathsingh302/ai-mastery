def contains_duplicate(nums):
    seen = []
    for num in nums: 
       if num in seen:
         return True
       else:
         seen.append(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3]))
print(contains_duplicate([]))
